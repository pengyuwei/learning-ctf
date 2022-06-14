# CTF-Zip encrypted compression package decryption

```
# echo 'flag\c' > src1.txt
% echo '0123\c' > src2.txt
% echo 'zzzz\c' > src3.txt
% zip -P 9876 ctf.zip *.txt 
  adding: src.txt (stored 0%)

% unzip -v ctf.zip 
Archive:  ctf.zip
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
       4  Stored        4   0% 06-14-2022 15:08 d1f4eb9a  src1.txt
       4  Stored        4   0% 06-14-2022 15:08 a6669d7d  src2.txt
       4  Stored        4   0% 06-14-2022 15:08 19a07b3c  src3.txt
--------          -------  ---                            -------
      12               12   0%                            3 files

% python3 main.py
0123
flag
zzzz
spend time: 23s
```



## performance

MacAir2020(1.1 GHz 4C Intel Core i5): 23s


