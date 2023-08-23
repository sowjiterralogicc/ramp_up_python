import re
from ping3 import ping

def validate_ip(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    out = re.search(pattern, ip)
    if out:
        ip_address = out.group()
        split_data = ip_address.split(".")
        data = [i for i in split_data if int(i) <= 255]
        if len(data) == 4:
            return ip_address
    return None

def write_to_file(ip_file, ip, is_valid):
    with open(ip_file, "a") as f:
        if is_valid:
            f.write(f"Valid ip_address: {ip}\n")
        else:
            f.write(f"Non-valid ip_address: {ip}\n")

def process_ip(ip):
    response_time = ping(ip, timeout=5)
    if response_time is not None:
        write_to_file("ip_address.txt", ip, True)
        print("Valid IP address:", ip)
    else:
        write_to_file("ip_address.txt", ip, False)
        print("Non-valid IP address:", ip)

while True:
    user_choice = input("Do you want to enter an IP? (Yes/No): ").strip().lower()

    if user_choice == "yes":
        input_ip = input("Enter an IP: ")
        validated_ip = validate_ip(input_ip)
        if validated_ip:
            process_ip(validated_ip)
        else:
            print("Invalid IP format.")

    elif user_choice == "no":
        break

    else:
        print("Invalid choice. Please enter Yes or No.")

with open("ip_address.txt", "r") as f:
    print(f.read())




