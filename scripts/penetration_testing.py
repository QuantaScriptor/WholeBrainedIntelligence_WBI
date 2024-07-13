python
import requests

# Run penetration test
def run_penetration_test(url):
    response = requests.get(url)
    return response.status_code, response.text

# Example usage
if __name__ == "__main__":
    test_url = "http://localhost:8000"  # Replace with actual URL
    status_code, response_text = run_penetration_test(test_url)
    print(f"Status Code: {status_code}")
    print("Response Text:")
    print(response_text)
