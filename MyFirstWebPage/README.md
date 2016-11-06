# San Alberto 2016: MyFirstWebPage

**Category:** Cryptography  
**Challenge designer:** Valentin Kivachuk  
**Link:** http://dafi.inf.um.es/MyFirstWebPage/  
**Description:**  

**Hints:**
> \#1: [https://youtu.be/XXjeSXk8dPw](https://youtu.be/XXjeSXk8dPw)  
> \#2: Sólo los que tengan style podrán resolver el reto ;)  


## Write-up

Lo primero podemos que ver al entrar en el reto es una plantilla (muy molona :P) de una web que tiene un enlace al final. Al darle la primera vez, se nos abre la misma página pero con dos pequeñas diferencias:

1. Ya no hay enlace al siguiente link. Solo texto
2. Una extraña letra al principio

¿Por qué no recopilar todas las letras? Al fin y al cabo, lo que importa es lo que te llevas durante el viaje :D #1


```bash
#!/bin/bash

subURL=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/| grep -E "/[a-zA-Z0-9]*\.html" -o | tail -1)
char=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| head -1 | cut -c 1)

p=0

while [ $subURL ]; do

####
let p=$p+1

echo $char

subURL=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| grep -E "/[a-zA-Z0-9]*\.html" -o | tail -1)
char=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| head -1 | cut -c 1)

done

>&2 echo $p

```

Probamos a ejecutar

```bash
$ ./testv1.sh | tee salida
...
...
R
n
C
g
o
=
503
```

No salen letras hasta que llega un punto en el que termina. Lo curioso es el caracter con el que termina, un **=**. Será base64¿?


```bash
$ cat salida | tr -d "\n" | base64 -d
Te pido disculpas por tenerte tanto tiempo dando a los enlaces. Si has sido listo, habrás llegado aqui por algún atajo. Enhorabuena.

Aún así, siento decirte que ha sido en vano. Aquí no está lo que buscas :P

Con amor y ternura, la Delegación de Alumnos de la Facultad de Informática :)

Disfruta de algo de música para compensar: https://youtu.be/vMkwqC48fDg


```

Muy gracioso... 503 links para reirse de nosotros...

Mirando mas detenidamente, nos damos cuenta que la hoja de estilos (comunmente denominada style.css #2 ) tiene un nombre muy raro


```bash
$ curl -s http://dafi.inf.um.es/MyFirstWebPage/ | grep text/css
	<link rel="stylesheet" href="stylle.css" type="text/css" />
```

**stylle.css**... Casualidad¿?

Está así en todas las paginas¿?


```bash
#!/bin/bash


subURL=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/| grep -E "/[a-zA-Z0-9]*\.html" -o | tail -1)
char=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| head -1 | cut -c 1)

p=0
s=0

while [ $subURL ]; do

####
let p=$p+1

if curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| grep -q stylle.css; then
let s=$s+1
else
echo "##### $subURL #####"
fi


echo $char

subURL=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| grep -E "/[a-zA-Z0-9]*\.html" -o | tail -1)
char=$(curl -s http://dafi.inf.um.es/MyFirstWebPage/$subURL| head -1 | cut -c 1)

done

>&2 echo $p
>&2 echo $s
```

```bash
$ ./test.sh | tee salida
...
...
503
501
```

Pues parece que tenemos algo... 

```bash
$ cat salida | grep \#
##### /qXVLSRfa5a6LxLItoE6Rt3ytOMrkclsQ.html #####
##### /rXN8P57gc4CkTg6jtJiwlEtAcbLvt9C3.html #####
```

Comprobemos que tiene exactamente.


```bash
$ curl -s http://dafi.inf.um.es/MyFirstWebPage/qXVLSRfa5a6LxLItoE6Rt3ytOMrkclsQ.html | grep text/css
	<link rel="stylesheet" href="styIle.css" type="text/css" />
```

Esto es sospechoso... **styIle.css** en vez de **styIle.css**. Cuando abrimos ese .css, parece que tiene demasiadas lineas... Tiene toda la pinta de esconder un comentario


```bash
$ curl -s http://dafi.inf.um.es/MyFirstWebPage/styIle.css | wc -l
6187
$ curl -s http://dafi.inf.um.es/MyFirstWebPage/styIle.css | grep !
<!--SanAlberto2016{Enh0rabu3nnA_p0r_d35cubr1r_3l_f1a6_:D}-->
```

