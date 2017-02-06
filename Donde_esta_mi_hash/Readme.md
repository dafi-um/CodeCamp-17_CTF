# ¿Dónde está mi hash?

Nos han proporcionado un fichero comprimido que contiene 100 ficheros. Cada uno contiene un hash aparentemente aleatorio, pero en uno de ellos coincide con el hash del código que se encuentra entre llaves en su nombre. Encuentra el nombre del fichero y habrás conseguido tu bandera.

---------------------------

#Solución

Para recrear el problema, podemos usar el script en python llamado **crear.py**. Para encontrar la solución, podemos usar un pequeño script en bash **encuentra.sh**.

```
#!/bin/bash

for i in * 
do 
  dato=$(echo $i | cut -f2 -d"{" | cut -f1 -d"}") 
  hash=$(echo -n $dato | sha1sum | cut -f1 -d" ")
  contenido=$(cat $i)
  if [ "$hash" == "$contenido" ]
  then echo $i 
  fi 
done
```


