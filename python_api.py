#test python api calls
#
import requests

response = requests.get("https://boards.greenhouse.io/embed/job_board?for=subsplash&b=https%3A%2F%2Fwww.subsplash.com%2Fopenpositions")

print(response.text)