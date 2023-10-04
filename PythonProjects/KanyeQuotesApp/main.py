import requests
import datetime as dt
import smtplib
# response = requests.get(url="https://api.kanye.rest")
#
# response.raise_for_status()
# data = response.json()
my_email = ""
password = ""
now = dt.datetime.now()
wednesday = now.weekday()

response = requests.get(url=" https://uselessfacts.jsph.pl//api/v2/facts/random")
response.raise_for_status()
data = response.json()
text = data["text"]
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg=f"Subject:Jouw dagelijkse weetje <3<3\n\n {text}"
    )
