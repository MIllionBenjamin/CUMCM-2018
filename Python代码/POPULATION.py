import random
import operator


class Population:
    generation = 0
    allchromo = [[-1],
                 [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1],
                 [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]]

    fitness = [-1,
               -1, -1, -1, -1, -1, -1, -1, -1,
               -1, -1, -1, -1, -1, -1, -1, -1]

    chosenposibilty = [ 0,
                       -1, -1, -1, -1, -1, -1, -1, -1,
                       -1, -1, -1, -1, -1, -1, -1, -1]

    def __init__(self):
        for i in range(1, 16 + 1):
            for j in range(1, 8 + 1):
                self.allchromo[i].append(random.randint(0, 1))

    def setfitness(self, num, fitamount):
        self.fitness[num] = fitamount

    def setchoice(self):
        totalfits = 0
        for i in range(1, 16 + 1):
            totalfits += self.fitness[i]
        for j in range(1, 16 + 1):
            self.chosenposibilty[j] = 10 * round(self.fitness[j] / totalfits, 1) + self.chosenposibilty[j - 1]

    def selecteva(self):
        copyallchro = self.allchromo.copy()
        for i in range(1, 16 + 1):
            ran = random.randint(1, max(self.chosenposibilty))
            for j in range(1, 16 + 1):
                if self.chosenposibilty[j] >= ran:
                    self.allchromo[i] = copyallchro[j]
                    break
        for k in range(1, 15 + 1):
            if operator.eq(self.allchromo[k], self.allchromo[k+1]):
                k += 1
                continue
            elif random.randint(1, 10) <= 9:
                ran2 = random.randint(1, 8)
                trans = self.allchromo[k][:ran2]
                self.allchromo[k][:ran2] = self.allchromo[k + 1][:ran2]
                self.allchromo[k + 1][:ran2] = trans
                k += 1
            else:
                k += 1
        for a in range(1, 16 + 1):
            if random.randint(1, 10) == 10:
                ran3 = random.randint(1, 8)
                if self.allchromo[a][ran3] == 1:
                    self.allchromo[a][ran3] = 0
                else:
                    self.allchromo[a][ran3] = 1
        self.generation += 1



