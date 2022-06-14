#!/bin/sh

echo 'flag\c' > src1.txt
echo '0123\c' > src2.txt
echo 'zzzz\c' > src3.txt
zip -P 9876 ctf.zip *.txt 
unzip -v ctf.zip 

