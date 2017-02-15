Simulación de peritaje
======================

Creador del reto: Virginio García López (virginiogl@cii-murcia.es)

Antecedentes
------------

La empresa PIRATILLA ha recibido una denunca por parte de la BSA por piratería. Está usando software Windows con varias suites software sin licencia.

El perito hace su intervención (acompañado de la policía), y con una clonadora hardware clona el disco duro donde se encuentra el software pirata.

El disco duro es enorme: de 4TB, y el perito lleva un disco en el que el clonado cabe justito.

El perito llega a casa y tiene que montar el disco duro, pero la clonadora lo ha dividido en trozos de 2GB.

No hay presupuesto para comparar otro disco de ese tamaño, así que hacer un "cat" de los trozos a otro disco duro no es viable...

No hay problema, el perito que sabe mucho de Linux usa un comando que empieza por aff... ¿cuál era?

Al montarlo, el perito se da cuenta de que ¡¡ alguien les ha avisado de la redada !!

Aunque el perito está seguro de que hay evidencias que se pueden recuperar...

Reto
----

Se trata de resolver un caso similar, pero muy simplificado.

Como no es viable dar 4TB de información, vamos a trabajar con una pequeña imagen de unos 30MB.

En este caso los trozos son de 1MB.

Para simular el caso, en lugar de usar el comando "cat" para juntar los trozos, el reto consiste en montar los ficheros sin duplicar el espacio. Es decir, coger los ficheros ctf.000 hasta ctf.029 y montarlos directamente.

Debes usar el comando que empieza por aff..., pero el perito no recuerda. Tendrás que averiguar también el paquete e instalarlo.

Justo antes de resolver el reto llegarás a un punto en el que te encontrarás con un fichero que necesita contraseña.

Necesitarás juntar dos cosas: el offset de la partición y el nombre del fichero que montaste con el comando desconocido que sabemos que empieza por aff.

El objetivo es encontrar la bandera, que es como encontrar el software ilegal borrado (en el caso planteado).

***
Todo lo anterior: Antecedentes + Reto, es público para el que quiera resolver el reto.

Todo lo que viene a continuación es la solución, y es solo para los organizadores del reto (y para ver la solución si no se consigue resolver).
***

Solución
--------

Vamos a crear un directorio de trabajo temporal, y luego descomprimimos el fichero proporcionado.

	mkdir temp
	cd temp
	tar vxfj ../ctf_peritaje.tar.bz2

Se crearán los siguientes ficheros:

	ctf.000
	ctf.001
	ctf.002
	ctf.003
	ctf.004
	ctf.005
	ctf.006
	ctf.007
	ctf.008
	ctf.009
	ctf.010
	ctf.011
	ctf.012
	ctf.013
	ctf.014
	ctf.015
	ctf.016
	ctf.017
	ctf.018
	ctf.019
	ctf.020
	ctf.021
	ctf.022
	ctf.023
	ctf.024
	ctf.025
	ctf.026
	ctf.027
	ctf.028
	ctf.029

Creamos un directorio para el disco completo:

	mkdir disco

Y lo montamos con el comando affuse ¡¡ el comando que no recordaba el perito es affuse !!:


	affuse ctf.000 disco/

Miramos dentro del directorio


	cd disco
	ls

Vemos el siguiente fichero:


	ctf.000.raw


Esto va a ser parte de la contraseña que vamos a necesitar. Lo anotamos.

Lo siguiente es ver las particiones. Podemos usar fdisk. O también mmls.


	mmls ctf.000.raw

Vemos lo siguiente:

	DOS Partition Table
	ffset Sector: 0

	Units are in 512-byte sectors

	      Slot      Start        End          Length       Description
	000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
	001:  -------   0000000000   0000000127   0000000128   Unallocated
	002:  000:000   0000000128   0000055423   0000055296   NTFS / exFAT (0x07)
	003:  -------   0000055424   0000061439   0000006016   Unallocated


Si usamos fdisk (`fdisk -l ctf.000.raw`), el resultado es equivalente.

Como el enunciado dice que es un Windows, vamos a fijarnos en la partición NTFS.

Dice que empieza en 128, y las unidades son sectores de 512 bytes.

Por tanto el desplazamiento en bytes va a ser 128\*512=65536, y la contraseña tiene puesta esta parte en bytes (esto no se indica, hay que probar).

Ya tenemos la clave que vamos a necesitar más adelante. Será "65536ctf.000.raw".

Lo siguiente es montar la partición NTFS.


	mkdir mntpoint1
	mount -o loop,ro,offset=$((128*512)) -t ntfs ctf.000.raw mntpoint1

Vamos a ver lo que hay por ahí:


	cd mntpoint1
	ls

Y vemos esto:

	$RECYCLE.BIN

Miramos a ver...

	cd \$RECYCLE.BIN/
	ls

Aparece el directorio del usuario (hay una papelera de reciclaje por cada usuario).

	S-1-5-21-4190837328-2166985514-1588226223-1001

Entramos y vemos lo que hay:

	cd S-1-5-21-4190837328-2166985514-1588226223-1001/
	ls -l

Aparece esto:	

	total 43
	-rwxrwxrwx 1 root root  129 feb 13 11:34 desktop.ini
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $I1Z20SW.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $I6AOK3A.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IDXIHJ9.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IFDCF9A.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IFHUIBC.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IGTVEAP.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $ILMW18E.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IMHWI8H.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $ISDH8QV.rar
	-rwxrwxrwx 1 root root   76 feb 13 11:34 $IV1JER8.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $R1Z20SW.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $R6AOK3A.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RDXIHJ9.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RFDCF9A.rar
	-rwxrwxrwx 1 root root  688 feb 13 11:30 $RFHUIBC.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RGTVEAP.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RLMW18E.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RMHWI8H.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RSDH8QV.rar
	-rwxrwxrwx 1 root root 1000 feb 13 11:30 $RV1JER8.rar

