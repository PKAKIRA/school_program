import sys
import datetime
from time import sleep
import os

def shutdown():
    os.system("shutdown /p /f")          #shutdown

def network_off():                   #network 연결 끊기
    os.system("ipconfig/release")

def network_on():                    #network 연결 
    os.system("ipconfig/renew")

def clock_1():                       #월요일 아침 
    if(h == 8):
        if(m <= 58):
            shutdown()
    if(h == 9):
        if(m == 50):
            network_off()
            sleep(600)
    if(h == 11):
        if(m == 15):
            network_off()
            sleep(1200)
            network_on()

def clock_2():                       #화, 수 아침
    if(h == 11):
        if(m == 50):
            network_off()
            sleep(600)
            network_on()

def clock_3():                        #목, 금 아침
    if(h == 11):
        if(m == 25):
            network_off()
            sleep(600)
            network_on()

def lunch():                            #모든 요일의 점심 시간
    if(h == 12):
        if(m <= 50):
            shutdown()
    if(h == 13):
        if(m <= 48):
            shutdown()
def eta():                              #모든 요일의 오후 시간 + 청소시간까지   + 야자
    if(m%40 == 0):
        network_off()
        sleep(600)
        network_on()
    if(h == 16):
        if(m >= 40 and m <= 58):
            shutdown()

def etn():                            #모든 요일의 8, 9교시 + 저녁시간
    if(h == 17):
        if(m == 50):
            network_off()
            sleep(600)
            network_on()
    if(h == 18):
        if(m >= 50):
            shutdown()
    if(h == 19):
        if(m <= 48):
            shutdown()
def ns():      #마무리로 컴퓨터 전원 꺼짐
    if(h == 21):
        if(m <= 40):
            shutdown()

def everytime_MN():                   #월요일을 제외하고, 나머지 요일의 아침시간 
    if(h == 8):
        if(m <= 33):
            shutdown()
    if(h == 9):
        if(m ==25):
            network_off()
            sleep(600)
            network_on()
    if(h == 10):
        if(m == 25):
            network_off()
            sleep(600)
            network_on()

def at():
    lunch()
    eta()
    etn()
    ns()

while True:
    dn = datetime.datetime.now()      
    h = dn.hour                      
    m = dn.minute                    
    week = dn.weekday()
    if(week == 0):
        clock_1()
        at()
    if(week == 1 or week == 2):
        clock_2()
        at()
    if(week == 3 or week == 4):
        clock_3()
        at()