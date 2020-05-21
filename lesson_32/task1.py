#   Task 1
#
# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests
from bs4 import BeautifulSoup
import urllib.robotparser


url = 'https://twitter.com/robots.txt'
def read_robots_file():
    rp = urllib.robotparser.RobotFileParser()  # This class provides methods to read, parse and answer questions about the robots.txt file at url.
    rp.set_url(url)  # Sets the URL referring to a robots.txt file.
    rp.read()  # Reads the robots.txt URL and feeds it to the parser.

    # Returns True if the useragent is allowed to fetch the url according to the rules contained in the parsed robots.txt file.
    return rp.can_fetch("*", url)

def client_request():
    page = requests.get(url)
    status = page.status_code   # This class of status code indicates that the client's request
                                # was successfully received, understood, and accepted.
    if status >= 200 and status <= 400:
        soup = BeautifulSoup(page.text, 'html.parser')
        print(soup.prettify())
        with open("robots.txt", "w", encoding=page.encoding) as f:
            f.write(page.text)
    else:
        raise "Error Status Code"
    return status

if __name__=="__main__":

    read = read_robots_file()
    if read == True:
        print("Useragent is ALLOWED to fetch the url according to the rules contained in the parsed robots.txt file")
        client_request()
    else:
        print("Useragent is DISALLOWED to fetch the url according to the rules contained in the parsed robots.txt file")