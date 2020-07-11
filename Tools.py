import os

def menu():

	print("""
.########..#######...#######..##........######...######.
....##....##.....##.##.....##.##.......##....##.##....##
....##....##.....##.##.....##.##.......##.......##......
....##....##.....##.##.....##.##........######...######.
....##....##.....##.##.....##.##.............##.......##
....##....##.....##.##.....##.##.......##....##.##....##
....##.....#######...#######..########..######...######.
========================================
Created by AnonHackerSamir
Ver: 2.0
----
СДЕЛАНО ДЛЯ ТЕРМУКСА!
----
==========================================
00. Превратите свой Android в Хакерскую машину.
------------------------------------------
1. Скачать Nmap
2. Скачать Hydra
3. Скачать SQLMap
4. Скачать Metasploit
5. Скачать Ngrok
6. Скачать Kali Nethunter
7. Скачать AngryFuzzer
8. Скачать Red_Hawk
9. Скачать Weeman
10. Скачать IPGeoLocation
11. Скачать Cupp
12. Скачать Instagram Bruteforcer (инстаграмвзлом)
13. Скачать Twitter Bruteforcer (твиттерснайпер)
14. Скачать Ubuntu
15. Скачать Fedora
16. Скачать viSQL
17. Скачать Hash-Buster
18. Скачать D-TECT
19. Скачать routersploit
------------------------------------------
99. Выход
==========================================
""")

loop = True

while loop:
	menu()
	what = input("#: ")
	if what == "00":
		print("================================")
		print("Это установит: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit и viSQL в один клик.")
		print("----------------")
		hm = input("[?] Вы хотите продолжить? (y/n): ")
		print("================================")
		if hm == "y":
			print("========================================================")
			print("[+] Пожалуйста, положи свой андроид и иди в туалет...")
			print("Потому что это займет много времени.")
			print("========================================================")
			os.system("pkg update")
			os.system("pkg install -y git")
			os.system("pkg install -y python")
			os.system("pkg install -y python2")
			os.system("pkg install -y wget")
			os.system("pkg install -y nmap")
			os.system("pkg install -y hydra ")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg install wget")
			os.system("cd /data/data/com.termux/files/home && wget https://Auzilus.github.io/metasploit.sh")
			os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
			os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
			os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
			os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
			os.system("cd /data/data/com.termux/files/home && bundle install")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
			os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
			os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
			os.system("cd /data/data/com.termux/files/home && pip2 install requests")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y php")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y python2")
			os.system("pkg install -y git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
			os.system("cd /data/data/com.termux/files/home && cd weeman")
			os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
			os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
		    os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
			os.system("cd /data/data/com.termux/files/home")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python")
		    os.system("pkg install -y nano")
		    os.system("pip install requests")
			os.system("pip install beautifulsoup4")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
		    os.system("pkg update -y")
		    os.system("pkg install -y git")
			os.system("pkg install -y python")
			os.system("pip install mechanicalsoup")
			os.system("pkg install -y nano")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
			os.system("pkg update -y")
			os.system("pkg install -y git")
		    os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
		    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
		    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
			os.system("cd /data/data/com.termux/files/home && cd routersploit")
			os.system("pip2 install -r requirements.txt")
			os.system("pip2 install -r requirements-dev.txt")
			os.system("pip2 install -r requests")
			os.system("clear")
			print("========================================")
			print("[+] Все успешно установлено :)")
			print("[+] Веселого Хакинга <3")
			print("========================================")
		else:
			rmenu = inpit("[?] Назад в меню? (y/n): ")
			if rmenu == "y":
				menu()
			else:
				break
	if what == "1":
		os.system("cd /data/data/com.termux/files/home")
		os.system("pkg update -y")
		os.system("pkg install -y nmap")
		os.system("cd /data/data/com.termux/files/home")
		print("========================================")
		print("[+] nmap успешно установлено :)")
		print("========================================")
		rmenu = input("[?] Назад в меню? (y/n): ")
		if rmenu == "y":
			menu()
		else:
			break
	elif what == "2":
		os.system("cd /data/data/com.termux/files/home")
	    os.system("pkg update -y")
	    os.system("pkg install -y hydra")
	 	os.system("cd /data/data/com.termux/files/home")
		print("====================================")
		print("[+] hydra успешно установлена :)")
		print("[+] Введите 'hydra' чтобы начать.")
		print("====================================")
		rmenu = input("[?] Назад в меню? (y/n): ")
		if rmenu =="y":
			menu()
		else:
			break
	elif what =="3":
		os.system("cd /data/data/com.termux/files/home")
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
		os.system("cd /data/data/com.termux/files/home")
		        print("====================================")
		        print("[+] SQLMap успешно установлена :)")
		        print("[+] Идите в папку с sqlmap и введите команду 'python2 sqlmap.py' чтобы начать.")
		        print("====================================")
		        rmenu = input("[?] Назад в меню? (y/n): ")
		        if rmenu == "y":
		            menu()
		        else:
		            break
		    elif what =="4":
		    	os.system("pkg install -y wget")
		    	os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
		    	os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
		    	os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
		    	os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
		    	os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
		    	os.system("cd /data/data/com.termux/files/home && bundle install")
		    	os.system("cd /data/data/com.termux/files/home")
		    	        print("====================================")
		    	        print("[+] Metasploit успешно установлен :)")
		    	        print("[+] Введите 'msfconsole' чтобы начать.")
		    	        print("====================================")
		    	        rmenu = input("[?] Назад в меню? (y/n): ")
		    	        if rmenu == "y":
		    	            menu()
		    	        else:
		    	            break
		    	    elif what == "5":
		    	        os.system("pkg update -y")
		    	        os.system("pkg install -y git")
		    	        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
		    	        os.system("cd /data/data/com.termux/files/home")
		    	        print("====================================")
		    	        print("[+] ngrok успешно установлен :)")
		    	        print("[+] Перейдите в папку с ngrok и введите './ngrok http 80' чтобы начать.")
		    	        print("====================================")
		    	        rmenu = input("[?] Назад в меню? (y/n): ")
		    	        if rmenu == "y":
		    	            menu()
		    	        else:
		    	            break
		    	elif what == "99":
		    		print("До встречи.")
		    		break