Parece que se han borrado varios ficheros rar.

Vemos que hay unos que empiezan por $I de 76 bytes, y otros que empiezan por $R de 1000 bytes.

Hay una correspondencia entre ellos, por ejemplo $I1Z20SW.rar corresponde con $R1Z20SW.rar, es decir solo cambia la primera letra.

Miramos un fichero cualquiera de los pequeños, a ver...

	cat \$I1Z20SW.rar

Y vemos que entre algunos caracteres raros se distingue esto:

	E:\codecamp.part009.rar

Vale, ese fichero en la papelera correspondía a codecamp.part009.rar.

Sabemos lo siguiente:
- En los ficheros que empiezan por $I está el nombre de fichero original antes de enviar a la papelera de reciclaje

- En los ficheros $R están los ficheros originales que hay que restaurar

Por tanto podemos ir mirando cada fichero $I, buscar su correspondiente $R y copiarlo con el nombre original.

Esto puede hacerse fichero por fichero manualmente, o bien con un pequeño script.

Por ejemplo:

	for i in \$I* ; do echo "$i "$(cat $i) ; done | cut -d. -f1,3 | sed "s|\$I\(.*\)\.\(.*\)|cp \\\\\$R\1.rar /tmp/codecamp.\2.rar|g"

Eso da la siguiente salida:

	cp \$R1Z20SW.rar /tmp/codecamp.part009.rar
	cp \$R6AOK3A.rar /tmp/codecamp.part004.rar
	cp \$RDXIHJ9.rar /tmp/codecamp.part006.rar
	cp \$RFDCF9A.rar /tmp/codecamp.part003.rar
	cp \$RFHUIBC.rar /tmp/codecamp.part010.rar
	cp \$RGTVEAP.rar /tmp/codecamp.part008.rar
	cp \$RLMW18E.rar /tmp/codecamp.part005.rar
	cp \$RMHWI8H.rar /tmp/codecamp.part002.rar
	cp \$RSDH8QV.rar /tmp/codecamp.part007.rar
	cp \$RV1JER8.rar /tmp/codecamp.part001.rar

Copiamos y pegamos esto en bash...

Y ya tenemos los ficheros en /tmp

Ahora descomprimimos:

	unrar x /tmp/codecamp.part001.rar

Metemos la clave que obtuvimos antes: 65536ctf.000.raw

Y vemos que ha sacado un fichero llamado codecamp.pdf

Miramos lo que tiene:

	pdftotext /tmp/codecamp.pdf -


Y vemos esto:

CodeCamp17{7812034DU}

**¡ Enhorabuena !**

Notas técnicas
--------------
Realmente no es necesario averiguar el offset para montar el fichero ctf.000.raw, ya que se puede usar algo como:

	losetup --partscan /dev/loop0 ctf.000.raw
	
No obstante, como el desplazamiento forma parte de la contraseña, al menos se debe echar un ojo a la tabla de particiones.


Al montar el sistema de ficheros NTFS debe hacerse en modo sólo lectura siempre. No solo porque es lo correcto para el análisis forense, sino porque además no se ha desmontado correctamente y va a dar un error. Los que intenten resolver este reto deben darse cuenta de este detalle.


La bandera está oculta en un pdf que a su vez se encuentra en un rar cifrado y troceado. ¿Por qué tanta complicación?. Por un lado se ha metido el pdf dentro de un rar cifrado para evitar que con el comando strings se pueda extraer la bandera.
Y por otro lado el rar se ha cifrado para que si se usa el comando binwalk solo se obtenga un montón de ficheros rar desordenados. Aún en el caso muy improbable de que se consiga ordenarlos, todavía haría falta la clave de descifrado.


El hecho de que la clave del rar se obtenga del offset y el nombre del fichero es algo que fuerza a que, por un lado se conozca el comando affuse, y por otro se entienda la tabla de particiones. Lógicamente se podría tomar el atajo de usar el comando cat para juntar los trozos, pero habría que averiguar de otra manera el nombre de fichero que genera el comando affuse.


La estructura de la papelera de reciclaje es real, y lo aprendido puede usarse para recuperar una papelera de reciclaje de Windows 7, 8, y 10 en Linux sin ninguna herramienta adicional (simplemente entendiendo cómo funciona la Papelera de Reciclaje de Windows).

Pistas
------

1. El comando olvidado por el perito es affuse

2. La contraseña es la concatencación del offset en BYTES junto con el nombre del fichero .raw que se ha montado. Sin espacios ni otros carácteres. La partición NTFS solo se monta en RO.

3. La Papelera de Reciclaje de Windows almacena los nombres de ficheros con el prefijo $I, y el contenido de los ficheros con el prefijo $R. Ambos nombres sin prefijo son iguales.

Epílogo
-------

El reto está pensado para tener una dificultad media/alta y poder resolverse sin necesidad de pistas. Aunque puede resultar sencillo para un usuario experimentado en Linux, para resolverlo hay que tener cierta habilidad con el manejo de Linux, ya que se hacen tareas como crear un fichero virtual con affuse, montar un fichero a partir de un desplazamiento, o emparejar ficheros con un patrón. Espero que este reto, además de ilustrativo de lo que se podría hacer en un peritaje, resulte divertido de resolver.
