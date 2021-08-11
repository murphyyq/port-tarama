#!/usr/bin/env python 
# encoding=utf-8

import os
import time
import sys


os.system("sudo apt-get install figlet")
os.system("clear")
print("\33[1;35m")
os.system("figlet PORT TARAMA")
print ("""\33[1;33m
       rex - murphyy nnmap kullanrak port tarama turkce 
       aracına hoşgeldiniz
       NOT : BU BİR NMAP ARACISIDIR YANİ BUNU KULLANMAK İÇİN  SİSTEMİNİZDE NMAP KURULU OLMALIDIR\33[1;31m
      1) hızlı tarama
      2) servis ve versiyon tarama
      3) işletim sistemi tarama
      4) exit
      5) ip aralığı tarama
      \33[93m
      KULLANIMI
      \33[1;36mip yi yada url yi girerken protokolleri yazma örn:192.168.1.69 örn:google.com bunun gibi
      """)
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

islemno = input("\33[1;37mişlem numarsını gir dostum: ")
if (islemno == "1"):
    hedef = input("\33[1;41mhedefi gir: ")
    print ("\33[1;45m")
    os.system("sudo nmap " + hedef)
    
elif (islemno == "2"):
    hedef = input("\33[1;41mhedefi girin: ")
    print ("\33[1;44m")
    os.system("sudo nmap -sS -sV " + hedef )
elif (islemno == "3"):
    hedef = input("\33[1;41mhedefi girin: ")
    print ("\33[1;46m")
    os.system("sudo nmap -O " + hedef )
elif (islemno == "4"):
    slowprint("\33[1;41mcıkış yapılıyor...")
    time.sleep(0.2)
    os.system("exit")
elif (islemno == "5"):
    hedef = input("\33[1;41mhedefi girin: ")
    ip_araligi = input("kaçıncı ip ye kadar tarıyayım: "  )
    os.system("nmap " + hedef  + ip_araligi)
    print ("\33[1;45mBunu yapamadım ab kusura bakma")

else:
    print ("DOSTUM SADECE 1-2-3-4-5 SEÇENEĞİNİ SEÇEBİLİRSİN ŞİMDİLİK")
    
