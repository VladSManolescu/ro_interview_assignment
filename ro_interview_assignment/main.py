from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter
from data_structures.network_collection import NetworkCollection
import requests as req
import time
import json
import datetime as dt


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    try:
        response = req.get(url=url)
        # check as integer !=200 or as string...depending on the API codes
        while not str(response.status_code).startswith("2") and max_retries != 0:
            response = req.get(url=url)
            time.sleep(delay_between_retries)
            max_retries -= 1
        if max_retries == 0:
            print(f"The max number of retries has been reached. Last response code was {response.status_code} with "
                  f"response:\n {response.text}")
            return {}
        else:
            return json.loads(response.text)

    except Exception as e:
        print(f"Exception on request:\n {e}")







def main():
    """
    Main entry to our program.
    """

    clusters = []
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    for dc in list(datacenters):
        Datacenter.remove_invalid_clusters(dc)
        for cluster_name in dc.cluster_dict:
            clusters.append(Cluster(cluster_name, dc.cluster_dict[f"{cluster_name}"]["networks"],
                                    dc.cluster_dict[f"{cluster_name}"]["security_level"]))

    for cluster in clusters:
        print(f"\nCurrent cluster: {cluster.name}")
        for network in cluster.network_dict:
            print(f"Starting to clean up and sort in {str(network.ipv4_network)}\n")
            NetworkCollection.remove_invalid_records(network)
            NetworkCollection.sort_records(network)
            print()

    # print(clusters)




if __name__ == '__main__':
    begin_time = dt.datetime.now()
    main()
    print(f"Duration of execution was {str(dt.datetime.now() - begin_time)}")
