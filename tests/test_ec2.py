import unittest
import json
import warnings
from ec2_functions import instance_report
from sample_responses import first_sample_resp


def nowarn():
    warnings.filterwarnings(action="ignore", category=ResourceWarning) # Ignore resource warning for SSL. OPTIONAL


class TestInstanceReport(unittest.TestCase):

    def test_instance_report(self):
        
        nowarn()
        response = instance_report()
        self.assertEqual(response, first_sample_resp)
        