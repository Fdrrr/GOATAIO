from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
from datetime import date, timedelta
import dateutil.relativedelta
import datetime
import hashlib,mysql.connector,platform

app = FastAPI()


Valu = []


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

def Register(key,email,username, password,HWID):
    try:
        """
        Inserts a new record into the Users table with the given username and password
        """
        if '@gmail' in email or "@yahoo" in email:
            # Hash the password for storage in the database
            hashed_password = HASH(password)
            hwid = HWID
            table = "regkeys"
            query = f"Select subtype from {table} WHERE regkey = %s"
            cr.execute(query, (key,))
            results = cr.fetchall()
            if len(results) == 0:
                return "WRONG KEY"
                
            else:
                sub = results[0][0]
                if sub == 'month':
                    now = datetime.datetime.now()
                    # Add 30 days to the current date
                    End_time = now + dateutil.relativedelta.relativedelta(days=31)
                elif sub == 'week':
                    now = datetime.datetime.now()
                    # Add 30 days to the current date
                    End_time = now + dateutil.relativedelta.relativedelta(days=8)
                elif sub == "lifetime":
                    now = datetime.datetime.now()
                    # Add 30 days to the current date
                    End_time = now + dateutil.relativedelta.relativedelta(days=5000)
                elif sub == "3d":
                    now = datetime.datetime.now()
                    End_time = now + dateutil.relativedelta.relativedelta(days=4)
                elif sub == "1d":
                    now = datetime.datetime.now()
                    End_time = now + dateutil.relativedelta.relativedelta(days=1)

                values = (username, hashed_password, str(hwid), str(email),str(End_time))
                query = f"INSERT INTO {Table} (username, password,HWID,email,End_date) VALUES (%s, %s, %s, %s, %s)"
                cr.execute(query, values)
                cnx.commit()
                key_column = "regkey"
                table = "regkeys"
                query = f"DELETE FROM {table} WHERE {key_column} = %s"
                cr.execute(query, (key,))
                cnx.commit()
                return True
        else:
            return "IT MUST BE A GMAIL OR YAHOO EMAIL"
    except Exception as e:
        return e 
    

import secrets
def gen_key():
    # Generate a 32-character random key
    key = secrets.token_urlsafe(32)
    return key

def subkey_To_db(subtype):
    key = gen_key()
    if key == None:
        return "ERORR"
    else:
        query = f"INSERT INTO regkeys (regkey,subtype) VALUES(%s,%s)"
        cr.execute(query,(key,subtype))
        cnx.commit()
        return key




def RESETHWID(email,password,HWID):
    try:
        hwid = HWID
        password = HASH(password)
        query = f"UPDATE {Table} set HWID = %s where email = %s and password = %s"
        cr.execute(query, (hwid,email, password))
        cnx.commit()
        return True
    except Exception as e:
        return e

def login(username, password,HWID):
    end_date = ""
    ret = []
    
    """
    Check if the given username and password match a record in the Users table
    """
    # Hash the password for comparison
    hashed_password = HASH(password)
    hwid = HWID
    cr.execute(f"SELECT * FROM {Table} WHERE username = %s AND password = %s and HWID = %s", (username, hashed_password,str(hwid)))
    results = cr.fetchall()#
    try:
        if results[0][1] == username and results[0][2] == hashed_password and results[0][3] == str(hwid):
            cr.execute(f"SELECT End_date FROM {Table} WHERE HWID = %s and username = %s",(str(hwid),username))
            results = cr.fetchall()
            if len(results) >0:
                end_date = results[0][0]
                ret.append(str(True))
                ret.append(str(end_date))
            return ret
        else:
            return str(False)
    except IndexError:
        return str(False)

HOST=""
USER=""
PASS=""
DATABASE=""
cnx = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASS,
    database=DATABASE
,
)
cr = cnx.cursor()


Table = "userdata"
def HASH(password):
    """
    Hashes the given password using the SHA-256 algorithm
    """
    hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
    return hashed_password



@app.get("/")
def home():
    return {}

@app.get("/register/{key}/{email}/{username}/{password}/{HWID}")
def register(key:str,email:str,username:str,password:str,HWID:str):
    resp = Register(key=key,email=email, username=username, password=password,HWID=HWID)
    return {"status":resp}

@app.get("/login/{username}/{password}/{HWID}")
def Login(username:str,password:str,HWID:str):
    resp = login(username=username,password=password,HWID=HWID)
    return {"status":str(resp[0]),"end_date":str(resp[1])}

@app.get("/resethwid/{email}/{password}/{HWID}")
def Login(email:str,password:str,HWID:str):
    resp = RESETHWID(email=email,password=password,HWID=HWID)
    return {"status":resp}

@app.get("/genkey/{key}/{type_sub}") 
def gen(key:str,type_sub:str):
    if key == "2z0d6c4GUs1aqnplLBVAHMg9k2uwfGvCATRyWBtY1pXaBrrFjJLkdb6ogdJZz27dVl79D3oRWMmeZI2uRmm6rRBJ3JtBvsD3bSmgb5Z7ZXW6NX8D2dta97qsGiSFyTwJN8OPfopIryfhBPjk1m0jldE3mTkZ4fWRTBX0f6Qp3VxICULx9iTJeXer52g8sg2S2K9hrEcH51QnCfMOqUQ7UofsCXU89tixYnL5lr0l8RvTXrCf3N2DUpamLaXX1GIf":
        key = subkey_To_db(type_sub)
        return{"GENERATED":key}



