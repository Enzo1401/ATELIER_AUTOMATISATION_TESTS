import requests
import time
import storage

def run_api_tests():
    url = "https://api.agify.io?name=enzo"
    passed, failed, latencies = 0, 0, []

    for i in range(3):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=3)
            latency = (time.time() - start_time) * 1000
            latencies.append(latency)

            if response.status_code == 200: passed += 1
            else: failed += 1
            
            data = response.json()
            if isinstance(data.get('age'), (int, type(None))): passed += 1
            else: failed += 1
        except:
            failed += 1

    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    storage.save_run(passed, failed, round(avg_latency, 2))

if __name__ == "__main__":
    run_api_tests()
