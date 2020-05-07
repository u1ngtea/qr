# -*- coding: utf-8 -*-
# Support <-> IKAPUJI TEAM BOTs ===>##
from linepy import *
from time import sleep
import argparse, ast, asyncio, codecs, json, os, pytz, shutil, sys, time, urllib.parse, re, null, subprocess, random, requests, pafy, traceback, humanize, threading, base64, livejson, multiprocessing
from datetime import timedelta, date
from datetime import datetime
from Naked.toolshed.shell import execute_js
from threading import Thread
from multiprocessing import *
from multiprocessing import Pool, Process, Manager, Array, Value

#==============[ LOGIN QR ]==============#
try:
    header = "ios_ipad"
    auth = "Q541hNgFX1AM"
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+auth).text)
    print("QR Link: {}".format(result["result"]["qr_link"]))
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
    if result["status"] != 200:
      raise Exception("Timeout!!!")
    myika = LINE(result["result"]["token"],appName="IOSIPAD\t10.1.1\tiPhone 8\t11.2.5")
    print("Login Sukses")
except:pass
#==============[ token 2 ]==============#
print("╭────────────────────╮")
print("│")
print("│• Status Login: Sukses")
print("│• Author: U1Ng")
print("│• Team: IKAPUJIBOTS TEAM")
print("│• Thanks to ALLAH S.W.T")
print("│")
print("╰──|[ U1Ng BOT LOGIN ]|──╯")
#==============================================================================#
oepoll = OEPoll(myika)
mid = myika.getProfile().mid
Bots=[mid]
Puji = ["u09ac0e36c15ce4a41047614ac728d132"]
Uing = ["u09ac0e36c15ce4a41047614ac728d132"]
Ikapuji = Bots+Puji+Uing
#==============[ Main Json ]==============#
settings = {
    "autoRead": False,
    "autoBlock":False,
    "autoBlockMessage": "maaf ku block ",
    "keyCmd": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCmd"]):
        cmd = pesan.replace(settings["keyCmd"],"")
    else:
        cmd = "command"
    return cmd

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoBlock"] == True:
                myika.blockContact(op.param1)
                myika.sendMention(op.param1, settings["autoBlockMessage"][op.param1])

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      myika.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                        cmd = command(text)
                        if cmd == "bot:on":
                            if msg._from in Puji:
                                myika.sendMessage(msg.to, "Self bot mode on")

                        elif cmd == "sbot:off":
                            if msg._from in Puji:
                                myika.sendMessage(msg.to, "Self bot mode off")

    except Exception as error:
        print (error)

while True:
    try:
        ops=oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
