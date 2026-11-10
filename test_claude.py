import requests

url = "http://ec2-35-88-109-159.us-west-2.compute.amazonaws.com:18001/v1/chat/completions"

payload = {
    "model":"ByteDance-Seed/UI-TARS-1.5-7B",  # "sonnet4", #"sonnet37v1",
    "messages": [
        {"role": "user", "content": "What's the difference between Claude 3.5 and GPT-4o?"}
    ],
    "temperature": 0.7
}

response = requests.post(url, json=payload)
print(response.json())