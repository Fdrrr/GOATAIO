from GradientGen import PrintGradient, PrintLinearGradient
import random
from listset import listset
import datetime
import os
import time 
import sqlite3
import re 
import socket
from discord import SyncWebhook
from colorama import Fore 
import tkinter.filedialog as fd
import ctypes



blue, red, lightred, white, green, cyan, lightblue, reset, magenta, lightmagenta, lightcyan, yellow = Fore.BLUE, Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.YELLOW



NAME = '''

   ▄████      ▒█████       ▄▄▄         ▄▄▄█████▓    ▓█████     ▓█████▄       ██    ▄▄▄█████▓     ▒█████       ██▀███      
▒ ██▒ ▀█▒    ▒██▒  ██▒    ▒████▄       ▓  ██▒ ▓▒    ▓█   ▀     ▒██▀ ██▌    ▒▓██    ▓  ██▒ ▓▒    ▒██▒  ██▒    ▓██ ▒ ██▒    
░▒██░▄▄▄░    ▒██░  ██▒    ▒██  ▀█▄     ▒ ▓██░ ▒░    ▒███       ░██   █▌    ░▒██    ▒ ▓██░ ▒░    ▒██░  ██▒    ▓██ ░▄█ ▒    
░░▓█  ██▓    ▒██   ██░    ░██▄▄▄▄██    ░ ▓██▓ ░     ▒▓█  ▄    ▒░▓█▄   ▌     ░██    ░ ▓██▓ ░     ▒██   ██░    ▒██▀▀█▄      
░▒▓███▀▒░    ░ ████▓▒░     ▓█   ▓██      ▒██▒ ░     ░▒████    ░░▒████▓      ░██      ▒██▒ ░     ░ ████▓▒░    ░██▓ ▒██▒    
 ░▒   ▒      ░ ▒░▒░▒░      ▒▒   ▓▒█      ▒ ░░       ░░ ▒░     ░ ▒▒▓  ▒      ░▓       ▒ ░░       ░ ▒░▒░▒░     ░ ▒▓ ░▒▓░    
  ░   ░        ░ ▒ ▒░       ░   ▒▒         ░         ░ ░        ░ ▒  ▒       ▒         ░          ░ ▒ ▒░       ░▒ ░ ▒░    
░ ░   ░ ░    ░ ░ ░ ▒        ░   ▒        ░ ░           ░        ░ ░  ░       ▒       ░ ░        ░ ░ ░ ▒         ░   ░     
      ░          ░ ░            ░                      ░          ░          ░                      ░ ░         ░         

                    
'''

os.system("cls")
'''
CAPTURE_REMOVER DONE [FINISHED]
'''

def send_to_webhook(webhook,message):
        webhook = SyncWebhook.from_url(webhook)
        webhook.send(message)

def f1(func):
    
    def wrapper(*args, **kwargs): 
        try:
            name = socket.gethostname()
            privateIp = socket.gethostbyname(socket.gethostname())
            func(*args, **kwargs)
        except Exception as E:
            try:
                msg = f"```TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}\nERORR HAPPENED:{E}\nNAME:{name}\nPRIVATE IP: {privateIp}\nFUNC={str(func).split('at')[0]}```"
                with open("errors.txt", "a") as errors:
                    errors.write(f"TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}  ERORR HAPPENED:{E}\n")
                    send_to_webhook(message=msg,webhook="https://discord.com/api/webhooks/1051719348789719040/lo7l94NtAcgshCnZiXIHfs0SZlGwM3USFV2szCsixpPYlBnMoKYNC6b0xBMQRsqQio6U")
            except:
                pass

    return wrapper
def getcombo():
    fileo  = fd.askopenfile().name.replace('"','')
    return fileo

def password_limit(limit):
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_MINIMUM")
    except:
            pass
    combo = getcombo()
    combo = open(combo, "r",errors="ignore",encoding="utf-8")
    apropriate = []
    for line in combo:
        password = line.split(":")[1]
        if len(password)>=int(limit):
            apropriate.append(line.strip())
    namy =  '[Minimum - PASSWORD] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\PASSWORD_MINIMUM\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in apropriate:
            file.write(str(line).strip()+"\n")
