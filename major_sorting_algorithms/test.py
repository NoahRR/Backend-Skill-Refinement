import unittest
import insertion, bubble, selection, quick, merge
import time
from random import randint


# testing:  selection, bubble
#           insertion
#           quick
#           merge


# tests
class test1_bubble_sorting_test(unittest.TestCase):
    def test_all(self):
        total = testing("bubble.bubble_sort", self)
        print('.........................BUBBLE SORT TIMER:')
        print(str(total)[:5] + ' / 10,000 s')

class test2_selection_sorting_test(unittest.TestCase):
    def test_all(self):
        total = testing("selection.selection_sort", self)
        print('........................SELECTION SORT TIMER:')
        print(str(total)[:5] + ' / 10,000 s')

class test3_insertion_sorting_test(unittest.TestCase):
    def test_all(self):
        total = testing("insertion.insertion_sort", self)
        print('........................INSERTION SORT TIMER:')
        print(str(total)[:5] + ' / 10,000 s')

class test4_quick_sorting_in_place_test(unittest.TestCase):
    def test_all(self):
        total = testing("quick.quick_sort", self)
        print('........................QUICK SORT TIMER:')
        print(str(total)[:5] + ' / 10,000 s')

class test5_merge_sorting(unittest.TestCase):
    def test_all(self):
        total = testing("merge.merge_sort", self)
        print('........................MERGE SORT TIMER:')
        print(str(total)[:5] + ' / 10,000 s')

# funcitonality for tests
def testing(sort_function, self):

    total_time = 0

    for item in arr_holder:

        # values to test
        input_array = item['input_array']
        correct_array = item['sorted']

        # querying algorithm
        start = time.time()
        return_arr = eval(sort_function + f"({input_array})")
        end = time.time()
        total_time += ((end-start) * 10000)

        # test correctness
        self.assertEqual(return_arr, correct_array)

    # querying algorithm with long array to test speed
    start = time.time()
    return_arr = eval(sort_function + f"({random_long_arr})")
    end = time.time()
    total_time += ((end-start) * 10000)

    return total_time


# create random and long array
random_long_arr = []
for i in range(902):
    random_long_arr.append( randint(0, 100) )
correct_random_long_array = random_long_arr.sort()

# holds test arrays and correct answers
arr_holder = [
    {
        'input_array': [1,2,3,4],
        'sorted': [1,2,3,4]
    },
    {
        'input_array': [6,5,4,3,2,1,0],
        'sorted': [0,1,2,3,4,5,6]
    },
    {
        'input_array': [1,2,5,8,9,5,2,1,1,4],
        'sorted': [1,1,1,2,2,4,5,5,8,9]
    },
    {
        'input_array': [33,0,1,1,1,1,2,3,4,8,9,2,11,3],
        'sorted': [0,1,1,1,1,2,2,3,3,4,8,9,11,33]
    },
    {
        'input_array': [215,3,12,8,12,43,1,1,216],
        'sorted': [1,1,3,8,12,12,43,215,216]
    },
    {
        'input_array': [66416,0,124,102957501,235,1,7,8,3,1,1,1,32,333,2347,9,0],
        'sorted': [0, 0, 1, 1, 1, 1, 3, 7, 8, 9, 32, 124, 235, 333, 2347, 66416, 102957501]
    },
    {
        'input_array': [2,7,7,4,434,4,4,4,4,4,4,4,1,12,99999,23,2,4],
        'sorted': [1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 12, 23, 434, 99999]
    },
    {
        'input_array': [0,0,125,2115,2115,6662,1,252,33379,22,1],
        'sorted': [0, 0, 1, 1, 22, 125, 252, 2115, 2115, 6662, 33379]
    },
    {
        'input_array': [2, -2, -1, 0, 6, 5],
        'sorted': [-2, -1, 0, 2, 5, 6]
    },
]


# run tests
if __name__ == '__main__':
    unittest.main()
