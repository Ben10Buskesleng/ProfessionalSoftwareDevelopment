import numpy as np

class examclass:
    def __init__(self, min1, max2, amount):
        self.min1 = min1
        self.max2 = max2
        self.amount = amount

    def numgenerator(self):
        listOfNumbers = []
        for i in range(self.amount):
            listOfNumbers.append(np.random.randint(self.min1, self.max2))
        return listOfNumbers



randomnumber1 = examclass(5,30,50)
print(randomnumber1.numgenerator())





