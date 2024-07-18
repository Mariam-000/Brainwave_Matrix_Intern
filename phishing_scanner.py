import requests
import tldextract
import Levenshtein

# List of legitimate domains
legit_domains = ["example.com", "google.com", "facebook.com"]

def is_phishing(url):
    # Extract the domain from the URL
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # Check similarity with legitimate domains
    for legit in legit_domains:
        if Levenshtein.distance(domain, legit) < 3:  # Adjust the threshold as needed
            return False
    return True

def check_url_safety(url):
    api_url = "https://api.urlchecker.com/check"  # Replace with actual API endpoint
    params = {"url": url}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        result = response.json()
        if result.get("safe"):
            return "safe"
        else:
            return "unsafe"
    else:
        return "error"

# Main function to check URLs
def main():
    urls = [
        "http://example.com",
        "http://goog1e.com",
        "http://faceb00k.com",
        "http://phishingsite.com"
    ]
    
    for url in urls:
        safety_status = check_url_safety(url)
        if safety_status == "error":
            print(f"Error checking {url}.")
        elif safety_status == "unsafe" or is_phishing(url):
            print(f"{url} is a potential phishing link.")
        else:
            print(f"{url} is safe.")

if __name__ == "__main__":
    main()

