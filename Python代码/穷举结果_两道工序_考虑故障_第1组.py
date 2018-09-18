from CNC import CNC
from RGV import RGV
import random

time = 0
goodsnum = 0
relativeloca = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
relativeloca2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
rgv = RGV([0, 20, 33, 46], 28, 31, 25, 1)
workingtime = [0, 400, 378]
cnclist = []
fcnc = [0]
scnc = [0]
sequenceall = [0]
sequence1 = [0]
sequence2 = [0]
uptsequence1 = [0]
uptsequence2 = [0]
updowntsequence1 = [0]
updowntsequence2 = [0]
genome = [-1, 0, 1, 0, 1, 0, 1, 0, 1]

def express():
    global cnclist
    global fcnc
    global scnc
    for n in range(1, 8 + 1):
        if genome[n] == 1:
            cnclist[n].whethersec = True
            scnc.append(cnclist[n].num)
        else:
            fcnc.append(cnclist[n].num)


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
    if cnclist[choice].whethersec == False:
        sequence1.append(choice)
        uptsequence1.append(time)
        addtime(rgv.oddchangetime)
        whetherbroken(choice)
    elif cnclist[choice].whethersec == True and rgv.haveone == True:
        sequence2.append(choice)
        uptsequence2.append(time)
        rgv.putone()
        addtime(rgv.oddchangetime)
        whetherbroken(choice)
    else:
        addtime(1)


def odddownup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    if cnclist[choice].whethersec == False:
        sequence1.append(choice)
        uptsequence1.append(time)
        updowntsequence1.append(time)
        rgv.catchone()
        addtime(rgv.oddchangetime)
        whetherbroken(choice)
        cnclist[choice].goodtrans()
        cnclist[choice].changestatu()
    elif cnclist[choice].whethersec == True and rgv.haveone == False:
        sequence2.append(choice)
        updowntsequence2.append(time)
        addtime(rgv.oddchangetime)
        addtime(rgv.washtime)
        goodsnum += 1
        print("2 end when rgv do not has 1")
    elif cnclist[choice].whethersec == True and rgv.haveone == True:
        sequence2.append(choice)
        uptsequence2.append(time)
        updowntsequence2.append(time)
        addtime(rgv.oddchangetime)
        whetherbroken(choice)
        addtime(rgv.washtime)
        goodsnum += 1
        rgv.putone()
        cnclist[choice].goodtrans()
        cnclist[choice].changestatu()
    rgvmovement(0)


def evenup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    cnclist[choice].changestatu()
    if cnclist[choice].whethersec == False:
        sequence1.append(choice)
        uptsequence1.append(time)
        addtime(rgv.evenchangetime)
        whetherbroken(choice)
    elif cnclist[choice].whethersec == True and rgv.haveone == True:
        sequence2.append(choice)
        uptsequence2.append(time)
        rgv.putone()
        addtime(rgv.evenchangetime)
        whetherbroken(choice)
    else:
        addtime(1)


def evendownup(choice):
    global time
    global rgv
    global cnclist
    global goodsnum
    cnclist[choice].goodtrans()
    if cnclist[choice].whethersec == False:
        sequence1.append(choice)
        uptsequence1.append(time)
        updowntsequence1.append(time)
        rgv.catchone()
        addtime(rgv.evenchangetime)
        whetherbroken(choice)
        cnclist[choice].goodtrans()
        cnclist[choice].changestatu()
    if cnclist[choice].whethersec == True and rgv.haveone == False:
        sequence2.append(choice)
        updowntsequence2.append(time)
        addtime(rgv.evenchangetime)
        addtime(rgv.washtime)
        goodsnum += 1
        print("2 end when rgv do not has 1")
    if cnclist[choice].whethersec == True and rgv.haveone == True:
        sequence2.append(choice)
        uptsequence2.append(time)
        updowntsequence2.append(time)
        addtime(rgv.evenchangetime)
        whetherbroken(choice)
        addtime(rgv.washtime)
        goodsnum += 1
        rgv.putone()
        cnclist[choice].goodtrans()
        cnclist[choice].changestatu()
    rgvmovement(0)


def initialize():
    for j in range(0, len(fcnc)):
        choice = cnclist[fcnc[j]].num
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


def twoprooperation():
    global time
    global goodsnum
    global rgv
    global cnclist
    if not rgv.haveone:
        for j in range(1, len(fcnc)):
            relativeloca[fcnc[j]] = abs(cnclist[fcnc[j]].num - rgv.location)
            if cnclist[fcnc[j]].having == True:
                relativeloca[fcnc[j]] += 1000
            if cnclist[fcnc[j]].working == True:
                relativeloca[fcnc[j]] += 1000
            if cnclist[fcnc[j]].broken == True:
                relativeloca[fcnc[j]] += 2000
        if min(relativeloca) >= 2000:
            for m in range(1, len(scnc)):
                relativeloca2[scnc[m]] = abs(cnclist[scnc[m]].num - rgv.location)
                if cnclist[scnc[m]].having == True:
                    relativeloca2[scnc[m]] += 1000
                if cnclist[scnc[m]].working == True:
                    relativeloca2[scnc[m]] += 1000
                if cnclist[scnc[m]].broken == True:
                    relativeloca[fcnc[m]] += 2000
                if cnclist[scnc[m]].having == False and cnclist[scnc[m]].working == False:
                    relativeloca2[scnc[m]] += 2000
            if min(relativeloca2) >= 2000:
                addtime(1)
            elif min(relativeloca2) >= 1000:
                choice = relativeloca2.index(min(relativeloca2))
                if relativeloca2[1] == 1006 and relativeloca2[2] == 1005:
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
    else:
        for j in range(1, len(scnc)):
            relativeloca[scnc[j]] = abs(cnclist[scnc[j]].num - rgv.location)
            if cnclist[scnc[j]].broken == True:
                relativeloca[scnc[j]] += 2000
            if cnclist[scnc[j]].having == True:
                relativeloca[scnc[j]] += 1000
            if cnclist[scnc[j]].working == True:
                relativeloca[scnc[j]] += 1000
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
    cnc = CNC(i, False, workingtime[1], workingtime[2])
    cnclist.append(cnc)
express()
while time <= (8 * 3600):
    twoprooperation()
    relativeloca = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    relativeloca2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
print("%-10s" % "CNC1", "%-10s" % "Uptime1", "%-10s" % "Downtime1",
      "%-10s" % "CNC2", "%-10s" % "Uptime2", "%-10s" % "Downtime2")
for i in range(1, len(updowntsequence2)):
    print("%-10d" % sequence1[i], "%-10d" % uptsequence1[i], "%-10d" % updowntsequence1[i],
          "%-10d" % sequence2[i], "%-10d" % uptsequence2[i], "%-10d" % updowntsequence2[i])
print("Total goods number: ", goodsnum)
print(genome)
