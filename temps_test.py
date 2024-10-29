import unittest
import temps

class TestTempFunctions(unittest.TestCase):

    def test_sort_temperatures(self):
        measurements = [96, 97, 99, 100]
        low, normal, high = temps.sort_temperatures(measurements)
        self.assertEqual(low, [96])
        self.assertEqual(normal, [97, 99])
        self.assertEqual(high, [100])

    def test_sort_temperatures_only_lows(self):
        measurements = [93, 94, 92]
        low, normal, high = temps.sort_temperatures(measurements)
        self.assertEqual(low, [93, 94, 92])
        self.assertEqual(normal, [])
        self.assertEqual(high, [])

    def test_sort_temperatures_no_measures(self):
        measurements = []
        low, normal, high = temps.sort_temperatures(measurements)
        self.assertEqual(low, [])
        self.assertEqual(normal, [])
        self.assertEqual(high, [])

    def test_sort_temperatures_floating_points(self):
        measurements = [99.2, 95, 100.3, 98.1]
        low, normal, high = temps.sort_temperatures(measurements)
        self.assertEqual(low, [95])
        self.assertEqual(normal, [98.1])
        self.assertEqual(high, [99.2, 100.3])
