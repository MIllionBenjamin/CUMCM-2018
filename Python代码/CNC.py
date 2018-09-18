class CNC:
    working = False
    having = False
    broken = False
    shouldbro = False
    whethersec = False
    mytime = 0
    brokentime = 0
    brokenmoment = 0

    def __init__(self, num, doubleprocess, oneprotime, twoprotime):
        self.num = num
        self.doubleprocess = doubleprocess
        if doubleprocess:
            self.oneprotime = oneprotime
            self.twoprotime = 0
        else:
            self.oneprotime = oneprotime
            self.twoprotime = twoprotime

    def changestatu(self):
        if not self.working:
            self.working = True
            self.mytime = 0
        else:
            self.working = False

    def goodtrans(self):
        if not self.having:
            self.having = True
        else:
            self.having = False

    def brokenfix(self):
        if not self.broken:
            self.broken = True
            self.mytime = 0
            self.changestatu()
            self.having = False
            self.shouldbro = False
        else:
            self.broken = False
            self.working = False
            self.having = False

    def addmytime(self, secs):
        if self.working:
            self.mytime += secs
        if self.broken:
            self.mytime += secs
        if not self.whethersec:
            if self.mytime >= self.oneprotime and self.working:
                self.changestatu()
        else:
            if self.mytime >= self.twoprotime and self.working:
                self.changestatu()
        if self.mytime >= self.brokentime and self.broken:
            self.brokenfix()
            print("broken fixed", self.mytime)

    def becomesec(self):
        self.whethersec = True

    def rebuild(self):
        self.working = False
        self.having = False
        self.broken = False
        self.shouldbro = False
        self.whethersec = False
        self.mytime = 0
        self.brokentime = 0
        self.brokenmoment = 0

    def cncprint(self):
        print(self.num, self.working, self.having, self.oneprotime, self.twoprotime)

