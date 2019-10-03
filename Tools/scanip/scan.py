# _*_ coding=UTF-8 _*_
import os,sys,socket,requests
def main():
	os.system('clear')
	os.system('sh data/logo.sh')
	print
	try:
		r = requests.get("https://github.com")
	except requests.exceptions.ConnectionError:
		print ("\033[37;1m[\033[31;1m×\033[37;1m] \033[31;1mTidak Ada Koneksi")
	else:
		web = raw_input("\033[37;1m[\033[32;1m?\033[37;1m] WEBSITE (\033[33;1mex:google.com\033[37;1m): \033[32;1m")
		try:
			ip = socket.gethostbyname(web)
			print ("\033[37;1m[\033[32;1m√\033[37;1m] IP: \033[32;1m"+ip)
		except socket.gaierror:
			print ("\033[37;1m[\033[31;1m×\033[37;1m] IP: \033[31;1mTidak Di Temukan")
main()
