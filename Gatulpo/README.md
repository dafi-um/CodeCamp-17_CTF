# Gatulpo

¿Quién es tu salvador?

SOLUCION: **CodeCamp17{Th3_R34L_G1tHu8_Ma57eR}**

-------------------------------------------------------


La gente se tiene que apañar para encontrar la bandera escondida en uno de los repositorios de DAFI en GitHub.

Si investigan a "ojo", podrán encontrar esto de aquí:

https://github.com/dafi-um/CodeCamp-17/commit/9ffd44f8792495d0d7d825548074d3b3b78fafae

**bandera{Gi7hu6_Ma5tt3r}**

Sin embargo, no sigue nuestro patrón del evento. Para ser mas precisos, efectuamos una busqueda más exhaustiva:

```bash
$ git clone https://github.com/dafi-um/CodeCamp-17
$ cd CodeCamp-17
$ $ git log --all -G"CodeCamp17" -p | grep -Ei "CodeCamp17\{*\}*"
-        <h2>Valentin Kivachuk</h2> <!-- CodeCamp17{Th3_R34L_G1tHu8_Ma57eR} -->
+        <h2>Valentin Kivachuk</h2> <!-- CodeCamp17{Th3_R34L_G1tHu8_Ma57eR} -->
```

Ahí tenemos nuestro flag

**CodeCamp17{Th3_R34L_G1tHu8_Ma57eR}**
