# Mau Ngapain Tod?

# Jangan Recode Lah
# Recode = Lemah/Noob
# Github: https://github.com/Bl4ckDr460n

# _*_ coding=UTF-8 _*_
import os,sys,time
class main:
	def __init__(self):
		print ("\033[33;1m"+40*"=")
		self.menu()
	def awal(self):
		os.system('sh run.sh')
	def menu(self):
		print ("\033[37;1m[!] Version: \033[32;1m0.1 \033[37;1m{\033[31;1mLow Version\033[37;1m}\033[0m")
		print ("\033[33;1m"+40*"=")
		print ("\033[37;1m{\033[32;1m1\033[37;1m} \033[33;1mScan IP Website")
		print ("\033[37;1m{\033[32;1m2\033[37;1m} \033[33;1mLacak IP")
		print ("\033[37;1m{\033[32;1m3\033[37;1m} \033[33;1mNick Anggota WCT & BCC")
		print ("\033[37;1m{\033[32;1m4\033[37;1m} \033[33;1mDownload Kumpulan WhatsApp Kebal")
		print ("\033[37;1m{\033[32;1m5\033[37;1m} \033[33;1mScan Bug 200 ok")
		print
		self.pilih()
	def pilih(self):
		p = raw_input("\033[37;1m[\033[32;1m?\033[37;1m] PILIH: \033[32;1m")
		if p == "":
			self.pilih()
		elif p in ["1","01"]:
			os.system('python2 Tools/scanip/scan.py')
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
                        self.awal()
		elif p in ["2","02"]:
			os.system('python Tools/lacak/lacak.py')
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
                        self.awal()
		elif p in ["3","03"]:
			os.system('sh data/anggota.sh')
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
			self.awal()
		elif p in ["4","04"]:
			os.system('sh Tools/dwl_wa/dwl.sh')
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
                        self.awal()
		elif p in ["5","05"]:
			os.system("sh Tools/scan_bug/scan.sh")
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
			self.awal()
		else:
			print ("\033[37;1m[\033[32;1m×\033[37;1m] \033[31;1mPilihan Anda Tidak Di Temukan")
			self.pilih()
main()
