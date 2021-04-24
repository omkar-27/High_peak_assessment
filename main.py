mdict={}
a_dictionary = {}
a_file = open("sample_input.txt")
out_file = open("output.txt","w+")
for line in a_file:
    key, value = line.split(":")
    value=int(value)



    a_dictionary[key] = value
#print(a_dictionary)
n=a_dictionary["Employee"]
del a_dictionary["Employee"]

k=sorted(a_dictionary.values())
min=999999


for i in range(len(k)-n-1):
    if k[i+n-1]-k[i]<min:
        min=k[i+n-1]-k[i]
        m=i

for c in range(n):
    for i,j in a_dictionary.items():
        if j==k[m+c]:
            out_file.write('%s:%s\n'%(i,j))
x="difference between highest and lowest price goodie is " + str(min)
out_file.write(x)



