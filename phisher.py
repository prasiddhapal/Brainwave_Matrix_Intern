import re
import requests
from urllib.parse import urlparse

# List of suspicious words often used in phishing URLs
MALICIOUS_DOMAINS = ["phishing.com", "malicious-site.net", "fake-login.org"]

def is_suspicious_keyword(url):
    # Check for suspicious keywords in the URL
    keywords = ["login", "verify", "update", "secure", "account", "bank", "signin"]
    return any(keyword in url.lower() for keyword in keywords)

def is_https(url):
    return urlparse(url).scheme == "https"

def is_malicious_domain(url):
    domain = urlparse(url).netloc
    return any(mal_domain in domain for mal_domain in MALICIOUS_DOMAINS)

def is_long_url(url, max_length=75):
    return len(url) > max_length

def scan_url_with_virustotal(api_key, url):

    api_url = f"https://www.virustotal.com/api/v3/urls"
    encoded_url = requests.utils.quote(url, safe='')
    headers = {"x-apikey": api_key}
    response = requests.post(api_url, headers=headers, data={"url": url})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def phishing_link_scanner(url, virustotal_api_key=None):
    results = {
        "long_url": is_long_url(url),
        "suspicious_keywords": is_suspicious_keyword(url),
        "https": is_https(url),
        "malicious_domain": is_malicious_domain(url),
    }

    # Check if the URL is too long
    if virustotal_api_key:
        vt_results = scan_url_with_virustotal(virustotal_api_key, url)
        if vt_results:
            results["virustotal"] = vt_results

    # Check if the URL is flagged by VirusTotal
    is_phishing = (
        results["long_url"]
        or results["suspicious_keywords"]
        or not results["https"]
        or results["malicious_domain"]
    )

    results["is_phishing"] = is_phishing
    return results

# Example usage
if __name__ == "__main__":
    test_url = input("Enter the URL to scan: ")
    # Replace with your actual VirusTotal API key
    vt_api_key = None  
    scan_results = phishing_link_scanner(test_url, virustotal_api_key=vt_api_key)
    print("\nScan Results:")
    for key, value in scan_results.items():
        print(f"{key}: {value}")
print("Thank you so much for trying out our service!")       
print("Created by @Prasiddha Pal")        
