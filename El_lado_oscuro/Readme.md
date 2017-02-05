
Category: Wit / Search

Challenge designer: José Ramón Hoyos Barceló

Description: 

-----------------------------------------------------------------------
 
                                 ,,@`      ;                        
                         @@@@@@@@@@@'  ,@@@@                        
                          +@@@@@@@@@@  @@@@;                        
                          ,@@@@@    `  +@@@.                        
                           @@@@# ,@    +@@@                         
                           @@@@@@@@    +@@@                         
                           @@@@@@@@    ;@@@                         
                           @@@@@  `  , ;@@@                         
                           @@@@,     : :@@@                         
                           +@@@,    @` :@@@                         
                           ,@@@@@@@@@  :@@:                         
                        `@@@@@@@@@@@@  @@@@                         
 
                                                                    
                ,+@@:                     @@@                       
               .@@@                       @@@                       
                @@@`                      @@@                       
               `@@@;       `@@@ ;@@,  @#@.;@@   ;@@@+               
               .@@@@       @@@@@`@:  @@@@@,@@  @@+,@@@              
               ,@@@@      @@@@ @@@; @@@@ ,@@@ +@  `#@@+             
               :@@@@   `, @@@@  @@' @@@@  @@@ @@``@@@@@             
               ;@@@@   @+ @@@@' @@# @@@@@@@@@ @@@@@@@@@             
               '@@@@,@@@@ @@@@@@@@@ @@@@@@@@@ @@@@@@@@@             
               @@@@@@@@@@ #@@@@@,@@  @@@@@@@@ :@@@@@@@`             
               @@@@@@@@@@  @@@@,;@@  `@@@@@@@  +@@@@@:              
                         `                ,,':   ;@,                
                         
       ,@@@@@@                                                      
      @@@@@@@@@                                                     
     @@@@@   @@@                                                    
    ,@@@@@    @@   @@@@; ,   ,@@@:  ,'@@; ,#@` '@@,,@@#   .@@@@     
    @@@@@@#  ;@@; @@@@@@@   '@@@@@@   @@  '@+   @@+@@@@@ '@@`@@@`   
    @@@@@@@@@@@@@.@@@   .   @@@@@@@` @@@  ,@@:  @@@@@@@@ @:  @@@@   
    @@@@@@@@@@@@+ @@@@@,   :@@@@@    @@@  @@@@  @@@@@@@,'@: @@@@@   
    @@@@@@@@@@@@.  @@@@@@@`@@@@@@   :@@@@@@@@@  @@@   ` @@@@@@@@@   
     @@@@@@@@@@@      @@@@@#@@@@@: @,@@@@@@@@@ .@@`     '@@@@@@@@   
     '@@@@@@@@@   @`  @@@@: @@@@@@@@ @@@@@@@@, ,@@`      @@@@@@@@   
      ;@@@@@@@   @@@@@@@@@  ;@@@@@', .@@@@@@:  :@@@      .@@@@@@    
        ,@@,        ,@@:      ;@:      ,@@,                ,@@      
                                                                    
 
               S4b3m0s qu13n 3r3s y p0rqu3 es74s 4qu1!! 
                              
=======================================================================

Después de apuntarte al CodeCamp 2017, unos desconocidos han entrado en
los servidores de la Universidad de Murcia y han bloqueado las cuentas 
de todos los profesores. Además han dejado trazas con tu nombre de 
usuario y con la dirección IP del ordenador en el que te encuentras
conectado ahora mismo, lo que te convierte en el principal sospechoso
de un delito que no has cometido. 

Para poner a prueba tus conocimientos te han enviado una serie de 
ficheros, uno de los cuales contiene un programa que al ejecutarlo 
restaurará las cuentas de los profesores y borrará todas las pruebas 
que te incriminan, pero el programa sólo funcionará si encuentras el
código correcto.

¿Conseguirás restaurar los servidores antes de que te localizen?

