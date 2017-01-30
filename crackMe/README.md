# CrackMe

/Td6WFoAAATm1rRGAgAhARwAAAAQz1jMAQAgYTZlYjQ4NmM5ZWVkOWU1ZDVjMGQwNGMwYTgxNGE0ZWEKAAAAAHAppTFkzuL8AAE5Ic8oa2IftvN9AQAAAAAEWVo=

Salt: S0mrIdlZvI

Solucion: a6eb486c9eed9e5d5c0d04c0a814a4ea

Hit: Dont crack me :)

-------------------------------------------------------


Está claro a primera vista que es base64

```bash
echo "/Td6WFoAAATm1rRGAgAhARwAAAAQz1jMAQAgYTZlYjQ4NmM5ZWVkOWU1ZDVjMGQwNGMwYTgxNGE0ZWEKAAAAAHAppTFkzuL8AAE5Ic8oa2IftvN9AQAAAAAEWVo=" | base64 -d > output
```

si le echamos file, vemos que es un comprimido

```bash
$ file output 
output: XZ compressed data
```

Descomprimos directamente en la terminal:

```bash
$ xz output -dc
a6eb486c9eed9e5d5c0d04c0a814a4ea
```

Tiene pinta de ser MD5. En este punto, mucha gente se rayará para romper el MD5. Sin embargo, la respuesta es directamente el hash :)
