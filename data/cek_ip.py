# Mau Ngapain Tod?

# Jangan Recode Lah
# Recode = Lemah/Noob
# Github: https://github.com/Bl4ckDr460n
import requests,os,sys,json
def main():
	try:
		r = requests.get('https://api.myip.com/')
		j = json.loads(r.text)
		open("config/ip.txt","w").write(j["ip"])
	except:
		open("config/ip.txt","w").write("\033[31;1mTidak Di Ketahui")
main()
