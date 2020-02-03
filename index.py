import requests
from bs4 import BeautifulSoup
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

#starttls() is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.
server.starttls()

#Next, log in to the server
server.login("gmail", "password)

msg = "Tech word is in Sky news"


page = requests.get("https://news.sky.com/technology")
soup = BeautifulSoup(page.content, "html.parser")
techWord = soup.find_all("h3", {"class": "sdc-site-tile__headline"})
for tWord in techWord:          # Print all occurrences
    #print(tWord.get_text())
    if "tech" in tWord.get_text():
        #print("Tech")
        server.sendmail("sender", "reciever", msg)
    else:
        print("not")