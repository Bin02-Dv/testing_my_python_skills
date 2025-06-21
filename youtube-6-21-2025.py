import base64

message = "Top Secret: Project X Launches in 24h"

encoded = base64.b64encode(message.encode()).decode()
print("Encoded:", encoded)

decoded = base64.b64decode(encoded.encode()).decode()
print("Decoded:", decoded)