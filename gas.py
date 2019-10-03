# Mau Ngapain Tod?

# Jangan Recode Lah
# Recode = Lemah/Noob
# Github: https://github.com/Bl4ckDr460n
import os,sys,time,requests
def logo():
	os.system('clear')
	os.system('sh data/logo.sh')
class main:
	def __init__(self):
		logo()
		os.system("python2 data/gen.py")
		self.cek()
	def l(self):
		try:
			open("config/lisen.txt","r").read()
		except IOError:
			os.system("python2 data/gen.py")
	def cek_li(self):
		r = requests.get("https://pastebin.com/raw/Pnhf779K").text
		try:
			data = open("config/lisen.txt","r").read()
		except IOError:
			os.system("python2 data/gen.py")
			id = open("config/lisen.txt","r").read()
			print ("\033[37;1m[!] User ID: %s"%(id))
			raw_input("\033[37;1m[!] Enter To Chat BL4CK DR460N ")
                        os.system("termux-open https://api.whatsapp.com/send?phone=6285797379476&text=konfirmasi saya dengan id: %s"%(data))
                        sys.exit()
		if data == r:
			self.cek()
		else:
			print ("\033[37;1m[!] \033[31;1mUser Not Found\n\033[37;1m[!] Please Contact BL4CK DR460N to confirm user id")
			raw_input("\033[37;1m[!] Enter To Chat BL4CK DR460N ")
			os.system("termux-open https://api.whatsapp.com/send?phone=6285797379476&text=konfirmasi saya dengan id: %s"%(data))
			sys.exit()
	def cek(self):
		os.system('sh data/cek_model.sh')
		os.system('python2 data/cek_ip.py')
		os.system('sh data/tampil_ip.sh')
		os.system("sh data/tampil_lisen.sh")
		os.system('python2 data/menu.py')
main()
