import time
import random
"""```txt
Input: [3, 5, -1, 2]
Output: [-1, 2, 3, 5]
"""

"""
use selection sort to the array
finding min values using built in methods is ok

element, index
if index + 1 < index, 

"""


def main(array):

    counter = 0
    min_value = 0
    current_value = 0

    while counter < len(array):
        current_value = array[counter]
        min_value = min(array[counter:len(array)])
        min_pos = array.index(min_value)
        if current_value > min_value: 
            array[counter] = min_value
            array[min_pos] = current_value
        counter +=1
    return array


if __name__ == "__main__":

    test_values = [
        [10, 4, 3, 2, 1, 5],
        [],
        [1],
        [-1,-1,-1,-1]
    ]

    test_answers = [
        [1, 2, 3, 4, 5, 10],
        [],
        [1],
        [-1,-1,-1,-1]

    ]

    # for value, answer in zip(test_values, test_answers):
    #     print(value, answer)
    #     result = main(value)
    #     assert result == answer, f"Expected {answer}, got {result}"
    #     print(f"Successful")

    # print(main([1]))


    #BENCHMARK
    # BENCHMARK HERE

    long_input = []

    for i in range(100):
        long_input.append(random.uniform(0, 1))

    start_time = time.time()

    for i in range(1000):
        main([2, 1])
        main(long_input)

    avg_time = ( time.time() - start_time ) / 2000

    print(avg_time)