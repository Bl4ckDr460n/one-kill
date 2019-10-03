# Mau Ngapain Tod?

# Jangan Recode Lah
# Recode = Lemah/Noob
# Github: https://github.com/Bl4ckDr460n
import os,sys,re,random
def lisen():
	r = []
	path = list(
		"abcdefghijklmnopqrstuvwxyz1234567890")
	for b in range(7):
		r.append(random.choice(path))
		r.append(random.choice(path).upper())
	return "".join(r)
li = lisen()
open("config/lisen.txt","w").write(li)
