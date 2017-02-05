# mp3

Estamos en 2009 y acaba de salir un nuevo hit que lo está petando en la facultad. Todos tienen la canción y presumen de ir a sus conciertos en el Fotolog. Todos menos yo :(

Le pedí a un colega si me podría pasar la canción. Así que fui al cyber para conectarme al MSN y guardarla en el mp4.

Sin embargo, tengo la ligera sospecha de que la cancion es un poco rara. Ha rulado por toda la facultad y vete a saber lo que le han hecho. ¿Sabrías decir si está bien?

Hit: No te fies de las extensiones

Solucion: **CodeCamp17{th3y.ar3_g0ing.down.n07.m3}**

-------------------------------------------------------

Para empezar, probamos abrir el archivo. Vemos que se trata de una cancion, por lo que pasaos a buscar algo raro dentro del archivo. Podemos usar herramientas como binwalk

```
$ binwalk -Me song.mp3 

Scan Time:     2017-02-05 15:35:01
Target File:   ./mp3/song.mp3
MD5 Checksum:  fa7b0bb534c055678dbfa7b58da8b1cb
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
570580        0x8B4D4         Cisco IOS experimental microcode, for "z"
7432708       0x716A04        Zip archive data, at least v2.0 to extract, compressed size: 41499, uncompressed size: 165373, name: secret.txt
7474339       0x720CA3        End of Zip archive


Scan Time:     2017-02-05 15:35:03
Target File:   ./mp3/_song.mp3.extracted/secret.txt
MD5 Checksum:  a01370ed90ae0aeb0d46efdedac01135
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
184           0xB8            Copyright string: "Copyright (C) 1992, 1993, 1994, 1995"
394           0x18A           Copyright string: "Copyright (C) 1991, 1992  Linus Torvalds"
```


Vemos que dentro había un zip, que a su vez tenía un archivo de texto secret.txt

Sin embargo, es un señuelo con informacion inutil

Podemos intentar abrir el archivo con un editor de audio como Audacity, pero el archivo no puede ser leido correctamente. Reproduce un ruido extraño y poco mas. Esto nos hace sospechar.

Comprobamos su extensión:

```
$ file song.mp3 
song.mp3: ATSC A/52 aka AC-3 aka Dolby Digital stream, 44.1 kHz,, complete main (CM) 3 front/2 rear, LFE on,, 320 kbit/s
```

Vemos que no se trata de un mp3 sino de un archivo ac3. Probamos a renombrarlo como tal y abrirlo.

Dentro, observamos que el canal 4 no tiene sonido, solo unas simples ondas. Nos podemos dar cuenta de que se trata de codigo morse. Si extraemos la información en codigo morse, tenemos

- .... ...-- -.-- ·-·-·- .- .-. ...-- ··--·- --. ----- .. -. --. ·-·-·- -.. --- .-- -. ·-·-·- -. ----- --... ·-·-·- -- ...--

Que traducido, con algún traductor online de morse, nos da

th3y.ar3_g0ing.down.n07.m3
