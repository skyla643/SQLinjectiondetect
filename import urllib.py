import urllib.request
from urllib.parse import urlparse, urljoin
import re

def extract_links(url):
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        page_content = response.read().decode('utf-8')
        links = re.findall(r'href="(.*?)"', page_content)
        return links
    else:
        print("Error accessing:", url)
        return []

def check_vulnerabilities(url):
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        page_content = response.read().decode('utf-8')
        if re.search(r'jquery\.js\?ver=1\.12\.4', page_content):
            print("Vulnerability found: Outdated jQuery version detected on", url)
        if re.search(r'SQL error', page_content, re.IGNORECASE):
            print("Vulnerability found: Possible SQL Injection on", url)
    else:
        print("Error accessing:", url)

def vulnerability_scanner(start_url):
    visited_urls = set()
    queue = [start_url]

    while queue:
        url = queue.pop(0)
        visited_urls.add(url)

        print("Scanning:", url)
        links = extract_links(url)
        for link in links:
            absolute_link = urljoin(url, link)
            if absolute_link not in visited_urls and absolute_link.startswith(start_url):
                queue.append(absolute_link)
                check_vulnerabilities(absolute_link)

# REPLACE THE EXAMPLE BELOW WITH YOUR URL OR "LINK" OF CHOICE
start_url = "https://example.com"
vulnerability_scanner(start_url)
