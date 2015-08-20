#!/usr/bin/python
""" Quick and dirty demo and comparison of various sorting algorithm
    implementations in Python.  As a benchmark the native python list sorting
    (Timsort) and the numpy Quicksort are included in the benchmark. Basic
    testing is performed.

    Author: Valentin Haenel
    Licence: wtfpl unless specified otherwise in attribution

    Profiling 3b18c79 on my machine (3.20GHz Ghz Quad Core Intel 6GB Ram with
    Hyperthreading enabled:

    Timing
    -----------------------------------------------------------
    Quicksort (val's)
    166.09 mseconds/pass
    Quicksort in-place
    252.70 mseconds/pass
    Quicksort in-place, optimized
    166.33 mseconds/pass
    Quicksort list comprehension
    187.01 mseconds/pass
    Mergesort
    807.52 mseconds/pass
    Mergesort2
    372.50 mseconds/pass
    Mergesort3
    275.95 mseconds/pass
    Mergesort4
    320.43 mseconds/pass
    Native
    32.07 mseconds/pass
    Numpy
    10.34 mseconds/pass



    Leading to the following ranking:
        1) Numpy
        2) Native
        3) Quicksort (vals's)
        4) Quicksort in-place, optimized
        5) Quicksort list comprehension
        6) Quicksort in-place
        7) Mergesort3
        7) Mergesort4
        8) Mergesort2
        9) Mergesort1

    A couple of things to note:
        a) Native and Numpy are an order of magnitude faster.
        b) Quicksort is faster than Mergesort, which is to be expected
        theoretically. (Maybe also the reason for numpy being faster than
        native, since Timsort is a Mergesort/Insertionsort hybrid)
        c) What baffles me, is that the inplace Quicksort isn't faster than the
        one that allocates more and more lists. Even the highly optimized one.
"""

import sys
from random import randint, shuffle, choice, randrange, random
from timeit import Timer
import numpy
import numpy.testing
import nose.tools as nt

print sys.getrecursionlimit()
sys.setrecursionlimit(2000)

def quicksort_val(array):
    """ Stable out-of-place Quicksort.

    This is written by yours truly in pythonic style.

    Parameters
    ----------
    array : list
        a possibly unordered list

    Returns
    -------
    sorted : list
        a sorted list
    """
    if len(array) <= 1:
        return array
    lower, upper, center = [], [], []
    part = choice(array)
    for i in array:
        if i < part:
            lower.append(i)
        elif i > part:
            upper.append(i)
        else:
            center.append(i)
    return quicksort_val(lower) + center + quicksort_val(upper)

def swap(array, i, j):
    """ Helper function for quicksort_ip. """
    array[i], array[j] = array[j], array[i]

def quicksort_ip(array, low, high):
    """ Quicksort 'array' in-place.

    This is converted from C code found in chapter three of:
    Beautiful Code
    Leading Programmers Explain How They Think

    Edited By Andy Oram & Greg Wilson
    First Edition Juli 2007
    ISBN 978-0-596-51004-6

    Should be fast as hell, no idea why its so slow.

    Parameters
    ----------
    low : int
        smallest index to consider
    high : int
        largest index to consider
    """
    if low >= high:
        return
    part, counter = randint(low, high), low
    swap(array, part, low)
    array_low = array[low]
    for i in xrange(low+1, high+1):
        if array[i] < array_low:
            counter += 1
            swap(array, counter, i)
    swap(array, low, counter)
    quicksort_ip(array, low, counter-1)
    quicksort_ip(array, counter+1, high)

def quicksort_pb(array):
    """ Quicksort 'array' in-place, optimized.

    Contributed by Pietro Berkes

    This function works exactly like quicksort_ip, heavily
    optimized at the expenses at readability.

    Parameters
    ----------
    low : int
        smallest index to consider
    high : int
        largest index to consider
    """

    # init stack, used to avoid recursion
    low, high = 0, len(array)-1
    stack_len = int(numpy.log(high)*20)
    stack_left = [None] * stack_len
    stack_right = [None] * stack_len
    idx_left = 0
    idx_right = -1

    stack_left[0] = (low, high)
    while True:
        while idx_left > -1:
            low, high = stack_left[idx_left]
            idx_left -= 1
            if low < high: break
            if idx_right > -1:
                low, high = stack_right[idx_right]
                idx_right -= 1
                if low < high: break
        else:
            return

        part = int(random() * (high-low) + low)
        counter = low
        #swap(array, part, low)
        array[part], array[low] = array[low], array[part]
        array_low = array[low]
        for i in xrange(low+1, high+1):
            if array[i] < array_low:
                counter += 1
                #swap(array, counter, i)
                array[counter], array[i] = array[i], array[counter]
        #swap(array, low, counter)
        array[low], array[counter] = array[counter], array[low]
        idx_left += 1
        stack_left[idx_left] = (low, counter-1)
        if counter+1 < high:
            idx_right += 1
            stack_right[idx_right] = (counter+1, high)

