#  reading a file
# f= open("file1.txt","rb") #r for reading(it's default b/w), A for appending,W for writing(rb means read in binary)
# # f = open("file2.txt","x") to ceate a file we use 'x'
# # f = open('myfile.txt',"w")
# # print(f)
# text = f.read()
# print(text)
# f.close()
# writing into a file
# f = open("myfile.txt","w")
# f.write("hellow devansh")
# f.close() #it clears out everything in there
# APPENDING TO A FILE
# f = open("myfile.txt","a")
# f.write(" hellow devansh")
# f.close() #don't forget to close the files
# a = None
# with open("myfile.txt","w") as f :
#     f.write("hey this is another way to write things")
f = open("file1.txt",'r')
i = 0
while True:
    line = f.readline()
    if not line:
        break
    i = i+1
    m2 = line.split(",")[1]
    m1 = line.split(",")[0]
    m3 = line.split(",")[2]
    print(f"The Student {i} in maths is {m1}")
    print(f"The Student {i} in Physics is {m2}")
    print(f"The Student {i} in chemistry is {m3}")

    print(line)
f.close()

f = open("iterable.txt","w")
lines = ["line1\n","line2\n","line3\n","line4\n"]
f.writelines(lines)
f.close()