
import pytest
import sys
sys.path.insert(1,'../')

from Exercises.Numbers import *

def test_piToNth():
    assert pi_to_nth(0) == 3
    assert pi_to_nth(1) == 3.1
    assert pi_to_nth(2) == 3.14
    assert pi_to_nth(-1) == "Enter number greater than or equal to 0"
    assert pi_to_nth(16) == "Enter number from 0 to 15 only"
    assert pi_to_nth(15) == 3.141592653589793

def test_eToNth():
    assert e_to_nth(0) == 2
    assert e_to_nth(1) == 2.7
    assert e_to_nth(2) == 2.72
    assert e_to_nth(-1) == "Enter number greater than or equal to 0"
    assert e_to_nth(16) == "Enter number from 0 to 15 only"
    assert e_to_nth(15) == 2.718281828459045

def test_fibonacci():
    assert fibonacci_sequence(4) == [0, 1, 1, 2]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(-1) == "Error"

def test_primeFactorization():
    assert prime_factorization(1) == "1 is neither prime nor composite"
    assert prime_factorization(2) == [2]
    assert prime_factorization(3) == [3]
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(54) == [2, 3, 3, 3]
    assert prime_factorization(24) == [2, 2, 2, 3]

if __name__ == '__main__':
    test_piToNth()
    test_eToNth()
    test_fibonacci()
    test_primeFactorization()