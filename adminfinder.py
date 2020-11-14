#!usr/bin/env python
#coding: UTF-*

from urllib2 import Request, urlopen, URLError, HTTPError

def Cetak(a):
    i = 0
    while i<=a:
        print " ",
        i+=1

def Creator():
    Cetak(9); print "++++++++++++++++++++++++++++++"
    Cetak(9); print "+     Tools Admin Finder     +"
    Cetak(9); print "+  Tanggal Dibuat 14/11/2020 +"
    Cetak(9); print "+     Creator : Abdillah     +"
    Cetak(9); print "++++++++++++++++++++++++++++++"
    Creator()
    print "\n\n"
def Admin():
    find = open("kumpulanlink.txt","r"):
        link = raw_input("Masukan URL Target (Contoh : www.contohnya.com \t: "):
    print "\n\nBerhasil nih\t: \n"
    while True:
        sub_link = find.readline()
        if not sub_link:
            break
        request_link = "http://"+link+"/"+sub_link
        request = Request(request_link)
        try:
            response = urlopen(request)
        except HTTPError as gagal:
            continue
        except URLError as gagal:
            continue
        else:
            print "LINK YANG ADMIN =>>",request_link
Admin()
