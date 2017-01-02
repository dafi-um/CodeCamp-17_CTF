Descifrar con RSA el texto “BYWF” dados los números primos  p=257 y q=337, usando como alfabeto de entrada de 26 caracteres [A, B, …, Z], donde A=0, ... ,Z=25.
R: “CAMP”

Utils: http://www.criptored.upm.es/software/sw_m001e.htm



Write-up:

Dado el alfabeto de entrada y su representación decimal:
```bash
A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9,  K=10,  L=11,  M=12,  N=13,  O=14,  P=15,  Q=16,
R=17,  S=18,  T=19,  U=20,  V=21,  W=22,  X=23,  Y=24,  Z=25
```

Se explica primero el cifrado:

CAMP se codifica en base 26 como: 
```bash
2*26^3 + 0*26^2 + 12*26^1+ 15 =  35152+0+312+15 = 35479
```

Cálculo del módulo(n):
```bash
n = p\*q = 257*337 = 86609
```

Cálculo del exponente (e) 
```bash
(p-1)*(q-1) = 256*336 = 86016
e = 17  / mcd(17,86016)=1
```

Cálculo de la clave privada (d): 
```bash
e * d= 1 mod 86016 = 17 * d = 1 mod 86016 →   d = 65777 (Extended Euclidean Algorithm, usando el software de ayuda)
```

Operación de Cifrado:
```bash
C= 35479^e mod n = 35479^17 mod 86609 = 34377
```

Paso a base 26:
```bash
34377 / 26 = 1322 R 5
1322 / 26 = 50 R 22
50 / 26 = 1 R 24
= 1*26^3 + 24*26^2 + 22*26^1 + 5  > 1=B, 24=Y, 22=W, 5=F
```

CRIPTOGRAMA = BYWF

Ahora se explica el descifrado, para poder descifrar es necesario conocer los valores de d y n:

Operación de Descifrado:
```bash
P = C^d mod n = C^65777 mod 86609 = 34377^65777 mod 86609 = 35479  (Por el teorema del resto chino, usando software de ayuda)
```

Como se ha visto anteriormente 35479 = CAMP

