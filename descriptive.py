import math


class DescriptiveStatistics(object):
    def mean(self, numbers):
        x = 0
        for n in numbers:
            x += x
        return x/len(numbers)

    def variance(self, numbers, mean, distribution="population"):
        if distribution == 'population':
            return self._variance_pop(numbers, mean)

    def _variance_pop(self, numbers, mean):
        return self._variance_calc(mean, len(numbers))

    def _variance_sample(self, numbers, mean):
        return self._variance_calc(mean, len(numbers) - 1)

    def _variance_calc(self, mean, n):
        return mean/n

    def sd(self, numbers, mean, distribution="population"):
        return math.sqrt(self.variance(numbers, mean, distribution))

    def se(self):
        pass

    def correlation(self):
        pass

    def correlation_spearman(self):
        pass

    def r_squared(self):
        pass

    def confidence_interval(self):
        pass