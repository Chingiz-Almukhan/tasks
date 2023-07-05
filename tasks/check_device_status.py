import requests


def check_device_status(mac_address: str) -> bool:
    url = f"http://localhost:8000/device/check/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    return False


mac_address = "1234ABCD5678"
status = check_device_status(mac_address)

if status:
    print("The network device is powered on and accessible.")
else:
    print("The network device is not found or turned off.")
