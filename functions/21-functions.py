#!/usr/bin/env python3
#In this very first programming challenge, your goal is to implement a program that reads two digits from the standard input and prints their sum to the standard output.  We start from this ridiculously simple problem to show you the pipeline of reading the problem statement, designing an algorithm, implementing it,testing and debugging your program.

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))

