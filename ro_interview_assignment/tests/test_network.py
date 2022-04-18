import ipaddress
import unittest
import json

import data_structures
from data_structures.network_collection import NetworkCollection


class TestNetworkCollection(unittest.TestCase):
    # test valid ips
    def test_valid_ips(self):

        with open("/home/vlad/Downloads/SDN Python Developer_latest/ro_interview_assignment/tests/network_response.json") as f:
            text = json.loads(f.read())

        with open("/home/vlad/Downloads/SDN Python Developer_latest/ro_interview_assignment/tests/network_valid.json") as f:
            valid_tests = json.loads(f.read())

        network = NetworkCollection(ipv4_network=ipaddress.IPv4Network("192.168.0.0/24"), raw_entry_list=text)

        self.assertAlmostEqual(NetworkCollection.remove_invalid_records(network), valid_tests)