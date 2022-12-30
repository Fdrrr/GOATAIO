from GradientGen import PrintGradient, PrintLinearGradient
import random
from listset import listset
import datetime
import os
import time
import requests
import json as js  
import re 
import mysql.connector
import hashlib
import platform
import os
import socket
from discord import SyncWebhook
from colorama import Fore 
import tkinter.filedialog as fd
import ctypes
import sys


website = "https://goatauth.deta.dev/"


bl, ree, lr, wh, gr, cy, lb, res, ma, lm, lc, ye = Fore.BLUE, Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.YELLOW



NAME = '''
     ██████╗      ██████╗      █████╗     ████████╗         █████╗     ██╗     ██████╗ 
    ██╔════╝     ██╔═══██╗    ██╔══██╗    ╚══██╔══╝        ██╔══██╗    ██║    ██╔═══██╗
    ██║  ███╗    ██║   ██║    ███████║       ██║           ███████║    ██║    ██║   ██║
    ██║   ██║    ██║   ██║    ██╔══██║       ██║           ██╔══██║    ██║    ██║   ██║
    ╚██████╔╝    ╚██████╔╝    ██║  ██║       ██║           ██║  ██║    ██║    ╚██████╔╝
     ╚═════╝      ╚═════╝     ╚═╝  ╚═╝       ╚═╝           ╚═╝  ╚═╝    ╚═╝     ╚═════╝ '''

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
@f1
def getcombo():
    fileo  = fd.askopenfile().name.replace('"','')
    return fileo

@f1
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

@f1
def CLEANER():
    combo=getcombo()
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
@f1
def get_pagetypes():
    filename=getcombo()
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
@f1
def get_pageformats():
    filename=getcombo()
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

def EP_TO_UP():
    filename=getcombo()
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

@f1
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

@f1
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
@f1
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

@f1
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




@f1
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



@f1
def SQL_SCANNER():
    start = time.time()
    os.system("cls")
    PrintGradient("#00FFFF","#FF69B4",NAME)
    cpm = "calculating"
    TP = 0 
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
            if "MySQL" or "mysql" in checker.text:
                MySQL+=1
                sqls+=1
            elif "native client" or "Native Client" in checker.text:
                MsSQL+=1
                sqls+=1
            elif "syntax error" or "Syntax Error" in checker.text:
                PostGRES+=1
                sqls+=1
            elif "ORA" or "ora" in checker.text:
                Oracle+=1
                sqls+=1
            elif "MariaDB" or "mariadb" in checker.text:
                MariaDB+=1
                sqls+=1
            elif "You have an error in your SQL syntax;" in checker.text:
                sqls+=1
                Nonee+=1
            else:
                nothing+=1

        except:
            Errorr+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"|GOAT-EDITOR|   |MODULE|:(SQLI_SCANNER) RESULTS=    Nothing:{nothing}   Nones: {Nonee}     MYSQL= {MySQL}   MsSQL: {MsSQL}   PostGRES: {PostGRES}   Oracle: {Oracle}   MariaDB: {MariaDb}    OVR(SQLS): {sqls}    ERORRS: {Errorr}   Checks:{retries}   TimePassed:{TP}")
        #print(f"\rNothing:{nothing} ||Nones: {Nonee} || MYSQL= {MySQL} || MsSQL: {MsSQL} || PostGRES: {PostGRES} || Oracle: {Oracle} || MariaDB: {MariaDb} || OVR(SQLS): {sqls} || Erros:{Errorr} || Checks:{retries}\r",end="\r")
        os.system("cls")
        end = time.time()
        total = end-start
        TP = round(total)
        cpm = int(round((retries/TP)*60))
        PrintGradient("#00FFFF","#FF69B4",NAME)
        print(f""" 
{lm}                                                  Checks:{retries}
{ma}                                        [{res}MySql:             {MySQL}{ma}   ]
{lb}                                        [                       ]
{bl}                                        [{res}MsSql:             {MsSQL}{bl}   ]
{cy}                                        [{res}PostGres:          {PostGRES}{cy}   ]
{lr}                                        [                       ]
{ree}                                        [{res}Oracle:            {Oracle} {ree}  ]
{gr}                                        [                       ]  
{ye}                                        [{res}MariaDb:           {MariaDb} {ye}  ]
                                                                
                                                        (Stats)
{lm}                                               [Checks:    ({retries})]
{ma}                                               [overall_sqls: ({sqls})]
{bl}                                               [Cpm:           ({cpm})]
{cy}                                               [Errors:     ({Errorr})]
{lr}                                               [noDbs:       ({Nonee})]
{ree}                                              [nothings:  ({nothing})]

""")
    input("choice: ")

