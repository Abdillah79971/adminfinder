#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Cetak(a):
	i = 0
	while i<=a:
		print " ",
		i+=1


def CariAdmin():
	teks = open("kumpulanlink.txt","r");
	link = raw_input("Masukan URL Target (CONTOH : www.contoh.com)\t: ")
	print "\n\nLink ==>\n"
	while True:
		sub = teks.readline()
		if not sub:
			break
		req_link = "http://"+link+"/"+sub
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "LINK YANG BISA DIAKSES ",req_link

def DiCetak():
	Cetak(9); print "+++++++++++++++++++++++++++++++++++++"
	Cetak(9); print "+      Recoded By Abdillah7997      +"
	Cetak(9); print "+         From Zero To Hero         +"
	Cetak(9); print "+         SEKIREI EXPLOITER         +"
	Cetak(9); print "+++++++++++++++++++++++++++++++++++++"

DiCetak()
CariAdmin()
