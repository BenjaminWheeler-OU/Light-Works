import unittest
import re

def sanitize_input(value):
    """Sanitize string input to neutralize potential XSS vectors."""
    if isinstance(value, str):
        # Remove any script tags or suspicious characters
        return re.sub(r'(?i)<script.*?>.*?</script>', '', value).strip()
    return value

def validate_knitPublicReport(trafficData):
    if not isinstance(trafficData, list) or len(trafficData) == 0:
        return False
    for entry in trafficData:
        sanitized_entry = {k: sanitize_input(v) for k, v in entry.items()}

        if (
            not isinstance(sanitized_entry.get("avgEmissionAtIdle"), float) or sanitized_entry["avgEmissionAtIdle"] < 0 or
            not isinstance(sanitized_entry.get("timeSpentAtLight"), int) or sanitized_entry["timeSpentAtLight"] < 0 or
            not isinstance(sanitized_entry.get("avgStopTime"), int) or sanitized_entry["avgStopTime"] < 0 or
            not isinstance(sanitized_entry.get("numberOfCars"), int) or sanitized_entry["numberOfCars"] < 0
        ):
            return False
    return True

class TestTrafficReport(unittest.TestCase):
    def test_valid_report(self):
        valid_traffic_data = [{
            "avgEmissionAtIdle": 1.2,
            "timeSpentAtLight": 30,
            "avgStopTime": 20,
            "numberOfCars": 100
        }]
        self.assertTrue(validate_knitPublicReport(valid_traffic_data))
    
    def test_invalid_empty_report(self):
        self.assertFalse(validate_knitPublicReport([]))
    
    def test_invalid_non_list_traffic_data(self):
        self.assertFalse(validate_knitPublicReport("invalid_data"))
    
    def test_invalid_negative_values(self):
        invalid_traffic_data = [{
            "avgEmissionAtIdle": -1.2,
            "timeSpentAtLight": 30,
            "avgStopTime": 20,
            "numberOfCars": 100
        }]
        self.assertFalse(validate_knitPublicReport(invalid_traffic_data))
    
    def test_boundary_valid_zero_values(self):
        boundary_traffic_data = [{
            "avgEmissionAtIdle": 0.0,
            "timeSpentAtLight": 0,
            "avgStopTime": 0,
            "numberOfCars": 0
        }]
        self.assertTrue(validate_knitPublicReport(boundary_traffic_data))
    
    def test_edge_case_negative_numbers(self):
        edge_case_data = [{
            "avgEmissionAtIdle": 1.5,
            "timeSpentAtLight": -5,
            "avgStopTime": 10,
            "numberOfCars": 50
        }]
        self.assertFalse(validate_knitPublicReport(edge_case_data))

    def test_potential_xss_injection(self):
        malicious_traffic_data = [{
            "avgEmissionAtIdle": 1.5,
            "timeSpentAtLight": 20,
            "avgStopTime": 10,
            "numberOfCars": 50,
            "note": "<script>alert('hacked!')</script>"
        }]
        self.assertTrue(validate_knitPublicReport(malicious_traffic_data))

if __name__ == '__main__':
    unittest.main()