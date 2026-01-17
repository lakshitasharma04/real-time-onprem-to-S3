import time
import random
from datetime import datetime
import os

BASE_PATH = "../onprem-stream-data"

def write_file(folder, prefix, content):
    filename = f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(BASE_PATH, folder, filename)
    with open(path, "w") as f:
        f.write(content)

while True:
    write_file(
        "transactions",
        "order",
        f"OrderID={random.randint(1000,9999)}, Amount={random.randint(100,5000)}"
    )

    write_file(
        "inventory",
        "stock",
        f"ItemID={random.randint(1,100)}, Qty={random.randint(1,50)}"
    )

    write_file(
        "audit",
        "log",
        f"Update at {datetime.now()}"
    )

    print("Generated new SAP-like records")
    time.sleep(30)