def quicksort_lc(array):
    """ This is a Quicksort using list comprehensions.

    It is taken from:
        http://en.literateprograms.org/Quicksort_(Python)
    According to the article it was the fastest of all of the three. However it
    doesn't run faster than val's quicksort. Perhaps this is due to having to
    iterate over the array twice each time, for each list comprehension?

    Parameters
    ----------
    array : list
        a possibly unordered list
        WARNING: this should be copied before use, as it will shrink.

    Returns
    -------
    sorted : list
        a sorted list
    """
    if array == []:
        return []
    else:
        pivot = array.pop(randrange(len(array)))
        lesser = quicksort_lc([l for l in array if l < pivot])
        greater = quicksort_lc([l for l in array if l >= pivot])
        return lesser + [pivot] + greater

def mergesort(array):
    """ Stable Mergesort (first attempt).

    Written by yours truly but inspired by pseudocode from:
        http://en.wikipedia.org/wiki/Merge_sort

    Has the downside of popping items off of a list from the front, causing
    resizing to happen all the time.

    Parameters
    ----------
    array : list
        a possibly unordered list

    Returns
    -------
    sorted : list
        a sorted list
    """
    if len(array) <= 1:
        return array
    part = len(array)//2
    return merge(mergesort(array[:part]), mergesort(array[part:]))

def merge(array1, array2):
    """ Helper for mergesort."""
    result = []
    while len(array1) or len(array2):
        if len(array1) and len(array2):
            if array1[0] <= array2[0]:
                result.append(array1.pop(0))
            else:
                result.append(array2.pop(0))
        elif len(array1):
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))
    return result

def mergesort2(array):
    """ Stable Mergesort (second version).

    An improvement on mergesort.

    This implementation alleviates the problem of having to pop of the front of
    the list, but then needs to reverse it after each merge of two lists. Minor,
    but statistically significant speed up.

    Parameters
    ----------
    array : list
        a possibly unordered list

    Returns
    -------
    sorted : list
        a sorted list
    """
    if len(array) <= 1:
        return array
    part = len(array)//2
    return merge2(mergesort2(array[:part]), mergesort2(array[part:]))

def merge2(array1, array2):
    """ Helper for mergesort2."""
    result = []
    while len(array1) or len(array2):
        # larger values go in first
        if len(array1) and len(array2):
            if array1[-1] >= array2[-1]:
                result.append(array1.pop())
            else:
                result.append(array2.pop())
        elif len(array1):
            result.append(array1.pop())
        else:
            result.append(array2.pop())
    # Here we need to reverse the array, so that smaller values are at the
    # beginning.
    # In numpy we could do this with strides, obviously.
    # Still, popping values of the end of the list and reversing is faster than
    # popping them off the front and resizing.
    result.reverse()
    return result

def mergesort3(array):
    """ Stable mergesort (version three).

    The code was taken from:
        http://en.literateprograms.org/Merge_sort_(Python)

    This one uses indices instead of popping from the list. Also the
    merge-helper is nicer. But code is less pythonic (uses indices). Faster than
    the previous two implementations.

    Parameters
    ----------
    array : list
        a possibly unordered list

    Returns
    -------
    sorted : list
        a sorted list
    """
    if len(array) <= 1:
        return array
    part = len(array)//2
    return merge3(mergesort3(array[:part]), mergesort3(array[part:]))

def merge3(array1, array2):
    """ Helper for mergesort3."""
    result = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    result += array1[i:]
    result += array2[j:]
    return result

def mergesort4(array):
    """ Stable in-place mergesort.

    Inspired by a codility exercise. Needs no pops or appends, just slicing.

    """
    if len(array) < 2:
        return 0
    m = (len(array) + 1) / 2
    left = array[0:m]
    right = array[m:len(array)]
    mergesort4(left)
    mergesort4(right)
    merge4(array, left, right)

def merge4(array, left, right):
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if i == len(left):
            array[i + j] = right[j]
            j += 1
        elif j == len(right):
            array[i + j] = left[i]
            i += 1
        elif left[i] <= right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1


