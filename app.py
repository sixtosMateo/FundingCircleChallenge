from __init__ import PrimeList

obj = PrimeList()

while (True):
    print("Enter 1 to see Table:")
    print("Enter 2 add Prime Number: ")
    print("Enter 3 to clear prime numbers insert:")
    print("Enter 4 to cancel program:")
    user_input = input("Some input please: ")

    if user_input =="1":
        obj.displayPrimeListTable()

    elif user_input =="2":
        prime = input("Enter a number: ")

        if prime.isdigit():
            prime = int(prime)
            obj.addPrimeNumber(prime)
            prime = ""
        else:
            print("Not a correct input!")

    elif user_input =="3":
        obj.clearInsertPrime()

    elif user_input =="4":
        break

    else:
        print("Enter a correct option (1,2,3,4):")

    print("\n\n\n\n")
