# San Alberto 2016: Pony

**Category:** Cryptography  
**Challenge designer:** Valentin Kivachuk  
**Link:** [dafi.inf.um.es/pony/](http://dafi.inf.um.es/pony/)   
**Description:**  
> Por la facultad se rumorea que Hasbro va a sacar un nuevo pony. Alguien ha conseguido cierta información confidencial, pero no han sido capaces de desencriptarla.
>
> Te ves capaz?
>	
> strlen(x)=**63**  
> sha512sum(x)=**9f8678a1b774c9d727a7a5a8be43b69b65dbb09bdc817f26bb4ea5867aead43cc9a07b0bea17640447700ff00804478db56c7c8a445fc7a3db09d145fe6871d6**  
> sha256sum(x)=**1b28cb5290c2fc0db389484a9fd7eb003ab1a1656a6117fe48b2b43e6377252a**  
> password_pattern=**[0-9]{63}**

**Hints:**
> \#1: Más vale maña que fuerza. Seguid buscando ;)  
> \#2: Una imagen vale más que 10^63 palabras  
> \#3: < html>La belleza está en el interior < /html>  
> \#4: 
> ![](https://github.com/vk496/SanAlberto_2016/raw/master/Pony/image.jpg)   
> \#5: Abrir el 7z implica resolver el reto ;)  
> \#6: https://youtu.be/fP22QqI32qs?t=7m19s  
> \#7: Mister_X tool  

## Write-up

![](https://github.com/vk496/SanAlberto_2016/raw/master/Pony/pony.jpg)

Empezamos por bajarnos el archivo y analizar que es exactamente.

```bash
$ file PonySecreto.exe 
PonySecreto.exe: 7-zip archive data, version 0.3
```

Al intentar abrirlo, nos pide una contraseña. Romper una contraseña de 10^63 combinaciones es un poco complicado **#1**, asi que buscamos algo raro en la web **#3**.

```bash
$ curl -s dafi.inf.um.es/pony/ |wc -l
5969
```

Demasiado texto...¿Qué raro no? A lo mejor hay comentarios escondidos.


```bash
$ curl -s dafi.inf.um.es/pony/ |grep !
<!--TFthLWNdR1twLXJdW2EtY11bbi1wXUNbbi1wXW5bci10XXsyfWFbci10XWVbbS1vXWFfW3Qtdl1b-->
<!--ai1sXVsyLTRdWzYtOV17Mn0K-->
```

Parece base64. 

```bash
$ echo TFthLWNdR1twLXJdW2EtY11bbi1wXUNbbi1wXW5bci10XXsyfWFbci10XWVbbS1vXWFfW3Qtdl1bai1sXVsyLTRdWzYtOV17Mn0K | base64 -d
L[a-c]G[p-r][a-c][n-p]C[n-p]n[r-t]{2}a[r-t]e[m-o]a_[t-v][j-l][2-4][6-9]{2}
```
Parece el patrón de una contraseña. Aunque no tiene pinta de ser del 7z, pues pone que su contraseña es de 10^63. Seguimos bsucando... en la imagen. **#2**

```bash
$ wget http://dafi.inf.um.es/pony/img/pony.jpg
--2016-10-30 13:23:54--  http://dafi.inf.um.es/pony/img/pony.jpg
Resolviendo dafi.inf.um.es (dafi.inf.um.es)... 155.54.204.189
Conectando con dafi.inf.um.es (dafi.inf.um.es)[155.54.204.189]:80... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 84221 (82K) [image/jpeg]
Guardando como: “pony.jpg”

pony.jpg            100%[===================>]  82,25K  --.-KB/s    in 0,08s   

2016-10-30 13:23:54 (1,07 MB/s) - “pony.jpg” guardado [84221/84221]
```

Vamos a ver si realmente es una imagen.

```bash
$ file pony.jpg
pony.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 631x355, frames 3 
```

Pues parece que si... Al menos la cabecera. 

```bash
$ xxd pony.jpg| tail -1
000148f0: 0001 0036 0000 00a2 0100 0000 00         ...6......... 
```

hmmm... Los jpg empiezan por la cabecera **ff d8** y terminan por **ff d9**, pero este no es el caso. Probemos a buscar lo que hay dentro...

```bash
$ binwalk -Me pony.jpg 

Scan Time:     2016-10-30 13:27:49
Target File:   /pony.jpg
MD5 Checksum:  97cd8e61088ed77775a82016d0df8162
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
83727         0x1470F         Zip archive data, at least v2.0 to extract, compressed size: 380, uncompressed size: 652, name: test.cap
84199         0x148E7         End of Zip archive


Scan Time:     2016-10-30 13:27:49
Target File:   /_pony.jpg.extracted/test.cap
MD5 Checksum:  97aeee31b691860858bca394023d1951
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

```

Analizando **test.cap** con Wireshark podemos ver que tiene una trama del protocolo 802.11. Esto nos da a entender que tiene que ver algo con el WiFi **#6**. Además, investigando un poco la pista **#7** en Google, deducimos que se menciona a la suite **aircrack-ng**

¿Es posible que tenga que ver con romper WiFi?

```bash
$ aircrack-ng test.cap 
Opening test.cap
Read 4 packets.

   #  BSSID              ESSID                     Encryption

   1  30:39:26:2B:67:DD  vk496                     WPA (1 handshake)

Choosing first network as target.

Opening test.cap
Please specify a dictionary (option -w).


Quitting aircrack-ng...

```

Efectivamente, tenemos un hanshake que tenemos que romper... Tendrá algo que ver la expresión regular de **#3**? No nos queda otra que probarlo...

Creamos un script que nos genere el patrón

```bash
# test.sh
#
# L[a-c]G[p-r][a-c][n-p]C[n-p]n[r-t]{2}a[r-t]e[m-o]a_[t-v][j-l][2-4][6-9]{2}
#
for x1 in {a..c}; do 
for x2 in {p..r}; do 
for x3 in {a..c}; do 
for x4 in {n..p}; do 
for x5 in {n..p}; do 
for x6 in {r..t}; do 
for x7 in {r..t}; do 
for x8 in {r..t}; do 
for x9 in {m..o}; do 
for x10 in {t..v}; do 
for x11 in {j..l}; do 
for x12 in {2..4}; do 
for x13 in {6..9}; do 
for x14 in {6..9}; do 
echo L${x1}G${x2}${x3}${x4}C${x5}n${x6}${x7}a${x8}e${x9}a_${x10}${x11}${x12}${x13}${x14}; 
done;
done;
done;
done;
done;
done;
done;
done;
done;
done;
done;
done;
done; 
done
```

Y lo dejamos ejecutando...

```bash
$ ./test.sh |aircrack-ng --bssid 30:39:26:2B:67:DD test.cap -w-
```

Tras un tiempo, descubrimos que hemos dado con la pass :D

```

                                 Aircrack-ng 1.2 beta3


                   [00:00:00] 1 keys tested (927.86 k/s)


                    KEY FOUND! [ LaGranContrasena_vk496 ]


      Master Key     : C6 A8 AC 7C 7A EC 83 9E D7 59 67 74 C9 AC 40 E2 
                       30 5C 88 61 F5 87 6A EB C1 E0 49 28 39 BC 14 71 

      Transient Key  : 0D 68 D6 B9 4B 61 6B E5 66 C2 3C DC 06 D0 69 13 
                       23 61 EB 68 9E 9A AF DF 9D DB AA AE 7D 81 70 2D 
                       BF 50 46 66 76 C8 67 83 23 9B 7F 83 1A 8A 8E F7 
                       D5 40 82 68 6E 4C 93 69 D5 F1 CD B8 B1 5A 49 4B 

      EAPOL HMAC     : FF 15 D5 DF DC 68 DB C5 98 CC 14 33 EF 52 8D 32
```

Sin embargo, no podemos abrir el 7z con ella... Se nos escapa algo. Y ese algo nos lo dice la pista **#4**. Octal!

```bash
$ ./text_to_octal LaGranContrasena_vk496 | tr -d " "
114141107162141156103157156164162141163145156141137166153647166
$ ./text_to_octal LaGranContrasena_vk496 | tr -d " " | sha512sum 
9f8678a1b774c9d727a7a5a8be43b69b65dbb09bdc817f26bb4ea5867aead43cc9a07b0bea17640447700ff00804478db56c7c8a445fc7a3db09d145fe6871d6  -
$
```

Abrimos el 7z y ahí tenemos nuestro flag :D


```
Enhorabuena!

Has pasado el reto. Envía un MP a la cuenta de @dafi_um con este mensaje:

SanAlberto2016{Pru3ba_h3chA_p0r_vk496!}
```
