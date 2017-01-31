# Bad Password

Un solpón ha chivado que en las ultimas horas ha habido una intrusión en los servidores de la CodeCamp. Según informa, el cracker ha conseguido entrar y publicar información confidencial. Necesitamos tu ayuda para saber que secreto ha filtrado y comunicarnoslo.

Nota: Al admin le gusta el puerto 1911

Solucion: **CodeCamp17{Un_4u7en1Co_Linc3}**

Hit: El valor de las líneas vacías es bien conocido por Alfred Vail

-------------------------------------------------------

Podemos ver que mencionan un puerto concreto. Intentamos conectarnos a él

```bash
$ telnet 127.0.0.1 1911
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Welcome to CTF System
login as: root
password: asdfgh

Bad password.
Connection closed by foreign host.
```

No parece haber mas información. Sin embargo, parece un poco peculiar la línea en medio. Probamos a ver que contiene:

```bash
$ telnet 127.0.0.1 1911 | tee output
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Welcome to CTF System
login as: asd
password: ds

Bad password.
Connection closed by foreign host.
$ xxd output 
00000000: 5472 7969 6e67 2031 3237 2e30 2e30 2e31  Trying 127.0.0.1
00000010: 2e2e 2e0a 436f 6e6e 6563 7465 6420 746f  ....Connected to
00000020: 2031 3237 2e30 2e30 2e31 2e0a 4573 6361   127.0.0.1..Esca
00000030: 7065 2063 6861 7261 6374 6572 2069 7320  pe character is 
00000040: 275e 5d27 2e0a 5765 6c63 6f6d 6520 746f  '^]'..Welcome to
00000050: 2057 6172 5379 7374 656d 0a6c 6f67 696e   CTF System.login
00000060: 2061 733a 2070 6173 7377 6f72 643a 200d   as: password: .
00000070: 0d20 090d 2009 0d0d 0920 0d09 0920 0d0d  . .. .... ... ..
00000080: 2009 090d 0d20 090d 0920 090d 0d20 0909   .... ... ... ..
00000090: 200d 0d09 0d20 0d09 0920 090d 0d09 200d   .... ... .... .
000000a0: 0920 0909 200d 0909 0920 090d 0d09 200d  . .. .... .... .
000000b0: 0909 0d20 090d 2009 0d09 200d 0909 200d  ... .. ... ... .
000000c0: 0d0d 0d09 2009 0d0d 0920 0909 0d0d 200d  .... .... .... .
000000d0: 0d09 2009 0909 200d 0d09 200d 0d0d 0909  .. ... ... .....
000000e0: 200d 0909 2009 0d09 200d 0d0d 0909 200d   ... ... ..... .
000000f0: 090d 200d 090d 200d 0d20 090d 2009 0d0d  .. ... .. .. ...
00000100: 0920 0d0d 0d09 2009 0d0d 0d0d 2009 2009  . .... ..... . .
00000110: 0d0d 200d 0909 0920 090d 2009 090d 0d20  .. .... .. .... 
00000120: 0d09 0d20 0920 0909 0d20 0909 0d0d 0d20  ... . ... ..... 
00000130: 0d0d 2009 0d09 0a42 6164 2070 6173 7377  .. ....Bad passw
00000140: 6f72 642e 0a                             ord..
```

Podemos ver que ese espacio contiene información. Bytes 0d, 20 y 09. Buscando en Internet, podemos ver que son espacios, tabuladores y retornos de carro (\r)


Probamos a darles otro valor mas visual para entender que esconden.


```bash
$ cat output | sed 's/\r/r/g' | sed 's/\t/t/g' 
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Welcome to CTF System
login as: password: rr tr trrt rtt rr ttrr trt trr tt rrtr rtt trrt rt tt rttt trrt rttr tr trt rtt rrrrt trrt ttrr rrt ttt rrt rrrtt rtt trt rrrtt rtr rtr rr tr trrt rrrt trrrr t trr rttt tr ttrr rtr t ttr ttrrr rr trt
Bad password.
```


Vemos que hay alternación de caracteres. Tiene toda la pinta de ser morse.

```bash
$ cat output | sed 's/\r/./g' | sed 's/\t/-/g' 
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Welcome to CTF System
login as: password: .. -. -..- .-- .. --.. -.- -.. -- ..-. .-- -..- .- -- .--- -..- .--. -. -.- .-- ....- -..- --.. ..- --- ..- ...-- .-- -.- ...-- .-. .-. .. -. -..- ...- -.... - -.. .--- -. --.. .-. - --. --... .. -.-
Bad password.
```


Si traducimos del morse, obtenemos el siguiente texto:


INXWIZKDMFWXAMJXPNKW4XZUOU3WK3RRINXV6TDJNZRTG7IK


No tiene pinta de ser Base64. Tenemos que probar algun tipo de codificación distinta, por ejemplo, Base32.

```bash
$ echo "INXWIZKDMFWXAMJXPNKW4XZUOU3WK3RRINXV6TDJNZRTG7IK" | base32 -d
CodeCamp17{Un_4u7en1Co_Linc3}
```
