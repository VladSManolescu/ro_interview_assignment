import re


class Datacenter:
    def __init__(self, name: str, cluster_dict: list):
        self.name = name
        self.cluster_dict = cluster_dict
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        pass

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        # [A-Z]{3}-([\d]{3}|[\d]{2}|[\d]{1})
        for cluster_name in list(self.cluster_dict):
            if not re.match("[A-Z]{3}-([\d]{1,3})$", cluster_name):
                print(f"Invalid cluster name {cluster_name} must be deleted")
                del self.cluster_dict[f"{cluster_name}"]

