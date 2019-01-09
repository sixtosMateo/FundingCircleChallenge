# Funding Circle Challenge - Multiplication Table of Prime Numbers

## Overview
Write a program that prints out a multiplication table of the first 10 prime
number.
● The program must run from the command line and print one table to STDOUT.
● The first row and column of the table should have the 10 primes, with each
  cell containing the product of the primes for the corresponding row and
  column.

## Dependencies
Required python3.4
Required tabulate
  - pip3 install tabulate
  - pip install tabulate

## How to Run
For simplicity purposes Challenge was done in one file:
  1) open terminal:
  2) git clone https://github.com/sixtosMateo/FundingCircleChallenge
  3) Navigate to FundingCircle directory:
      -  run $ python3 app.py or
      -  run $ python app.py

  4) To run Tests.py  
      -  Navigate to FundingCircle directory:
      -  run $ pytest Tests.py

## How to use:
  /app.py

  # Maxsize of a int in python3.4 is 9223372036854775807 lets not get
    carry away let stay within this range

  Program will ask for input: 1, 2, 3, 4:
    - 1: will display the table with default values included
    - 2: will allow user to add a prime number if requirements are met
    - 3: will allow user to clear prime numbers inserted except default values
    - 4: will end program

## Improvements on Program
    - sort prime numbers as they are inserted
    - improve isDuplicateNumber method by using binarysearch if prime numbers
      are sorted
    - create a feature/method that allows user to view the expression of one
      prime number
