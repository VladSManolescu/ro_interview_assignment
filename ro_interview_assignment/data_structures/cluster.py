import ipaddress
from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name: str, network_dict: dict, security_level: int):

        self.name = name
        self.network_dict = []
        for k in network_dict.keys():
            ip = ipaddress.IPv4Network(f"{k}")
            entries = network_dict[f"{k}"]
            self.network_dict.append(NetworkCollection(ip, entries))
        self.security_level = security_level

        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        pass
