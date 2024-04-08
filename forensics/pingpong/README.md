# pingpong

In this directory are the files to make the challenge ([generate_chall_pcap.py](./generate_chall_pcap.py), [flag.png](./flag.png)), the challenge file ([traffic.pcap](./traffic.pcap)),  and the solution script ([solv.py](./solv.py))

This challenge involved exfiltrating the base64 data of an image in a pcap.

While this can be solved using wireshark and some manual labor, the easiest way to solve this is by using [scapy](https://scapy.net/) to read all the ICMP packets, get the load (the data), and then write the base64-decoded data to a file.
