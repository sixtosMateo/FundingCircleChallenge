import unittest
from . import PrimeList


class Tests(unittest.TestCase):


    def test_is_prime(self):
        self.prime = PrimeList()
        # test is number is prime or not
        print("test_is_prime()")
        self.assertEqual(False, self.prime.isPrime(15))
        self.assertEqual(False, self.prime.isPrime(69))
        self.assertEqual(True, self.prime.isPrime(167))

    def test_add_prime_number(self):
        self.prime = PrimeList()
        print("test_add_prime_number")
        self.assertEqual(False, self.prime.addPrimeNumber(15))
        self.assertEqual(False, self.prime.addPrimeNumber(69))
        self.assertEqual(True, self.prime.addPrimeNumber(167))
        # should not pass because its a dusplicate
        self.assertEqual(False, self.prime.addPrimeNumber(167))

    def test_duplicate_number(self):
        self.prime = PrimeList()
        print("test_duplicate_number")
        self.assertEqual(False , self.prime.isDuplicateNumber(15))
        self.assertEqual(True, self.prime.isDuplicateNumber(69))
        self.assertEqual(True, self.prime.isDuplicateNumber(167))
        self.assertEqual(False, self.prime.isDuplicateNumber(29))