def mergesort5(lst):
    """ Taken from:

    https://github.com/hugopeixoto/mergesort/blob/master/python/mergesort.py

    """
    if len(lst) < 2:
        return lst

    m = len(lst)/2
    return merge5(mergesort5(lst[:m]), mergesort5(lst[m:]))

def merge5(a, b):
    if len(a)*len(b) == 0:
        return a+b

    v = (a[0] < b[0] and a or b).pop(0)
    return [v] + merge5(a, b)

number_repeats = 10
array_size = 2000
def do_timing(timer):
    """ Execute timer and print result."""
    print ("%.2f mseconds/pass" %
    (1000 * timer.timeit(number=number_repeats)/number_repeats))

target_array = range(array_size)
original = target_array[:]

def testing():

    print 'Testing'
    print "-----------------------------------------------------------"

    shuffle(target_array)
    print "Quicksort (val's)"
    nt.assert_equal(quicksort_val(target_array), original)

    shuffle(target_array)
    print "Quicksort in-place"
    quicksort_ip(target_array, 0, len(target_array)-1)
    nt.assert_equal(target_array, original)

    shuffle(target_array)
    print "Quicksort in-place, optimized"
    quicksort_pb(target_array)
    nt.assert_equal(target_array, original)

    shuffle(target_array)
    print "Quicksort list comprehension"
    to_sort = target_array[:]
    nt.assert_equal(quicksort_lc(to_sort), original)

    shuffle(target_array)
    print 'Mergesort'
    nt.assert_equal(mergesort(target_array), original)

    shuffle(target_array)
    print 'Mergesort2'
    nt.assert_equal(mergesort2(target_array), original)

    shuffle(target_array)
    print 'Mergesort3'
    nt.assert_equal(mergesort3(target_array), original)

    shuffle(target_array)
    print 'Mergesort4'
    to_sort = target_array[:]
    mergesort4(target_array)
    nt.assert_equal(target_array, original)

    shuffle(target_array)
    print 'Mergesort5'
    nt.assert_equal(mergesort5(target_array), original)

    shuffle(target_array)
    print 'Native'
    target_array.sort()
    nt.assert_equal(target_array, original)

    np_array = numpy.arange(array_size)
    np_original = np_array.copy()
    numpy.random.shuffle(np_array)
    print 'Numpy'
    np_array.sort()
    numpy.testing.assert_array_equal(np_array, np_original)

    print "-----------------------------------------------------------"

def timing():

    print 'Timing'
    print "-----------------------------------------------------------"

    def get_timer(func_name, args_str='target_array'):
        """
        Parameters
        ----------
        func_name -- string with name of the sorting function
        args_str -- string with list of arguments
        """

        _timer_code = """
        target_array = range(%(size)i)
        shuffle(target_array)
        %(func_name)s(%(args)s)
        """
        _timer_import = 'from __main__ import shuffle, %(func_name)s'
        _dict = {'size': array_size, 'func_name': func_name, 'args': args_str }
        return Timer(_timer_code % _dict, _timer_import % _dict)


    print "Quicksort (val's)"
    do_timing(get_timer('quicksort_val'))

    print "Quicksort in-place"
    do_timing(get_timer('quicksort_ip',
                        'target_array, 0, len(target_array)-1'))


    print "Quicksort in-place, optimized"
    do_timing(get_timer('quicksort_pb'))

    print "Quicksort list comprehension"
    do_timing(get_timer('quicksort_lc', 'target_array[:]'))

    print 'Mergesort'
    do_timing(get_timer('mergesort'))

    print 'Mergesort2'
    do_timing(get_timer('mergesort2'))

    print 'Mergesort3'
    do_timing(get_timer('mergesort3'))

    print 'Mergesort4'
    do_timing(get_timer('mergesort4'))

    print 'Mergesort5'
    do_timing(get_timer('mergesort5'))

    print 'Native'
    t = Timer("""
    target_array = range(%i)
    shuffle(target_array)
    target_array.sort()
    """% array_size, "from __main__ import shuffle")
    do_timing(t)

    print 'Numpy'
    t = Timer("""
    np_array = numpy.arange(%i)
    numpy.random.shuffle(np_array)
    np_array.sort()
    """% array_size, "from __main__ import shuffle, numpy")
    do_timing(t)

    print "-----------------------------------------------------------"

if __name__ == '__main__':
    testing()
    timing()
