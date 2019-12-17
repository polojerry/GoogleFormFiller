import requests

"""
Python script to help in filling google form from predefined data

"""

# replace https://docs.google.com/forms/d/e/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/viewform

url = "https://docs.google.com/forms/d/187uY6SQMZzOFvkp8vmsuh8jz_oVvZ6c2Dnsbn4-SOhM/formResponse"

# the data to be inserted uses key:value pair. The key is the entry.XXX number and "" is tha data to be inserted
data = {
    'entry.563148456': "Jeremiah Polo",
    'entry.511270756': "Peter Okello"
}

try:
    requests.post(url, data)
except:
    print("Error")
else:
    print("Success")
