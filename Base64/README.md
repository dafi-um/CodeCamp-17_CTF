# Base64

==gCD9GZlNUYtBXM3sXY1kWb0gWf

Solucion: **CodeCamp17{a5im4h}**

-------------------------------------------------------

El titulo nos lo dice: Base64. Sin embargo, tenemos que darnos cuenta de que está invertido.
```
$ echo ==gCD9GZlNUYtBXM3sXY1kWb0gWf | rev |base64 -d
}h4mi5a{71pmaCedoC
```

Una vez mas, darse cuenta de que está invertido:

```
$ echo ==gCD9GZlNUYtBXM3sXY1kWb0gWf | rev |base64 -d | rev
CodeCamp17{a5im4h}
```

