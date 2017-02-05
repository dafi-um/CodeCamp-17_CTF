A tus manos ha llegado, por casualidad, un archivo denominado “confidencial.zip”, este archivo contiene información 
sobre una contraseña de administrador (admin) de un equipo. ¿Puedes encontrarla? 
    R=CodeCamp17{CTFIPSEC}

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

Si la salida del descifrado la guardamos en un archivo, podemos comprobar que este archivo es un archivo comprimido .tar.gz 
(puede verse en linux con el comando file o en windows con herramientas como FileTypeID)

Si descomprimimos el archivo se obtienen otros dos archivos: data.pcap y ip_xfrm_state_output.txt. El primero, al abrirlo con 
Wireshark se ve que contiene trazas del tipo ESP, es decir, trazas cifradas mediante IPsec. Si abrimos el archivo .txt veremos 
que es una salida del comando ip xfrm state, es decir, los datos de dos Asociaciones de Seguridad (SA) IPsec, "probablemente" con
las que se ha protegido los paquetes capturados. 

Para comprobarlo cargamos la información de las SAs en Whireshark (Edit→ Preferencias→ Protocolos → ESP). 
Si la información es introducida correctamente Whireshark detectará que esos paquetes corresponde a una conexión Telnet, 
a un equipo con IP 10.1.0.2, y desde el equipo 10.0.0.2. 

Haciendo un análisis del flujo TCP veremos que la conexión se ha realizado con el usuario “admin”, y la contraseña 
es “CodeCamp17{CTFIPSEC}”. 
