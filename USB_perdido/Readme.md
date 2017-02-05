# El USB de Alí Babá

Ha llegado a nuestras manos la imagen iso de un pendrive perdido. Pensamos que
pertenece a un componente de una peligrosa banda criminal y que en algún lugar
debe de tener escondido un fichero con información valiosa (la bandera).

SOLUCION:

CodeCamp17{896745}

---------------------------------------------

La imagen aparentemente contiene una partición FAT16 que podemos montar
fácilmente con **mount**. Sin embargo podemos ver que hay una discrepancia
entre el tamaño del fichero .iso y el de la partición: le faltan megas.
Si ejecutamos:

```
# string usb.iso
```

podemos ver que salen muchas cadenas, entre las cuales puede verse lo 
siguiente justamente al final:

```
NO NAME    FAT16
This is not a bootable disk.  Please insert a bootable floppy and
press any key to try again ... 
VASBIEN
EJEJ
.
EJEJ
..
EJEJ
VASBIEN ZIP 
EJEJ
CLAVE   TXT 
EJEJ
vasbienUT	
vasbienUT
 Bab
 la usaba para entrar a la cueva de los ladrones

```

Esto nos da la pista de que hay una partición borrada. Lo más sencillo es ejecutar **fdisk**:

```
# fdisk usb.iso
```

Y creamos una nueva partición primaria con los valores por defecto, que será el comienzo
a continuación de la que existe y con el tamaño restante.

Si usamos **losetup** prácticamente cualquier linux nos automontará las particiones. Y si no,
las montamos a mano.

```
# losetup -P /dev/loop0 usb.iso
```

Si vamos a la partición recuperada, veremos un directorio llamado "vasbien" y dentro de
él, un fichero *vasbien.zip* y un fichero *clave.txt* que contiene el mensaje anterior 
sobre Alí Babá. Si no se sabe, se puede buscar en google, pero la frase
para abrir la cueva de los 40 ladrones era *"ábrete sésamo"*. Si usamos esa frase sin
espacios y sin tildes para la clave podremos abrir el zip que contiene un fichero
con el código.

-----------------------------------

Si tenemos acceso a herramientas más elaboradas como por ejemplo **binwalk** o **photorec**
podríamos intentar recuperar los archivos directamente del .iso. Lo he comprobado y
no se obtiene una solución obvia. Sin embargo, con **testdisk** se puede detectar fácilmente
que hay otra partición y recuperarla. A partir de ahí ya es igual de fácil que el
procedimiento que describí al comienzo.


