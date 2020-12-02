# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
#test
import requests
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv
SECRET_KEY = os.getenv("SENDGRID_API_KEY")


import requests

response = requests.get("https://boards.greenhouse.io/embed/job_board?for=subsplash&b=https%3A%2F%2Fwww.subsplash.com%2Fopenpositions")


message = Mail(
    from_email='shawntompke@gmail.com',
    to_emails='info@topdogsites.com',
    subject='Hello There! :)',
    html_content=response.text)
try:
    sg = SendGridAPIClient(SECRET_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print()
    print(e)

print(SECRET_KEY)