def get_hwid():
    # Get the CPU name and version
    cpu_name = platform.processor()
    cpu_version = platform.machine()

    # Get the OS name and version
    os_name = platform.system()
    os_version = platform.release()

    # Concatenate the CPU and OS information into a single string
    hwid = f"{cpu_name} ({cpu_version}), {os_name} {os_version}"

    # Return the HWID
    return hwid


            
@f1
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



@f1
def get_pagetypes_from_urls():
    try:
            os.mkdir(os.getcwd()+"\\results")
    except:
            pass
    try:
            os.mkdir(os.getcwd()+"\\results\\PGT_FROM_URLS")
    except:
            pass
    namy = '[Pagetypes-Urls] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
    combo=getcombo()
    def redupe(litss):
        nodupe = listset(litss)
        return nodupe
    PageTypes = []
    with open(combo,"r",encoding = "utf-8",errors="ignore") as urls:
        for line in urls.readlines():
            string = line
            match = re.search(r"([^\/\.]*)\.([^\/.]*|[^\/.]*\.|gov\.rw|com\.au|add\.YourOwnDommainExtentionsHereIfItHasMultipleDots|co\.za|ca\.us)\/[^\.]*[^\/]*\.([a-zA-Z1-9]*)\?([^=&]*)=",string)

            if match:
                pre  = match.group()

                string = pre 

                match = re.search(r"\?(.*)", string)

                if match:
                    query_string = match.group(1)
                    if len(query_string) >2: 
                        PageTypes.append(query_string)
                    else:
                        pass 
    pagetypes = redupe(PageTypes)
    with open(os.getcwd()+"\\results\\PGT_FROM_URLS\\"+namy,'a',encoding='utf8',errors='ignore') as file:
        for line in pagetypes:
            file.write(str(line).strip()+"\n")


@f1
def HASH(password):
    """
    Hashes the given password using the SHA-256 algorithm   
    """
    hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
    return hashed_password

def login(username, password,HWID):
    req = requests.get(f"{website}"+f'login/{username}/{password}/{HWID}')
    data = req.json()
    status = data["status"]
    if status == True:
        return True
    else:
        return False


def register(email, username, password,key,HWID):
    req = requests.get(f"{website}"+f"register/{key}/{email}/{username}/{password}/{HWID}")
    data = req.json()
    status = data["status"]
    if status == True:
        return True
    else:
        return False

def RESETHWID(email, password, HWID):
    req = requests.get(f"{website}"+f"resethwid/{email}/{password}/{HWID}")
    data = req.json()
    status = data["status"]
    if status == True:
        return True
    else:
        return False
    

@f1
def auth():
    os.system("cls")
    PrintGradient("#00FFFF","#FF69B4",NAME)
    print('\n\n')
    print("[1] Login")
    print("[2] Register")
    print("[3] reset Hwid")
    resp = input(": ")
    if resp == "3":
        RESETHWID(email=input("email: "),password=input("password: "),HWID=get_hwid())
    if resp == "2":
        register(key=input("REGISTER-KEY: "),email=input("email: "),username=input("username: "),password=input("password: "),HWID=get_hwid())
    if resp == "1":
        response = login(username=input("username: "),password=input("password: "),HWID=get_hwid())
        print(response)
        time.sleep(2)
        if response == True:
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
                    print("[5] Get Parameters from Url")
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
                    elif Choice == "5":
                        get_pagetypes_from_urls()
                    elif Choice == "99":
                        pass 
                elif Choicee == "6":
                    os.system("cls")
                    print(f"""
                                    +-----------------------------------------------------------------------------------------------------------------------------------+
                                {ma} IQTHEGOAT#0310: the main devoloper of the tool worked on [pass edits , mail edits , combo edits, dork skidder, sql scanner]\n      
                                {ree}  KillinMachine#2570: used some of his code on the parsers [BIG THANKS TO HIM FOR LETTING ME TO USE HIS PARSERS CODE IN MY PROJECT]\n
                                {gr}  @! Y1ZOX7#9758: worked on the design and fixed the parsers                                                                       \n
                    """)  

                input("\n\n:")
        else:
            print("[!] Invalid Choice")
            print("[!] Please try again")
            time.sleep(0.5)
                    
while True:
    auth()  