Para salvarte tendrás que conocer el lado osucuro e iniciarte en el
mundo de los hackers!!

Ficheros:
.Pasate_al_lado_oscuro.zip
.La_sabiduria.zip
.La_clave_forma_parte_de_la_historia.zip

-----------------------------------------------------------------------

Result= **CodeCamp17{CAMP5956}**

-----------------------------------------------------------------------

Utils:

. Programa editor gráfico con capacidad de alterar el brillo y contraste
  de una imagen, tipo GIMP, Photoshop, Paintshop pro, etc..

. Programa para abrir archivos comprimidos .zip protegidos con AES, tipo
  7-zip, winrar, winzip, ...

. Java JRE 1.7+

. Conexión a Internet y un navegador web

-----------------------------------------------------------------------

Write-up:

El fichero "Pasate_al_lado_oscuro.zip" contiene dos archivos: una imagen 
"el lado de la luz.jpg" y un archivo leeme.txt. En el archivo de texto 
puede leerse la frase "En la oscuridad está la sabiduría".

La imagen es de una chica con un fondo blanco brillante en el lado derecho.
Mediante un editor gráfico reducimos gradualmente el brillo de la imagen
y aparecerá escrito el texto "busca la senda del mal" a la derecha.

El fichero "La_sabiduria.zip" contiene dos archivos: un archivo 
"Historia_de_hackers.txt" que contiene el "Jargon File" con la jerga y 
cultura hackers; el otro es un archivo leeme.txt que contiene la frase
"Sólo tienes que saber lo que buscar".

Si buscamos la frase "la senda del mal" dentro del archivo 
"Historia_de_hackers.txt" encontraremos una linea que contiene las cadenas:

"la senda del mal" : 'soyunfrikioscuro'

Otra opción es leerse el archivo entero y darse cuenta de que en esa línea 
aparecen esas cadenas extrañas resaltadas.

El fichero "La_clave_forma_parte_de_la_historia.zip" está encriptado con el
algoritmo AES. Contiene dos archivos: una imagen "KM.jpg" y un archivo jar
ejecutable "ejecutame.jar".

La clave para poder descomprimir el archivo es la que encontramos en el
archivo "Historia_de_hackers.txt" (soyunfrikioscuro)

Si ejecutamos el archivo con:

jar -jar ejecutame.jar

el programa nos pedirá tres valores:
COSMOS, MICROCORP SYSTEMS y DIGITAL EQUIPMENT

Dará un error si no se introducen valores numéricos (valor numérico 
esperado). Si se introducen los valores incorrectos nos dará una cadena 
y el mensaje "código incorrecto".

La foto es del conocido hacker Kevin Mitnick. Si no se le reconoce se 
puede realizar una búsqueda en Internet utilizando algún buscador de 
imágenes como

http://images.google.com/

http://www.tineye.com/

Investigando la biografía de Kevin Mitnick se puede comprobar que en 
1981 fué su primera incursión como hacker para asaltar la base de datos 
COSMOS en las oficinas de Pacific Bell. Más tarde, en 1987 fue acusado 
de invadir el sistema de la compañia MICROCORP SYSTEMS, y fue arrestado 
en 1988 por invadir el sistema de la empresa DIGITAL EQUIPMENT.

Si introducimos esos tres valores:

COSMOS: 1981

MICROCORP SYSTEMS: 1987

DIGITAL EQUIPMENT: 1988

el programa producirá la respuesta:

CAMP5956:código correcto

NOTA: El archivo ejecutame.jar no contiene la clave "CAMP5956", por lo 
que no se puede averiguar con un editor hexadecimal.

-----------------------------------------------------------------------

Hints:

. Pasate_al_lado_oscuro.zip

PISTA: "El brillo de la luz se apagará y la oscuridad revelará la verdad"

. La_sabiduria.zip

PISTA: "Tienes que ir por el mal camino"

. La_clave_forma_parte_de_la_historia

PISTA: "Kevin Mitnick"
