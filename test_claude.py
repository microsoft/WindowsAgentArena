import requests

url = "http://localhost:18000/v1/chat/completions"

payload = {
    "model":"Qwen/Qwen2.5-VL-72B-Instruct",  # "sonnet4", #"sonnet37v1",
    "messages": [
        {"role": "user", "content": "What's the difference between Claude 3.5 and GPT-4o?"}
    ],
    "temperature": 0.7
}

response = requests.post(url, json=payload)
print(response.json())