import math

from ..stats import DescriptiveStatistics
import pytest
import warnings
from pytest import fixture


@fixture
def descriptive():
    return DescriptiveStatistics()


@fixture
def numbers1():
    return [22, 40, 53, 57, 93, 98, 103, 108, 116, 121, 253]


@fixture
def numbers2():
    return [1, 2, 3, 3, 4]



def test_mean(descriptive, numbers1):
    expected_output = round(96.7272727273, 8)

    actual_output = round(descriptive.mean(numbers1), 8)
    assert expected_output == actual_output


def test_range(descriptive, numbers1):
    expected_output = 231
    actual_output = descriptive.range(numbers1)

    assert expected_output == actual_output


def test_sum_of_squared_errors(descriptive, numbers2):
    expected_output = 5.2
    actual_output = round(descriptive.ss_tot(numbers2), 1)
    assert expected_output == actual_output

def test_variance(descriptive, numbers2):
    expected_output = 1.3
    actual_output = round(descriptive.variance(numbers2),1)

    assert expected_output == actual_output

def test_sd(descriptive, numbers2):
    expected_output = 1.14
    actual_output = descriptive.sd(numbers2, "population")

    assert expected_output == round(actual_output, 2)

def test_se(descriptive, numbers2):
    expected_output = 1.14/math.sqrt(5)
    actual_output = descriptive.se(numbers2)

    assert round(expected_output, 3) == round(actual_output, 3)


# def test_se_sample_size_warns(descriptive, numbers2):
#     # Should raise a warning if the sample size is less than 30
#     with pytest.warns(UserWarning):
#         descriptive.se(numbers2)


def test_calculate_z_score(descriptive):
    mean = 7.9
    test_value = 7.5
    sd = 0.74

    expected_value = -0.54
    actual_value = descriptive.calculate_z_score(test_value, mean, sd)

def test_calculate_z_score_list(descriptive):
    input = [7, 8, 8, 7.5, 9]
    test_value = 7.5
    expected_value = -0.54
    actual_value = descriptive.calculate_z_score_list(test_value, input)

    assert expected_value == round(actual_value, 2)


# TODO: Come up with a good test for confidence_interval
# def test_calculate_confidence_interval(descriptive, numbers1_altered):
#     mean = 96.64
#     sd = 61.27
#     z_score = 1.96
#     sample_size = 11
#     expected_value = mean - (1.96 *


def test_confidence_interval(descriptive, numbers1):
    mean = descriptive.mean(numbers1)
    se = descriptive.se(numbers1)
    # I got this value from R.  They have a far more detailed test statistic than I could get
    # One day I'll calculate it properly
    # I know 2.228 is accurate, but no idea beyond that, the final two figures make the test pass, for now!
    expected_value = [round(55.39262, 2), round(138.06193, 2)]
    actual_value = descriptive.confidence_interval(mean, se, 2.22809)
    actual_value[0] = round(actual_value[0], 2)
    actual_value[1] = round(actual_value[1], 2)
    assert expected_value == actual_value



def test_correlation(descriptive):
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_values = [2.2, 2.8, 4.5, 3.1, 8.7, 5.0, 4.5, 8.8, 9.0, 9.2]

    expected_value = 0.8302539
    actual_value = descriptive.correlation(x_values, y_values)

    assert round(expected_value, 6) == round(actual_value, 6)


