import requests
BASE="http://127.0.0.1:5000/"
data=[{"likes":1000,"name":"abhishek","views":10000},
      {"likes":10,"name":"guru","views":100},
      {"likes":50,"name":"munni","views":1000}]
#response=requests.put(BASE + "video/1",{"name":"baby song","views":10000,"likes":100})
for i in range(len(data)):
    response=requests.put(BASE + "video/"+str(i),data[i])
    print(response.json())

input()
response=requests.delete(BASE + "video/2")
print(response)
