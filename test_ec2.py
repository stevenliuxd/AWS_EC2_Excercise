import unittest
import json
from ec2_functions import instance_report

first_resp = {
    "instances": [
        {
            "Instance ID": "i-0e85d4a77301ec602",
            "Name": "webserver 1",
            "Instance Type": "t1.micro",
            "Security Group IDs": [
                "sg-0d86fb90a180ef0aa"
            ]
        },
        {
            "Instance ID": "i-047ae0eea184a32a8",
            "Name": "database",
            "Instance Type": "t1.micro",
            "Security Group IDs": [
                "sg-00a99efae992dbd6e"
            ]
        }
    ]
}

class TestInstanceReport(unittest.TestCase):

    def test_instance_report(self):
        func_result = json.loads(instance_report()) # Convert to dict
        self.assertEqual(func_result, first_resp)
