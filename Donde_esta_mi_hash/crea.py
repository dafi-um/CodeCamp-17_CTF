import hashlib
import os
import random
import string

for n in range(1000):
  datoshash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  fichero="CodeCamp17{"+datoshash+"}"
  if n!=47:
    datoshash = datoshash + '0'  # metemos basura al final 
  f=open(fichero,'w')
  mihash=hashlib.sha1()
  cadena = bytes(datoshash,"ascii")
  mihash.update(cadena)
  f.write(mihash.hexdigest())
  f.close()
    

