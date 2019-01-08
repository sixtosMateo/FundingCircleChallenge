import sys

# maxsize of a int in python3.4 is 9223372036854775807
# lets not get carry away let stay within this range

# 0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
class PrimeList:
    def __init__(self):
        self.primeList = [{"number": 0, "expresion": "1 * 0"},
                          {"number": 1, "expresion": "1 * 1"},
                          {"number": 2, "expresion": "1 * 2"},
                          {"number": 3, "expresion": "1 * 3"},
                          {"number": 5, "expresion": "1 * 5"},
                          {"number": 7, "expresion": "1 * 7"},
                          {"number": 11, "expresion": "1 * 11"},
                          {"number": 13, "expresion": "1 * 13"},
                          {"number": 17, "expresion": "1 * 17"},
                          {"number": 19, "expresion": "1 * 19"},
                          {"number": 23, "expresion": "1 * 23"},
                          {"number": 29, "expresion": "1 * 29"}]

    # this method return True/False if number is prime or not
    def isPrime(self, number):
        factors = 0;
        iterator = 1;

        while iterator <= number:
            if number % iterator == 0:
                factors += 1
            iterator += 1

        if factors == 2:
            return True
        else:
            print("The number "+str(number)+" is not a prime number")
            return False

    # this return True/False if number was added
    def addPrimeNumber(self, number):

        if self.isPrime(number):
            if self.isDuplicateNumber(number):
                self.primeList.append({"number":number, "expresion": "1 * " + str(number)})
                print(str(number) + " has been added!")
                return True
            return False

    # display multiplication table of prime numbers
    def displayPrimeListTable(self):
        for number in self.primeList:
            print(number["number"], number["expresion"])

    # display the set of prime numbers
    def displayPrimeNumbersOnly(self):
        for number in self.primeList:
            print(number["number"], end =" ")

    # clears prime numbers that were inserted
    def clearInsertPrime(self):
        for prime in self.primeList[12:]:
            self.primeList.remove(prime)
        print ("cleared")

    # returns True/False if number is duplicate
    def isDuplicateNumber(self, number):
        if number <= 29:
            print("This number " +  str(number) + " has been duplicated. Try another number!")
            return False

        for num in self.primeList[12:]:
            if number == num["number"]:
                print("This number " +  str(number)+ " has been duplicated. Try another number!")
                return False

        return True

obj = PrimeList()

# 37, 41, 43, 47, 53, 59, 61, 67, 71, 73
obj.addPrimeNumber(4)

obj.addPrimeNumber(31)
obj.displayPrimeNumbersOnly()
print()
obj.addPrimeNumber(41)
obj.displayPrimeNumbersOnly()
print()
obj.addPrimeNumber(43)
obj.displayPrimeNumbersOnly()
print()
obj.addPrimeNumber(43)
obj.displayPrimeNumbersOnly()
print()
obj.clearInsertPrime()

obj.displayPrimeNumbersOnly()
