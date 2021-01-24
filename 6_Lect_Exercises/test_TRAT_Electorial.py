# #Program to demonstrate testing for main program -> TRAT_Electorial.py - 04/11/2020
# Created by: Andy Blankley

from TRAT_Electorial import mean_of_list, median_of_list, mode_of_list, range_of_list, standard_deviation, correlation
from pytest import approx

### Test of the MEAN Function
def test_mean():
    assert mean_of_list([7,9,5,3]) == 6

### Test of the MEDIAN Function
def test_median():
    assert median_of_list([1,2,3,3,3,4,5]) == 3
    assert median_of_list([1,2,3,3,4,5,7,7]) == 3.5

### Test of the MODE Function
def test_mode():
    assert mode_of_list([2,3,3,3,4,5,7,7,8,8]) == 3
    assert mode_of_list([1,2,3,3,4,5,7,7,8,8,8]) == 8   # Failing purposely.

### Test of the RANGE Function
def test_range():
    assert range_of_list([1,7,9,8,5]) == 8

### Test of the STANDARD DEVIATION Function
def test_stnd_deviation():
    assert standard_deviation([1,2,3,4,4,5]) == approx(1.47, 0.01)

### Test of the CORRELATION Function
def test_correlation():
    assert correlation([1,2,3,4], [2,4,6,8]) == approx(1)
    assert correlation([1,2,3,4], [8,6,4,2]) == approx(-1)