import requests

data_dari_internet = requests.get("https://my-json-server.typicode.com/sslaia/katawaena/posts").json()

print()
print("Berikut adalah amaedola yang ditarik dari Internet")
print()

i = 0

while i < len(data_dari_internet):
  for amaedola in data_dari_internet:

    print("| " + str(i + 1) + ": " + amaedola['title'])

    i += 1

print()
print("Hanya begitu saja. \nSebelumnya saya pikir akan rumit. \nTernyata gampang banget!")
print('''
     _|_
      |
     _|_
    //_/\\
  __|  ||____
 ////////////\\
/////////////\\\\
|^^^^^^^^^^||+|
|  # # #   ||||
 ....    ....".
|||||||||||||||||
''')