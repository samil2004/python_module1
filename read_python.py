##"reading a file using python"
file=open("sample.txt","r")
x=file.read()
print(x)
file.close()
with open("hello.txt","r") as file:
    x=file .read()
    print(x)