# Web Crawling Vulnerability Scanner

## How it Works

### Functions
1. **extract_links(url)**: Extracts all links from a webpage using regular expressions.
2. **check_vulnerabilities(url)**: Checks for outdated jQuery libraries and potential SQL injection vulnerabilities in the HTML content of a webpage.
3. **vulnerability_scanner(start_url)**: Orchestrates the scanning process by starting from a specified URL and recursively scanning all linked pages.

### Detailed Explanation
- **extract_links(url)**: Fetches the HTML content of a webpage using `urllib.request.urlopen()`, extracts all links from it using regular expressions, and returns them.
- **check_vulnerabilities(url)**: Fetches the HTML content of a webpage using `urllib.request.urlopen()`, searches for known vulnerabilities using regular expressions, and prints a message if any are found.
- **vulnerability_scanner(start_url)**: Initiates the vulnerability scanning process by starting from a specified URL, traversing all links within the same domain, and checking each page for vulnerabilities.

## How to Use

To use the vulnerability scanner, call the `vulnerability_scanner()` function with the initial URL as an argument.

## Example Output

### If Nothing is Found
If the vulnerability scanner does not find any vulnerabilities, the output will indicate that no vulnerabilities were found.

### If Something is Found
If the vulnerability scanner finds a vulnerability, it will print out a message indicating the vulnerability found, along with the URL where it was detected.

Love -
SMRCCC3301

