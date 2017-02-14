A tus manos ha llegado, por casualidad, un archivo denominado “confidencial.zip”, este archivo contiene información 
sobre una contraseña de administrador (admin) de un equipo. ¿Puedes encontrarla? 
    R=CodeCamp17{CTFIPSEC}

Hit: ESP & IPsec :)

Utils:

OpenSSL
Wireshark,
Conexión a Internet

Write-up: 

Se ofrece un archivo denominado “confidencial.zip” que contiene dos archivos: data.aes y estoquesera.txt.
El archivo data.aes es un archivo cifrado mediante AES-128 con contraseña. 
La contraseña se obtiene del contenido estoquesera.txt. En concreto este archivo contiene un hash de 128 bits, es decir, MD5.
Este hash es fácilmente rompible a través de sitios como http://www.md5online.es/

Para descifrar el archivo con la contraseña encontrada podemos usar OpenSSL. 

$openssl enc -aes-256-cbc -d -in data.aes -out fichero_salida

Si la salida del descifrado la guardamos en un archivo, podemos comprobar que este archivo es un archivo comprimido .tar.gz 
(puede verse en linux con el comando file o en windows con herramientas como FileTypeID)

$mv fichero_salida fichero_salida.tar.gz

Si descomprimimos el archivo

$tar -xzvf fichero_salida.tar.gz

se obtienen otros dos archivos: data.pcap y ip_xfrm_state_output.txt. El primero, al abrirlo con 
Wireshark se ve que contiene trazas del tipo ESP, es decir, trazas cifradas mediante IPsec. Si abrimos el archivo .txt veremos 
que es una salida del comando ip xfrm state, es decir, los datos de dos Asociaciones de Seguridad (SA) IPsec, "probablemente" con
las que se ha protegido los paquetes capturados. 

Cada SA se define mediante una IP origen (src) y otra destino (dst) y respresenta los mecanismos con los que se ha protegido el tráfico entre esos dos equipo, en cada dirección. La primera asociación indica el algoritmo de cifrado y autenticación utilizado en el tráfico origen 10.0.0.2 y destino 10.1.0.2. La segunda indica la misma informacin para el tráfico en sentido contrario. 

Para comprobarlo cargamos la información de las SAs en Whireshark (Edit→ Preferencias→ Protocolos → ESP --> ESP SAs --> Edit). 
Aquí habrá que introducir dos entradas, una para cada SA. 
Por ejempo, la primera será:
Protocol: IPv4, Src IP: 10.0.0.2, SPI: 1, Encryption: AES-CBC, Encryption Key: 0x34e1...., Authentication: HMAC-SHA-256-96, Authenticaion Key: 0x34e1....

Si la información es introducida correctamente Whireshark detectará que esos paquetes corresponde a una conexión Telnet, 
a un equipo con IP 10.1.0.2, y desde el equipo 10.0.0.2. 

Haciendo un análisis del flujo TCP (selecciona cualquier paquete TCP, pulsa botón derecho-->Follow-->TCP Stream) veremos que la conexión se ha realizado con el usuario “admin”, y la contraseña 
es “CodeCamp17{CTFIPSEC}”. 
