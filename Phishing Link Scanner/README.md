
# Phishing Link Scanner 🔍

A lightweight Python-based tool to detect potentially malicious or phishing URLs using heuristic checks and optional integration with [VirusTotal](https://www.virustotal.com/).

## 🚀 About the Project

This project was developed by **Prasiddha Pal**, Intern at **Brainwave Matrix Solutions**, to explore cybersecurity techniques in detecting phishing attacks. The tool helps users evaluate suspicious URLs based on various criteria including domain patterns, suspicious keywords, HTTPS usage, and URL length.

## 🧠 Features

- ✅ Checks for suspicious keywords in URLs  
- 🔐 Verifies whether the URL uses HTTPS  
- 📏 Detects unusually long URLs  
- 🚫 Flags known malicious domains  
- 🧪 Integrates with VirusTotal API for in-depth scanning (optional)

## 🧑‍💻 Usage

Run the script with Python 3:

```bash
python phisher.py
```

You'll be prompted to enter a URL to scan. Optionally, you can provide a VirusTotal API key in the script to enable external scanning.

## 🔑 VirusTotal Integration

To use the VirusTotal API:

1. Sign up at [virustotal.com](https://www.virustotal.com) to get a free API key.
2. Replace the placeholder in the code:
   ```python
   vt_api_key = "your_api_key_here"
   ```

## 📝 Example Output

```
Enter the URL to scan: http://fake-login.org/account/verify
Scan Results:
long_url: True
suspicious_keywords: True
https: False
malicious_domain: True
is_phishing: True
Thank you so much for trying out our service!
Created by @Prasiddha Pal
```

## 📁 File Structure

```
phisher.py          # Main phishing scanner script
README.md           # Project documentation
```

## 📜 License

This project is for educational purposes and internal research. Not intended for commercial use without permission.
