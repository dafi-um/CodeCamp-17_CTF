# Palomitas

Palomitas de distintos colores y sabores. ¿Podrás con todas?

Solucion: CodeCamp17{e5c85b43fd62f703d6bfc0b6eb7be596}

Hit: El orden de los ingredientes determina su sabor

-------------------------------------------------------


Al extraer el zip, nos encontramos con 44 archivos. De nombre tienen un hash SHA1 y de contenido todas tienen algo codificado con base64. Probamos juntarlo todo y ver que es:

```
$ cat * | base64 -d
}4672beCfo67bc9be53pd6e3a5{fCbdcme07fd5608b1
```

Tiene pinta de ser la solucion, pero no sabemos el orden.

Sin embargo, podemos intentar algún nombre de archivo SHA1 en un cracker online.

Nos damos cuenta de que todos son numeros. Por tanto, probamos a realizar el mismo proceso de forma ordenada (suponemos que van del 0 al 43)

```
$ for i in {0..43};do cat $(echo -n $i | sha1sum | cut -d" " -f1) | base64 -d; done
CodeCamp17{e5c85b43fd62f703d6bfc0b6eb7be596}
```

