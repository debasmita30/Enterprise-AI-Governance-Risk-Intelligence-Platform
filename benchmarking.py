import time
import requests

def benchmark_api(url, payload):

    start = time.time()
    try:
        response = requests.post(url, json=payload, timeout=10)
        latency = time.time() - start
        status = response.status_code
    except:
        latency = None
        status = "Failed"

    return {
        "latency_seconds": latency,
        "status": status
    }