import sys
from tabulate import tabulate



# 0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
class PrimeList:
    def __init__(self):
        self.primeList = [{"number": 0, "expression": "1 * 0"},
                          {"number": 1, "expression": "1 * 1"},
                          {"number": 2, "expression": "1 * 2"},
                          {"number": 3, "expression": "1 * 3"},
                          {"number": 5, "expression": "1 * 5"},
                          {"number": 7, "expression": "1 * 7"},
                          {"number": 11, "expression": "1 * 11"},
                          {"number": 13, "expression": "1 * 13"},
                          {"number": 17, "expression": "1 * 17"},
                          {"number": 19, "expression": "1 * 19"},
                          {"number": 23, "expression": "1 * 23"},
                          {"number": 29, "expression": "1 * 29"}]

    # this method return True/False if number is prime or not
    def isPrime(self, number):
        factors = 0;
        iterator = 1;
        if number == 1 or number == 0:
            return True

        if number < 0:
            return False

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
                self.primeList.append({"number":number, "expression": "1 * " + str(number)})
                print(str(number) + " has been added!")
                return True
            return False

        return False

    # display multiplication table of prime numbers
    def displayPrimeListTable(self):
        table=[]

        for number in self.primeList:
            table.append([number["number"], number["expression"]])

        print (tabulate(table, headers=['Number', 'Expression'], tablefmt='orgtbl'))

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
