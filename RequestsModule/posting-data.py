import requests


my_data = {'name': 'Shock', 'email': 'shock@test.com'}
r = requests.post("http://httpbin.org/post", data = my_data)

print(r.status_code)
print(r.text)

f = open("myfile.html", "w+")
f.write(r.text)