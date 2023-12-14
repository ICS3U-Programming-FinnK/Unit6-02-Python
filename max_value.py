#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 14th, 2023
# this program generates 10 numbers between 0 to 100 and it finds the maximum value of the list.
import random

MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def find_max_value(arr):
    # Initializing the max value as the first element in the array
    max_value = arr[0]

    # Looping through the array to find the maximum value
    for num in arr:
        if num > max_value:
            max_value = num

    return max_value


def main():
    # Generating 10 random numbers between MIN_NUM and MAX_NUM
    random_numbers = [random.randint(MIN_NUM, MAX_NUM) for _ in range(MAX_ARRAY_SIZE)]

    # Printing the generated numbers
    print("Generated Numbers:")
    print(random_numbers)

    # Finding the maximum value using the find_max_value function
    max_value = find_max_value(random_numbers)

    # Displaying the maximum value
    print("Maximum Value:", max_value)


# Calling the main function to run the program
if __name__ == "__main__":
    main()
