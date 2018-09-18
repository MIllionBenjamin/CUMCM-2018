from CNC import CNC
from RGV import RGV
import random

time = 0
goodsnum = 0
relativeloca = [10000, 0, 0, 0, 0, 0, 0, 0, 0]
rgv = RGV([0, 18, 32, 46], 27, 32, 25, 1)
workingtime = 545
cnclist = []
sequence = [0]
uptsequence = [0]
updowntsequence = [0]

def addtime(secs):
    global time
    global rgv
    global cnclist
    for s in range(1, secs + 1):
        time += 1
        for k in range(1, 8 + 1):
            cnclist[k].addmytime(1)
            if (cnclist[k].working == True
                and cnclist[k].broken == False
                and cnclist[k].shouldbro == True
                and cnclist[k].mytime == cnclist[k].brokenmoment):
                cnclist[k].brokenfix()
                print("broken now", k, time)

def rgvmovement(steps):
    global time
    global rgv
    global cnclist
    rgv.move(steps)
    addtime(rgv.movetime[abs(steps)])

def whetherbroken(cncnum):
    global cnclist
    random.seed()
    ran = random.randint(1, 100)
    if ran == 1:
        cnclist[cncnum].shouldbro = True
        cnclist[cncnum].brokentime = random.randint(600, 1200)
        cnclist[cncnum].brokenmoment = random.randint(1,560)

def oddup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    cnclist[choice].changestatu()
    sequence.append(choice)
    uptsequence.append(time)
    addtime(rgv.oddchangetime)
    whetherbroken(choice)



def odddownup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    sequence.append(choice)
    uptsequence.append(time)
    updowntsequence.append(time)
    addtime(rgv.oddchangetime)
    whetherbroken(choice)
    addtime(rgv.washtime)
    goodsnum += 1
    rgvmovement(0)
    cnclist[choice].goodtrans()
    cnclist[choice].changestatu()

def evenup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    cnclist[choice].changestatu()
    sequence.append(choice)
    uptsequence.append(time)
    addtime(rgv.evenchangetime)
    whetherbroken(choice)

def evendownup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    sequence.append(choice)
    uptsequence.append(time)
    updowntsequence.append(time)
    addtime(rgv.evenchangetime)
    whetherbroken(choice)
    addtime(rgv.washtime)
    goodsnum += 1
    rgvmovement(0)
    cnclist[choice].goodtrans()
    cnclist[choice].changestatu()

def opration():
    global time
    global goodsnum
    global rgv
    global cnclist
    global useamount
    for j in range(1, 8 + 1):
        relativeloca[j] = abs(cnclist[j].num - rgv.location)
        if cnclist[j].broken == True:
            relativeloca[j] += 2000
        if cnclist[j].having == True:
            relativeloca[j] += 1000
        if cnclist[j].working == True:
            relativeloca[j] += 1000
    if min(relativeloca) >= 2000:
        addtime(1)
    elif min(relativeloca) >= 1000:
        choice = relativeloca.index(min(relativeloca))
        if relativeloca[1] == 1006 and relativeloca[2] == 1005:
            choice = 1
        truediff = (choice - rgv.location)
        if choice % 2 == 0:
            if truediff == 1:
                rgvmovement(0)
                evendownup(choice)
            elif truediff == 3:
                rgvmovement(1)
                evendownup(choice)
            elif truediff == 5:
                rgvmovement(2)
                evendownup(choice)
            elif truediff == 7:
                rgvmovement(3)
                evendownup(choice)
            elif truediff == -1:
                rgvmovement(-1)
                evendownup(choice)
            elif truediff == -3:
                rgvmovement(-2)
                evendownup(choice)
            elif truediff == -5:
                rgvmovement(-3)
                evendownup(choice)
        else:
            if truediff == 0:
                rgvmovement(0)
                odddownup(choice)
            elif truediff == 2:
                rgvmovement(1)
                odddownup(choice)
            elif truediff == 4:
                rgvmovement(2)
                odddownup(choice)
            elif truediff == 6:
                rgvmovement(3)
                odddownup(choice)
            elif truediff == -2:
                rgvmovement(-1)
                odddownup(choice)
            elif truediff == -4:
                rgvmovement(-2)
                odddownup(choice)
            elif truediff == -6:
                rgvmovement(-3)
                odddownup(choice)
    else:
        choice = relativeloca.index(min(relativeloca))
        truediff = (choice - rgv.location)
        if choice % 2 == 0:
            if truediff == 1:
                rgvmovement(0)
                evenup(choice)
            elif truediff == 3:
                rgvmovement(1)
                evenup(choice)
            elif truediff == 5:
                rgvmovement(2)
                evenup(choice)
            elif truediff == 7:
                rgvmovement(3)
                evenup(choice)
            elif truediff == -1:
                rgvmovement(-1)
                evenup(choice)
            elif truediff == -3:
                rgvmovement(-2)
                evenup(choice)
            elif truediff == -5:
                rgvmovement(-3)
                evenup(choice)
        else:
            if truediff == 0:
                rgvmovement(0)
                oddup(choice)
            elif truediff == 2:
                rgvmovement(1)
                oddup(choice)
            elif truediff == 4:
                rgvmovement(2)
                oddup(choice)
            elif truediff == 6:
                rgvmovement(3)
                oddup(choice)
            elif truediff == -2:
                rgvmovement(-1)
                oddup(choice)
            elif truediff == -4:
                rgvmovement(-2)
                oddup(choice)
            elif truediff == -6:
                rgvmovement(-3)
                oddup(choice)


for i in range(0, 8 + 1):
    cnc = CNC(i, False, workingtime, 0)
    cnclist.append(cnc)
while time <= (8*3600):
    opration()
print("%-8s" % "CNC", "%-8s" % "Uptime", "%-8s" % "Downtime")
for i in range(1, len(updowntsequence)):
    print("%-8d" % sequence[i], "%-8d" % uptsequence[i], "%-8d" % updowntsequence[i])
print("Total goods number: ", goodsnum)









