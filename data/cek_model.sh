# Mau Ngapain Tod?

# Jangan Recode Lah
# Recode = Lemah/Noob
# Github: https://github.com/Bl4ckDr460n
# Codded By RUSMANA & BL4CK DR460N
cek(){
	neofetch | grep "Host" | awk {'print $2,$3,$4,$5,$6,$7,$8,$9,$10'}> config/model
}
cek2(){
info=$(cat config/model)
echo "\033[37;1m[!] Merek HP Anda :\033[32;1m $info"
}
cek
cek2
