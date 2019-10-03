# Codded By BL4CK DR460N & Rusmana ID
# Copyright (c) Rusmana ID & BL4CK DR460N
# _*_ coding=UTF-8 _*_
import os,sys
class main:
	def __init__(self):
		url = raw_input("\033[37;1m[\033[33;1m?\033[37;1m] Bug Host: \033[32;1m")
		self.scan(url)
		self.scan_now()
	def scan(self,url):
		try:
			open("/data/data/com.termux/files/usr/bin/nmap").read()
			os.system("nmap -p 80 --script dns-brute.nse "+url+" > config/x")
			os.system("cat config/x | grep "+url+" | awk {'print $2'}> config/hasil.k")
			os.system("cat config/hasil.k | grep "+url+" | awk {'print $1,$4'}> config/hasil.bug")
			os.system("rm -rf config/hasil.k config/x")
		except IOError:
			print ("\033[37;1m[\033[31;1mx\033[37;1m] 'nmap' belum di install")
			raw_input("[=] Enter Intuk Menginstall ")
			os.system("pkg install nmap")
	def scan_now(self):
		bug = open("config/hasil.bug").read()
		for url in bug:
			print ("\033[37;1m[\033[33;1m!\033[37;1m] Scanning Now ")
			os.system("curl -m 10 -s -I $1 "+url+" | grep HTTP/1.1 | awk {'print $2,$3'}> config/hasil")
			status =open("config/hasil").read()
			print ("\033[37;1m[\033[32;1m+\033[37;1m] Status: "+status)
			sys.exit()

main()
