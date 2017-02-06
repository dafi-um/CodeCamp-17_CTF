#!/bin/bash

for i in * 
do 
  dato=$(echo $i | cut -f2 -d"{" | cut -f1 -d"}") 
  hash=$(echo -n $dato | sha1sum | cut -f1 -d" ")
  contenido=$(cat $i)
  if [ "$hash" == "$contenido" ]
  then echo $i 
  fi 
done

