"""
用来统计ip的c段



"""

file = "ip.txt"
result = []

with open(file,"r+") as f:
    data = f.readlines()
    f.close()

for i in data:
    a = ""
    i = i.strip()
    i = i.split(".")
    a+=i[0]+"."
    a+=i[1]+"."
    a+=i[2]
    if a not in result:
        result.append(a)
for i in result:
    print(i)