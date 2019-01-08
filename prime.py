# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
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
        if number % 2 == 0:
            return False
        else:
            return True

    def addPrimeNumber(self, number):
        if self.isPrime(number):
            self.primeList.append({"number":number, "expresion": "1*" + str(number)})
            return True
        else:
            return False

    def 

obj = PrimeList()

obj.addPrimeNumber(31)



for number in obj.primeList:
    print(number["number"], number["expresion"] )

# print(obj.isPrime(4))
