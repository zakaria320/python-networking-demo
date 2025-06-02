"""
Short Python Networking Demo - Perfect for 10-minute presentation
Based on GeeksforGeeks Socket Programming Tutorial
Source: https://www.geeksforgeeks.org/socket-programming-python/
"""

import socket
import requests

print("PYTHON NETWORKING LIBRARIES DEMO")
print("=" * 40)

# PART 1: REQUESTS LIBRARY (Web requests)
print("\n1. REQUESTS LIBRARY - Check website status")
print("-" * 25)

websites = ["https://www.google.com", "https://www.github.com"]

for site in websites:
    try:
        response = requests.get(site, timeout=3)
        print(f"✓ {site} - Status: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"✗ {site} - Failed")

# PART 2: SOCKET LIBRARY (Network connections)
print("\n2. SOCKET LIBRARY - Connect to Google")
print("-" * 25)

try:
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get Google's IP address
    google_ip = socket.gethostbyname('www.google.com')
    print(f"✓ Google's IP: {google_ip}")

    # Connect to Google (port 80 = web)
    s.connect((google_ip, 80))
    print("✓ Connected to Google successfully!")
    s.close()

except Exception as e:
    print(f"✗ Connection failed: {e}")

# PART 3: NETWORK INFO
print("\n3. NETWORK INFORMATION")
print("-" * 25)

# Get local computer info
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Your computer: {hostname}")
print(f"Your IP: {local_ip}")

# Resolve website names to IP addresses
sites = ['www.python.org', 'www.stackoverflow.com']
for site in sites:
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} → {ip}")
    except socket.gaierror:
        print(f"{site} → Could not resolve")

print("\n" + "=" * 40)
print("DEMO COMPLETED!")
print("\nKEY TAKEAWAYS:")
print("• requests library = Easy web requests")
print("• socket library = Low-level networking")
print("• Python makes networking simple!")
