#!/bin/bash
link1="https://www.mediafire.com/file/sa2m62njvodogl1/El-SaYaDyn_WhatsApp.apk/file"
if [ -z $1 ]
then
	if [ -z $1 = "EL" ]
	then
	xdg-open $link1
	printf "\033[37;1m[+]\033[32;1m Link : $link1 \n\033[37;1m"
	read -p "[!] Enter Untuk Kembali" b
#	sh Tools/dwl_wq/dwl.sh
	fi
fi

