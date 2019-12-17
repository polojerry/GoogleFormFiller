import requests

"""
Python script to help in filling google form from predefined data

"""

# replace https://docs.google.com/forms/d/e/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/viewform

url = "https://docs.google.com/forms/d/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/formResponse"

# the data to be inserted uses key:value pair. The key is the entry.XXX number and "" is tha data to be inserted
data = {
    'entry.XXXX': "value",
    'entry.XXXXX': "value "
}

try:
    requests.post(url, data)
except:
    print("Error")
else:
    print("Success")
