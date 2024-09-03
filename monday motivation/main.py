import datetime as dt
import random
import smtplib

time_now = dt.datetime.now()
today = time_now.weekday()

with open("quotes.txt") as file:
    quote_list = file.readlines()

random_quote = random.choice(quote_list)

my_email = "sendingemail"
password = "apppassword"

if today == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Monday Motivation\n\n{random_quote}",
        )
