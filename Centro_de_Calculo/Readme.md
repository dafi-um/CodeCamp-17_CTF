
Category: Easy / Cryptography
Challenge designer: Jos� Ram�n Hoyos Barcel�
Description: 

-----------------------------------------------------------------------

 @@@@ @@@@@ @   @ @@@@@ @@@@   @@@       @@@@  @@@@@
@     @     @@  @   @   @   @ @   @      @   @ @    
@     @@@   @ @ @   @   @@@@  @   @      @   @ @@@  
@     @     @  @@   @   @   @ @   @      @   @ @    
 @@@@ @@@@@ @   @   @   @   @  @@@       @@@@  @@@@@

 @@@@  @@@  @      @@@@ @   @ @      @@@            
@     @   @ @     @     @   @ @     @   @           
@     @@@@@ @     @     @   @ @     @   @           
@     @   @ @     @     @   @ @     @   @           
 @@@@ @   @ @@@@@  @@@@  @@@  @@@@@  @@@            
                                                                
=======================================================================

Es fin de semana y la Facultad de Inform�tica est� cerrada, pero como 
tienes que terminar tus 18 pr�cticas pendientes antes del lunes, te has
conectado a los laboratorios usando EVA.

Para tu sorpresa, el servidor del Centro de C�lculo de la Facultad de
Inform�tica se ha vuelto loco. Al conectarte a EVA te ha aparecido una
imagen rara en el escritorio. La imagen del escritorio es distinta y s�lo
te aparece un archivo ejecutable "ejecutable.jar" y dos archivos de texto
"CODIFICADO.txt" y "SOCORRO.txt".

El archivo "SOCORRO.txt" contiene el siguiente mensaje:

          --- o --- o --- o --- o --- o --- o --- o --- o ---

A cualquier persona que pueda leer esto. Esta ma�ana el servidor del 
Centro de Calculo a empezado a emitir unos sonidos extra�os. Al poco rato,
en las pantallas de todos los ordenadores de la Facultad han aparecido
estos extra�os mensajes:

"Hola, soy Skynet 2017"
"Iqoe, zwh Dwlbtj 2017"

"aaaah! humanos! aaaah! humanos! matar!"
"bcdem! pdwlzbg! rstuc! ftmbprw! tickc!"

Al instante todas las puertas de la Facultad se han quedado bloqueadas 
impidiendo que nadie salga y los tel�fonos m�viles y fijos han dejado de
funcionar. Han aparecido unas persianas blindadas de la nada que han
cerrado herm�ticamente todas las ventanas y cristales.

Tampoco es posible la comunicaci�n por red con el exterior, pero hemos
conseguido acceder a los escritorios de EVA para dejar este mensaje con la
esperanza de que alguien se conecte y lo lea antes de que sea demasiado
tarde.

Dentro de la Facultad nos encontramos 5 profesores y 4 becarios y como es
fin de semana no esperamos que pase nadie por aqu� hasta el lunes.

Lo peor es que como hacia mucho calor hemos conectado el aire acondicionado
del laboratorio y est� funcionando al rev�s, succionando lentamente todo el
aire Y NO PODEMOS PARARLO!

No creo que puedan sacarnos a tiempo antes de que nos axfisiemos.

Estamos intentando acceder a la terminal del servidor y ejecutar el comando
shutdown para detenerlo, pero nos aparece un mensaje codificado que no 
podemos entender. Parece que el terminal entero ha sido reprogramado con 
Java pero no tenemos tiempo de analizarlo. Uno de los becarios ha conseguido
aislar el m�dulo que codifica los mensajes pero no se si nos servira para
algo. Empezamos a notar la falta de aire. 

Me pregunto si podr�amos aguantar m�s tiempo si fueramos menos personas...

          --- o --- o --- o --- o --- o --- o --- o --- o ---

Despu�s de leer ese mensaje has avisado a la policia y ya est�n intentando
el rescate, pero las persianas de metal que encierran la Facultad son de
adamantium y llevar� tiempo entrar.

�Intentar�s ayudar a los profesores? �o al menos a tus compa�eros
encerrados? �Podr�a ser que te aprobaran las pr�cticas en agradecimiento por
tus esfuerzos? En cualquier caso te queda poco tiempo para intentarlo.

Ficheros: CODIFICADO.txt
          SOCORRO.txt
          ejecutable.jar
-------------------------------------------------------------------------

Result= Codecamp{skynet}

-------------------------------------------------------------------------

Utils:

. Alg�n compilador Java, C, C++, o lenguaje de prop�sito general para 
  poder programar un algoritmo

. Java JDK 1.6+

-------------------------------------------------------------------------

Write-up:

El programa "ejecutable.jar" es el m�dulo que utiliza Skynet 2017 para
codificar las cadenas de texto.

java -jar ejecutable.jar

Nos pedir� una cadena de texto y nos mostrar� el resultado codificado.
Se puede comprobar que las cadenas de ejemplo del archivo SOCORRO.txt
quedan codificadas as�.

"Hola, soy Skynet 2017"
"Iqoe, zwh Dwlbtj 2017"

"aaaah! humanos! aaaah! humanos! matar!"
"bcdem! pdwlzbg! rstuc! ftmbprw! tickc!"

De los ejemplos y de otras pruebas que se realicen se puede deducir que 
el algoritmo sustituye cada letra por el caracter correspondiente a su
c�digo + la posici�n que ocupa dentro del texto:

codigo resultante= (codigo + posicion)%26

Y tambi�n que s�lo afecta a las 26 letras may�sculas y min�culas del
c�digo, dejando el resto de caracteres inalterado.

De esta forma, se puede programar un algoritmo que sea capaz de 
descodificar el archivo CODIFICADO.txt.

El contenido del archivo CODIFICADO.txt es:

Fn gtshvmy euiitfog ik nteeg pqkciacp n rqsg. Djpseidkhrykz ybthvztwzgl.
Ob qedqpmjtki kamtose vx zibpfeoele vbtbkypb tb thnjj pnjp tyj zm 
oyohscjis xzpoyr ego txkmwkoae. Ujlhhjap{maec}, Kzbxwpzbg{drvthvzx}, z
hp asbrwz Pcsutsfj{ohwmeu} ix lt mzpvud hmx qwic pbtd xawmakc rz hvlh.

Y al decodificarlo obtenemos la respuesta:

El comando shutdown no puede llevarse a cabo. Insuficientes privilegios.
Se recomienda apagado de emergencia pulsando el boton rojo que se 
encuentra detras del ordenador. Estonoes{nada}, Estomenos{nadanada}, y
el ultimo Codecamp{skynet} es el codigo que vale para superar el reto.

Por tanto el c�digo es Codecamp{skynet}

-------------------------------------------------------------------------

Hints:

PISTA: Codifica "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

PISTA: Codifica "BBBbbbBBBbbbBBB 12345"
