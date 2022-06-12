import unittest
import warnings
from ec2_functions import instance_report, ingress_rules
from test_params.sample_responses import instance_response, rule_one_response, rule_two_response


def nowarn():
    warnings.filterwarnings(action="ignore", category=ResourceWarning) # Ignore resource warning for SSL. OPTIONAL


class TestEC2App(unittest.TestCase):

    def test_instance_report(self):
        
        nowarn()
        response = instance_report()
        self.assertEqual(response, instance_response)

    def test_ingress_rules(self):
        
        nowarn()
        self.assertEqual(ingress_rules('sg-00a99efae992dbd6e'), [rule_one_response, True])
        self.assertEqual(ingress_rules('sg-0d86fb90a180ef0aa'), [rule_two_response, False])
        self.assertEqual(ingress_rules('sg-doesnotexist'), [])
        self.assertEqual(ingress_rules(''), [])
        
        