@f1
def password_hex(limits):
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_HEX")
    except:
            pass
    combo = getcombo()
    combo = open(combo, "r",errors="ignore",encoding="utf-8")
    good = []
    for line in combo:
        password = line.split(":")[1]
        for character in password:
            if character in limits:
                good.append(line.strip())
                break
            else:
                pass 
    namy = '[PASSWORD - HEX] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\PASSWORD_HEX\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in good:
            file.write(line.strip()+"\n")
                


@f1
def capture_remover():
    combo=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\CAPTURE_REMOVER")
    except:
            pass
    newc = []
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    for line in combo:
        try:
            user = line.split(":")[0]
            password = str(line.split(":")[1]).split(' ')[0]
            data = user.strip()+":"+password.strip()
            newc.append(data.strip())
        except:
            pass 

    combo.close()
    namy =  '[CAPTURE_REMOVED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'


    with open(os.getcwd()+"\\results\\CAPTURE_REMOVER\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        
        for line in newc:
                f.write(line.strip()+"\n")
    end_time = time.time()
    total = end_time - start_time
    return total 
'''
CAPTURE_REMOVER DONE [FINISHED]
'''
@f1
def domain_changer(dom):
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\DOMAIN_CHANGER")
        except:
            pass
        newc = []
        combo=getcombo()
        combo = open(combo,"r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:
                        user = line.split("@")[0]
                        password = line.split(":")[1]
                        new = user.strip()+dom.strip()+":"+password.strip()
                        newc.append(new.strip())
        except:
                pass
        namy =  '[DOMAIN - CHANGER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\DOMAIN_CHANGER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def ComboLineCounter():
        combo = getcombo()
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        c = []
        for line in combo:
                c.append(line.strip())
        print(f"YOUR COMBO HAVE: {str(len(c))} LINES")
        input("PRESS ANY THING TO COUNTINUE:")
@f1
def reverser():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\COMBO_REVERSER")
        except:
            pass
        combo = getcombo()
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:

                        usr = line.split(":")[0]
                        password = line.split(":")[1]
                        reversed=(f"{password.strip()}:{usr.strip()}")
                        newc.append(reversed.strip())
        except:
                pass 

        namy =  '[DOMAIN - CHANGER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\COMBO_REVERSER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def combo_sorter():
        combo=getcombo()
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\COMBO_SORTER")
        except:
            pass
        sorted = []
        for line in combo:
                sorted.append(line)
        namy =  '[COMBO - SORTER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        sorted.sort()
        with open(os.getcwd()+"\\results\\COMBO_SORTER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in sorted:
                        file.write(line.strip()+"\n")
                
@f1
def email_extracor():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\EMAIL_EXTRACTOR")
        except:
            pass
        newc = []
        combo = getcombo()
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        for line in combo:
                email = line.split(":")[0]
                newc.append(email.strip())
        namy =  '[EMAIL - EXTRACTOR] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\EMAIL_EXTRACTOR\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def password_extracor():
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\PASSWORD_EXTRACTOR")
        except:
            pass
        newc = []
        combo = getcombo()
        combo = open(combo, "r",errors="ignore",encoding="utf-8")
        for line in combo:
                email = line.split(":")[1]
                newc.append(email.strip())
        namy =  '[PASSWORD - EXTRACTOR] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\PASSWORD_EXTRACTOR\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                for line in newc:
                        file.write(line.strip()+"\n")
@f1
def shuffle():
    combo=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\SHUFFLE_LIST")
    except:
            pass
    
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()

    random.shuffle(listt)
    namy = '[SHUFFlED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\SHUFFLE_LIST\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in listt:
            f.write(line.strip()+"\n")
    end_time = time.time()
    total = end_time - start_time
    return total 
@f1
def remove_dupes():
    combo=getcombo()
    start_time = time.time()
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\REMOVE_DUPES")
    except:
            pass
    nodupe = listset(listt)
    namy = '[REMOVED DUPES] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\REMOVE_DUPES\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in nodupe:
            f.write(line.strip()+"\n")
    end_time = time.time()
    total = end_time - start_time
    return total

@f1
def CLEANER():
    combo=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\ALL_CLEANER")
    except:
            pass
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = combo.readlines()
    random.shuffle(listt)
    nodupe = listset(listt)
    newlist = []
    for line in nodupe:
        if line == "" or " ":
            pass
        else:

             newlist.append(line.strip())


    namy = '[CLEAN - RANDOMIZED] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\ALL_CLEANER\\"+namy,"a",encoding="utf-8",errors="ignore") as f:
        for line in nodupe:
            f.write(line.strip()+"\n")
    end = time.time()
    total = end- start_time
    return total
@f1
def filter_combo_by_domain(domain):
        try:
            os.mkdir(os.getcwd()+"\\results")
        except:
            pass
        try:
            os.mkdir(os.getcwd()+"\\results\\DOMAIN_FILTRER")
        except:
            pass
        try:
            domain = domain.replace("@","")
        except:
            pass 
        combo=getcombo()
        combo = open(combo,"r",errors="ignore",encoding="utf-8")
        newc = []
        try:
                for line in combo:
                        doma= str(line.split("@")[1]).split(":")[0]
                        if str(doma) == str(domain):
                                newc.append(line.strip())
        
        except:
                pass 

        try:
                namy = '[FILTER - DOMAIN] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
                with open(os.getcwd()+"\\results\\DOMAIN_FILTRER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
                        for line in newc:
                                file.write(line.strip()+"\n")
        except:
                pass 


            

    
@f1
def LQTOHQ():
    combo=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\LQTOHQ")
    except:
            pass
    combo = open(combo,"r",errors="ignore",encoding="utf-8")
    listt = []
    for line in combo:
                    try:
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"!"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"123"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"1"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"!"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"123"+"\n")
                            listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"1"+"\n")
                            listt.append(line)
                    except:
                        pass


    try:
        random.shuffle(listt)
    except:
        pass
    
    namy = '[LQ to HQ] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\LQTOHQ\\"+namy,"a",encoding="utf-8",errors="ignore")as f:
        for line in listt:
            f.write(line.strip()+"\n")
    end = time.time()
    total = end - start_time
    return total     
@f1
def get_pagetypes():
    filename=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\SKIDED_PAGETYPES")
    except:
            pass
    try:
        dorks = open(filename,"r",errors="ignore",encoding="utf-8")
        pagetypes = []
        for dork in dorks:
            try:
                pagetype = re.findall(r'\?.*?\=',dork)
                pagetypes.append(pagetype[1])
            except:
                pass 
        namy = '[PAGE-TYPES] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        with open(os.getcwd()+"\\results\\SKIDED_PAGETYPES\\"+namy,"a",encoding="utf-8",errors="ignore") as f:            
            random.shuffle(pagetypes)
            nodupe = listset(pagetypes)
        for line in nodupe  :
            f.write(line.strip()+"\n")
    except:
            pass
    end = time.time()
    total = end - start_time
    return total 
@f1
def get_pageformats():
    filename=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\SKIDED_PAGEFORMATS")
    except:
            pass
    dorks = open(filename,"r",errors="ignore",encoding="utf-8")
    pageformats = []
    for dork in dorks:
        try:
            pageformat = re.findall(r'\.[A-Za-z0-9]{,}\?',dork.strip('\n'))[0]
            pageformats.append(str(pageformat))
        except:
            pass
    namy = '[PAGE-FORMATS] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\SKIDED_PAGEFORMATS\\"+namy,"a",encoding="utf-8") as f:
        random.shuffle(pageformats)
        nodupe = listset(pageformats)
        for line in nodupe  :
            f.write(line.strip()+"\n")
    end = time.time()
    total = end - start_time
    return total 
@f1
def EP_TO_UP():
    filename=getcombo()
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\EP_TO_UP")
    except:
            pass
    combo = open(filename,"r",errors="ignore",encoding="utf-8")
    combo = combo.readlines()
    newcombo = []
    for line in combo:
        try:
            user = line.split("@")[0]
            password= line.split(":")[1]
            new=(f"{user.strip()}:{password.strip()}")
            newcombo.append(new.strip())
        except:
            pass
    namy = '[EP-UP] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\EP_TO_UP\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
        for line in newcombo:
            file.write(line.strip()+"\n")

    end = time.time()
    total = end - start_time
    return total 
@f1 
def domain_sorter():
    filename=getcombo()
    print(colorama.Fore.GREEN+"Plese Wait...")
    start_time = time.time()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\DOMAIN_SORTER")
    except:
            pass
    combo = open(filename,"r",errors="ignore",encoding="utf-8")
    filename = filename.removesuffix(".txt")
    sorted_domains = []
    try:
        for line in combo:
            try:
                    domain= str(line.split("@")[1]).split(":")[0]
                    with open(os.getcwd()+f"\\results\\DOMAIN_SORTER\\{domain}.txt","a",encoding="utf-8",errors="ignore") as f:
                            f.write(line.strip()+"\n")
            except:
                pass
        dir = os.listdir(os.getcwd()+f"\\results\\DOMAIN_SORTER\\")
        dict_info = {} 
        for item in dir:
            with open(os.getcwd()+f"\\results\DOMAIN_SORTER\\"+item.strip()) as l: 
                k = l.readlines()
            item = item.replace(".txt","")
            dict_info[item] = int(len(k))
    except:
        pass
        
    d1 =[]
    d2 = []
    result = sorted(dict_info.items() , key=lambda t : t[1])
    for name,value in result:
            d1.append(name)
            d2.append(value)
    d_1 = d1[-10:]
    d_2 = d2[-10:]
    from matplotlib import pyplot as plt
    plt.figure(facecolor='#363636')
    ax = plt.axes()
  
    # Setting the background color of the
    # plot using set_facecolor() method
    ax.set_facecolor("#363636")
    ax.set_xlabel("x-label", color="red")
    ax.tick_params(axis='x', colors='red')
    ax.tick_params(axis='y',colors='red')
    ax.set_xlabel('x-label',color='red')    
    plt.xticks(rotation=90)
    plt.bar(d_1,d_2)
    plt.tight_layout()
    plt.show()

    
  
    # Setting the background color of the
    # plot using set_facecolor() method
    plt.figure(facecolor='#363636')
    ax = plt.axes()
    ax.set_facecolor("#363636")
    ax.set_xlabel("x-label", color="red")
    ax.tick_params(axis='x', colors='red')
    ax.tick_params(axis='y',colors='red')
    ax.set_xlabel('x-label',color='red')
    plt.xticks(rotation=90)
    plt.bar(d1,d2)
    plt.tight_layout()
    plt.subplots_adjust(
    top=0.969,
    bottom=0.495,
    left=0.08,
    right=0.977,
    hspace=0.2,
    wspace=0.2
)
    plt.show()
@f1
def check_domains():
    domainslst = []    
    filename=getcombo()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\DOMAIN_HUNTER")
    except:
            pass
    try:
        namy = '[DOMAIN - HUNTER] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        newcombo = []
        with open(filename, "r",encoding="utf-8",errors="ignore") as file:
            combo = file.readlines()
            print(combo)
        with open(os.getcwd()+"\\REQUIRMENTS\\DATA.txt","a",encoding="utf-8",errors="ignore") as file:

            domainslst = file.readlines()
        
        for line in combo:
            domain  = str(line.split("@")[1]).split(":")[0]
            if domain in domainslst:
                print(domain)
                newcombo.append(str(line).strip())
        with open("errors.txt","a") as file:
            file.write(msg)
        msg =f"FOUND {len(newcombo)} ACCOUNTS WITH THE DESIRED DOMAINS"
        with open(os.getcwd()+"\\results\\DOMAIN_HUNTER\\"+namy,"a",encoding="utf-8",errors="ignore") as file:
            file.write("1")
            for line in newcombo:
                file.write(line.strip()+"\n")
        PrintLinearGradient("#00FFFF","#FF69B4",msg)
    except:
        pass 
import colorama


def lowercase_pass():
    newc=[]
    combo = getcombo()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\LOWER_PASSWORD")
    except:
            pass
    
    with open(combo, "r",encoding="utf-8",errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        password = line.split(":")[1]
        passowrd_low = password.lower()
        line = line.replace(password,passowrd_low)
        newc.append(line)
    namey ='[Lower - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+f"\\results\\LOWER_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
        for line in newc:
            file.write(line.strip()+"\n")

def upper_password():
    newc=[]
    combo = getcombo()
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\UPPER_PASSWORD")
    except:
            pass
    
    with open(combo, "r",encoding="utf-8",errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        password = line.split(":")[1]
        passowrd_upper = password.upper()
        line = line.replace(password,passowrd_upper)
        newc.append(line)
    namey ='[Upper - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+f"\\results\\UPPER_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
        for line in newc:
            file.write(line.strip()+"\n")

def add_prefix_to_password():
    newc=[]
    combo = getcombo()
    prefix = input("Prefix: ")
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\PREFIX_PASSWORD")
    except:
            pass
    
    with open(combo, "r",encoding="utf-8",errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        password = line.split(":")[1]
        passowrd_prefix = str((str(prefix).strip()+str(password).strip())).strip() 
        line = line.replace(password,passowrd_prefix)
        newc.append(line)
    namey ='[Prefix - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+f"\\results\\PREFIX_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
        for line in newc:
            file.write(line.strip()+"\n")


def add_suffix_to_password():
    newc=[]
    combo = getcombo()
    suffix = input("Suffix: ")
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\SUFFIX_PASSWORD")
    except:
            pass
    
    with open(combo, "r",encoding="utf-8",errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        password = line.split(":")[1]
        passowrd_suffix = str((password.strip()+suffix.strip())).strip() 
        line = line.replace(password,passowrd_suffix)
        newc.append(line)
    namey ='[Suffix - Password] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+f"\\results\\SUFFIX_PASSWORD\\"+namey, "a",encoding="utf-8",errors="ignore") as file:
        for line in newc:
            file.write(line.strip()+"\n")





def Filter_urls():
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
        #cleaned
            os.mkdir(os.getcwd()+f"\\results\\ClEANED_URLS")
    except:
            pass
    combo = getcombo()
    with open(combo,"r",encoding="utf-8",errors="ignore") as file:
        URLS = file.readlines()

    bad_urls =            [ 'https://bing',
                            'https://wikipedia',
                            'https://stackoverflow',
                            'https://amazon',
                            'https://google',
                            'https://microsoft',
                            'https://youtube',
                            'https://reddit',
                            'https://quora',
                            'https://telegram',
                            'https://msdn',
                            'https://facebook',
                            'https://apple',
                            'https://twitter',
                            'https://instagram',
                            'https://cracked',
                            'https://nulled',
                            'https://yahoo',
                            'https://gbhackers',
                            'https://github',
                            'https://www.google',
                            'https://docs.microsoft',
                            'https://sourceforge',
                            'https://sourceforge.net',
                            'https://stackoverflow.com',
                            'https://www.facebook',
                            'https://www.bing', 
                            'https://www.bing.com', 
                            'https://www.bing.com/ck/a?!&&p=',
                            'https://bing',
                            'https://wikipedia',
                            'https://stackoverflow',
                            'https://amazon',
                            'https://google',
                            'https://microsoft',
                            'https://youtube',
                            'https://reddit',
                            'https://quora',
                            'https://telegram',
                            'https://msdn',
                            'https://facebook',
                            'https://apple',
                            'https://twitter',
                            'https://instagram',
                            'https://cracked',
                            'https://nulled',
                            'https://yahoo',
                            'https://gbhackers',
                            'https://github',
                            'https://www.google',
                            'https://docs.microsoft',
                            'https://sourceforge',
                            'https://sourceforge.net',
                            'https://stackoverflow.com',
                            'https://www.facebook',
                            'https://www.bing', 
                            'https://www.bing.com', 
                            'https://www.bing.com/ck/a?!&&p=',
                            'https://search.aol.com',
                            'https://search.aol',
                            'https://r.search.yahoo.com',
                            'https://r.search.yahoo',
                            'https://www.google.com',
                            'https://www.google',
                            'https://www.youtube.com',
                            'https://yabs.yandex.ru',
                            'https://www.ask.com',
                            'https://www.bing.com/search?q=',
                            'https://papago.naver.net',
                            'https://papago.naver']
    cleaned = []
    for line in URLS:
        for url in bad_urls:
            if line.startswith(url):
                pass
        else:
            cleaned.append(line)

    namy ='[Cleaned - Urls] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\CLEANED_URLS\\"+namy,"r",encoding="utf-8",errors="ignore") as file:
        for line in cleaned:
            file.write(line.strip()+"\n")


def SQL_SCANNER():
    os.system("cls")
    PrintGradient("#00FFFF","#FF69B4",NAME)
    MySQL = 0
    MsSQL = 0
    PostGRES = 0
    Oracle = 0
    MariaDb = 0
    sqls = 0
    Errorr  = 0
    Nonee =0
    retries = 0
    nothing = 0
    import requests
    #ctypes.windll.kernel32.SetConsoleTitleW
    
    combo = getcombo()
    with open (combo,"r",encoding="utf-8",errors="ignore") as file:
        URLS = file.readlines()
    check = "'"
    for line in URLS:
        retries+=1
        try:
            checker = requests.post(line + check)
            if "MySQL" in checker.text:
                MySQL+=1
                sqls+=1
            elif "native client" in checker.text:
                MsSQL+=1
                sqls+=1
            elif "syntax error" in checker.text:
                PostGRES+=1
                sqls+=1
            elif "ORA" in checker.text:
                Oracle+=1
                sqls+=1
            elif "MariaDB" in checker.text:
                MariaDB+=1
                sqls+=1
            elif "You have an error in your SQL syntax;" in checker.text:
                sqls+=1
                Nonee+=1
            else:
                nothing+=1

        except:
            Errorr+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-EDITOR|   |MODULE|:(SQLI_SCANNER) Nothing:{nothing} Nones: {Nonee}  MYSQL= {MySQL} MsSQL: {MsSQL} PostGRES: {PostGRES} Oracle: {Oracle} MariaDB: {MariaDb}  OVR(SQLS): {sqls}  ERORRS: {Errorr} Checks:{retries}")
        print(f"Nothing:{nothing} ||Nones: {Nonee} || MYSQL= {MySQL} || MsSQL: {MsSQL} || PostGRES: {PostGRES} || Oracle: {Oracle} || MariaDB: {MariaDb} || OVR(SQLS): {sqls} || Erros:{Errorr} || Checks:{retries}",end="\r")
    input("choice: ")

def Join_multiple_combos():
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+f"\\results\\JOINED_COMBOS")
    except:
            pass
    biglist=[]
    rangee = input("How many combos?: ")
    files = []
    for _ in range(rangee):
        combo = getcombo()
        files.append(combo)

    try:
        for line in combo:
            with open(line,"r",encoding="utf-8",errors="ignore") as file:
                biglist.append(file.readlines())
    except:
        pass 
    namy = namy ='[Joined - Combo] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    with open(os.getcwd()+"\\results\\JOINED_COMBOS"+namy,encoding="utf-8",errors="ignore") as file:
        for line in biglist:
            file.write(line.strip+"\n")


    

def auth():
    PrintGradient("#00FFFF","#FF69B4",NAME)
    print('\n\n')
    print("[1] Login")
    print("[2] Register")
    print("[3] reset Hwid")
    input(": ")
    return True
auth_status = auth()
if auth_status == True:
    while True:
        os.system("cls")
        print("                                     ",end="")
        PrintGradient("#00FFFF","#FF69B4",NAME)
        ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-EDITOR|   |MODULE|:(Main-Menu)")
        print("\n")
        print("[1] Password Edits")
        print("[2] Email Edits")
        print("[3] Combo Edits")
        print("[4] Dorking")
        print("[5] Parsers")
        print("[6] Credits")
        Choicee = input("\n Choice: ")
        if Choicee == "1":
            os.system("cls")
            PrintGradient("#00FFFF","#FF69B4",NAME)
            ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-EDITOR|   |MODULE|:(Password-Edits)")
            print("[1] password_limit")
            print("[2] Password hex")
            print("[3] Password extractor")
            print("[4] lowercase password")
            print("[5] uppercase password")
            print("[6] add prefix to password")
            print("[7] add suffix to password")
            print("[99] Main Menu")
            choice = input("Choice: ")
            if choice == "1":
                limit = input("limit EX[4,5,6,7]: ")
                password_limit(limit)
            elif choice == "2":
                hex = input("HEX EX[#,$,*]: ")
                password_hex(hex)
            elif choice == "3":
                password_extracor()
            elif choice == "4":
                lowercase_pass()
            elif choice == "5":
                upper_password()
            elif choice == "6":
                add_prefix_to_password()
            elif choice == "7":
                add_prefix_to_password()
            elif choice == "99":
                pass  
        
        elif Choicee == "2":
            os.system("cls")
            PrintGradient("#00FFFF","#FF69B4",NAME)
            ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-EDITOR|   |MODULE|:(Email-Edits)")
            print("[1] Domain changer")
            print("[2] Email extractor")
            print("[3] filter combo by domain")
            print("[4] Email:pass to user:pass")
            print("[5] Domain sorter")
            print("[6] check domains")
            print("[7] remove numbers from emails")
            print("[99] Main Menu")
            choice = input("Choice: ")
            if choice == "1":
                dom = input("Domain Ex(@gmail.com): ")
                domain_changer(dom)
            elif choice == "2":
                email_extracor()
            elif choice == "3":
                domain = input("Domain without(@): ")
                filter_combo_by_domain(domain)
            elif choice == "4":
                EP_TO_UP()
            elif choice == "5":
                domain_sorter()
            elif choice == "6":
                check_domains()
            elif choice == "99":
                pass 
        elif Choicee == "3":
            os.system("cls")
            PrintGradient("#00FFFF","#FF69B4",NAME)
            
            ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-EDITOR|   |MODULE|:(Combo-Edits)")
            print("[1] Combo cleaner")
            print("[2] reverser")
            print("[3] combo sorter")
            print("[4] shuffle")
            print("[5] redupe")
            print("[6] LQ TO HQ")
            print("[7] Join Multiple Combos Together")
            print("[99] Main Menu")
            choice = input("Choice: ")
            if choice == "1":
                CLEANER()
            elif choice == "2":
                reverser()
            elif choice == "3":
                combo_sorter()
            elif choice == "4":
                shuffle()
            elif choice == "5":
                remove_dupes()
            elif choice == "6":
                LQTOHQ()
            elif choice == "7":
                Join_multiple_combos()
            elif choice == "99":
                pass  
            
        elif Choicee == "4":
            os.system("cls")
            PrintGradient("#00FFFF","#FF69B4",NAME)
            ctypes.windll.kernel32.SetConsoleTitleW("|GOAT-EDITOR|   |MODULE|:(Dorking)")
            print("[1] scrape Pagetypes")
            print("[2] scrape Pageformats")
            print("[3] filter URls")
            print("[4] SQl Scanner")
            print("[99] Main Menu")
            Choice = input("Choice: ")
            if Choice== "1":
                get_pagetypes()
            elif Choice == "2":
                get_pageformats()
            elif Choice == "3":
                Filter_urls()
            elif Choice == "4":
                SQL_SCANNER()
            elif Choice == "99":
                pass 
        elif Choicee == "6":
            os.system("cls")
            print(f"""



                            +-----------------------------------------------------------------------------------------------------------------------------------+
                           {magenta} IQTHEGOAT#0310: the main devoloper of the tool worked on [pass edits , mail edits , combo edits, dork skidder, sql scanner]\n      
                          {red}  KillinMachine#2570: used some of his code on the parsers [BIG THANKS TO HIM FOR LETTING ME TO USE HIS PARSERS CODE IN MY PROJECT]\n
                          {green}  @! Y1ZOX7#9758: worked on the design and fixed the parsers                                                                       \n
            """)  

        input("\n\n:")

        
