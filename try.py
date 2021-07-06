import requests

x = requests.get("http://127.0.0.1:5000/login", json={"user_name": "Onur Sefa",
                                                              "password": "sifre"})
print(x)
print(x)