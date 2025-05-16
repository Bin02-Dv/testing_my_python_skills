import qrcode
from wifi_password import password

ssid = "Airtel_X25A_469F_5G"
password = password

security = "WPA"


wifi_data = f"WIFI:T:{security};S:{ssid};P:{password}"

qr = qrcode.make(wifi_data)

qr.save("wifi_qr.png")

print("WIFI QR Code generated successfully as wifi_qr.png")