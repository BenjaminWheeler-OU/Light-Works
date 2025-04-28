#!/bin/python
import unittest
import json
import os

def readJSONFile():
    path = "Unit Tests/test.json"
    try:
        file = open(path)
        return json.load(file)
    except Exception as e:
        return e

class TestJSONFile(unittest.TestCase):
    data = readJSONFile()

    def test_check_data_loaded(self):
        self.assertNotIsInstance(self.data, Exception, "Data could not be loaded: {data}")

    def test_data_is_list(self):
        self.assertIsInstance(self.data, dict, "Data is not a dictionary")

    def test_entry_structure(self):
        self.assertIn('city', self.data)
        self.assertIn('simulation_speed', self.data)

        self.assertIsInstance(self.data['city'], str, "City is not a string")
        self.assertIsInstance(self.data['simulation_speed'], float, "Simulation speed is not a float")

        self.assertGreater(self.data['simulation_speed'], 0, "Simulation speed is not positive")
if __name__ == '__main__':
    unittest.main()