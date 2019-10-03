# _*_ coding=UTF-8 _*_
import requests,json,os,sys,time,socket
def banner():
	os.system('sh data/logo.sh')
def tidak(arg):
	print ("\033[37;1m[\033[31;1m×\033[37;1m] \033[37;1m"+arg+": \033[31;1mTidak Di Ketahui")
def sukses(arg,type):
	print ("\033[37;1m[\033[32;1m√\033[37;1m] "+arg+": \033[32;1m"+type)
class main:
	def __init__(self):
		self.tampil()
	def awal(self):
                os.system('sh run.sh')
	def tampil(self):
		global ip
		banner()
		print
		web = input("\033[37;1m[?] IP: \033[32;1m")
		if "https://" in web or "http://" in web:
			print ("\033[37;1m[\033[31;1m*\033[37;1m] \033[31;1mSepertinya Tools Tidak Mensupport 'https & http")
			raw_input("\033[37;1m[!] Enter Intuk Kembali Ke Menu Awal ")
			self.awal()
		else:
			try:
				ip = socket.gethostbyname(web)
			except:
				ip = web
		self.main(ip)
	def main(self,ip):
		url = "http://ip-api.com/json/%s" %(ip)
		try:
			r = requests.get(url)
		except requests.exceptions.ReadTimeout:
			print ("\033[37;1m[\033[31;1m×\033[37;1m] \033[31;1mKoneksi Error")
		except requests.ConnectionError:
			print ("\033[37;1m[\033[31;1m×\033[37;1m] \033[31;1mTidak Ada Koneksi")
		except (UnboundLocalError,KeyError):
			print ("\033[37;1m[\033[31;1m×\033[37;1m] \033[31;1mKesalahan Tidak Di Ketahui")
		j = json.loads(r.text)
		self.pol(j)
	def pol(self,j):
		print ("\033[33;1m"+50*"=")
		try:
			sukses("AS",j["as"])
		except: tidak("AS")
		try:
			sukses("ISP",j["isp"])
		except: tidak("ISP")
		try:
			sukses("KOTA",j["city"])
		except: tidak("KOTA")
		try:
			sukses("NEGARA",j["country"])
		except: tidak("NEGARA")
		try:
			sukses("KODE NEGARA",j["countryCode"])
		except: tidak("KODE NEGARA")
		try:
			sukses("LAT",j["lat"])
		except: tidak("LAT")
		try:
			sukses("LON",j["lon"])
		except: tidak("LON")
		try:
			if j == 'success':
				sukses("STATUS","ON")
			else:
				print ("\033[37;1m[\033[31;1m×\033[37;1m] STATUS: \033[31;1mOFF")
		except: tidak("STATUS")
		try:
			sukses("ZONA WAKTU",j["timezone"])
		except: tidak("ZONA WAKTU")

main()
