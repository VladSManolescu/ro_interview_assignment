import ipaddress
import socket
import struct

from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network: ipaddress.IPv4Network, raw_entry_list: list):
        self.ipv4_network = ipv4_network
        self.entries = []
        for entry in raw_entry_list:
            self.entries.append(Entry(entry["address"], entry["available"], entry["last_used"]))

        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        pass

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        netw = int(self.ipv4_network.network_address)
        mask = int(self.ipv4_network.netmask)
        ok = False
        while not ok:
            ok = True
            for index, entry in enumerate(self.entries):
                try:
                    a = int(ipaddress.ip_address(entry.address))
                    a = struct.unpack('!I', socket.inet_aton(entry.address))[0]
                    if not (a & mask) == netw:
                        print(f"\tIp address {entry.address} does not belong in the subnet and it will be deleted")
                        del self.entries[index]
                        ok = False
                    # if not ipaddress.IPv4Address(entry.address) in self.ipv4_network:
                    #     del self.raw_entry_list[index]

                except ValueError:
                    print(f"\tIp address {entry.address} is invalid and it will be deleted")
                    del self.entries[index]
                    ok = False



    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries)
        pass
