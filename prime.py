# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
import math

class PrimeList:
    def __init__(self):
        self.primeList = [{"number": 2, "expresion": "1*2"},
                          {"number": 3, "expresion": "1*3"},
                          {"number": 5, "expresion": "1*5"},
                          {"number": 7, "expresion": "1*7"},
                          {"number": 11, "expresion": "1*11"},
                          {"number": 13, "expresion": "1*13"},
                          {"number": 17, "expresion": "1*17"},
                          {"number": 19, "expresion": "1*19"},
                          {"number": 23, "expresion": "1*23"},
                          {"number": 29, "expresion": "1*29"}]

    def isPrime(self, number):
        factors = 0;
        iterator = 1;

        while iterator <= number:
            if number % iterator == 0:
                factors += 1
            iterator += 1

        return factors == 2;

    def addPrimeNumber(self, number):
        if self.isPrime(number):
            self.primeList.append({"number":number, "expresion": "1*" + str(number)})
            return True
        else:
            return False

    def displayPrimeListTable(self):
        for number in obj.primeList:
            print(number["number"], number["expresion"])

    def displayPrimeNumbersOnly(self):
        for number in obj.primeList:
            print(number["number"], end =" ")

    def clearInsertPrime(self):
        for prime in self.primeList[10:]:
            self.primeList.remove(prime)
        print ("cleared")


obj = PrimeList()

obj.displayPrimeNumbersOnly()

print()

obj.addPrimeNumber(31)

#
obj.displayPrimeNumbersOnly()

print()
obj.addPrimeNumber(77)
obj.addPrimeNumber(937)

obj.displayPrimeNumbersOnly()
print()
obj.clearInsertPrime()

obj.displayPrimeNumbersOnly()
