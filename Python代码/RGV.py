class RGV:
    haveone = False

    def __init__(self, movetime, oddchangetime, evenchangetime, washtime, location):
        self.movetime = movetime.copy()
        self.oddchangetime = oddchangetime
        self.evenchangetime = evenchangetime
        self.washtime = washtime
        self.location = location

    def move(self, step):
        self.location += 2*step

    def catchone(self):
        if not self.haveone:
            self.haveone = True
        else:
            print("Error in catching")

    def putone(self):
        if self.haveone:
            self.haveone = False
        else:
            print("Error in putting")

    def rgvprint(self):
        print(self.location, self.haveone)