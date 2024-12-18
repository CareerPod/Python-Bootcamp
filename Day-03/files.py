f=open("boot1.txt","w")
f.write("Welcome to Careerpod Python Bootcamp")
print(f.closed)
f.close()
print(f.closed)

#f=open("boot1.txt","a")
#f.write("\nLuffy")
#f.close()

#f=open("boot1.txt","r")
#print(f.read())
#f.close()

with open("./boot1.txt","r") as f:
    print(f.read())

print(f.closed)