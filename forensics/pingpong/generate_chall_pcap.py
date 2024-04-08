import base64
from scapy.all import IP, ICMP, TCP, send

def read_png_file(filename):
    with open(filename, "rb") as f:
        png_data = f.read()
    return png_data

def encode_base64(data):
    return base64.b64encode(data)

def send_http_request(dest_ip, method="GET"):
    sport = 12345  # Source port for TCP connection
    dport = 80     # HTTP port
    seq = 1000     # Sequence number
    http_request = (
        f"{method} / HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    packet = IP(dst=dest_ip)/TCP(sport=sport, dport=dport, seq=seq)/http_request
    send(packet)

def send_icmp_packet(base64_data, dest_ip):
    for i in range(0, len(base64_data), 56):
        chunk = base64_data[i:i+56]
        packet = IP(dst=dest_ip)/ICMP()/chunk
        send(packet)

if __name__ == "__main__":
    png_filename = "flag.png"  # Replace with your PNG file name
    destination_ips = ["192.168.56.%d" % i for i in range(10, 23)]

    png_data = read_png_file(png_filename)
    base64_data = encode_base64(png_data)

    for dest_ip in destination_ips:
        send_http_request(dest_ip, method="GET")
        send_icmp_packet(base64_data, dest_ip)
        send_http_request(dest_ip, method="POST")
        send_http_request(dest_ip, method="HEAD")
