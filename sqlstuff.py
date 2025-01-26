import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost" ,user = 'root',passwd = 'root',database = 'test')
if mycon.is_connected():
    print("Successfully connected to mysql database")
cursor = mycon.cursor()
cursor.execute("drop table student;")
cursor.execute("""CREATE TABLE student(
                rollno INT PRIMARY KEY,
                name VARCHAR(50),
                marks INT NOT NULL,
                grade VARCHAR(1),
                city VARCHAR(30)
                );""")
cursor.execute("USE test")
cursor.execute("""INSERT INTO student
(rollno,name,marks,grade,city)
VALUES -- guahati surat or jaipur
(101,"anil",23,"C","guahati"),
(102,"vijay",19,"A","guahati"),
(103,"soumya",19,"B","surat"),
(104,"devansh",30,"A","surat"),
(105,"ankit",32,"C","jaipur"),
(106,"anuradha",18,"C","jaipur"),
(107,"shailaish",19,"D","surat"),
(108,"manas",16,"A","guahati"),
(109,"suraj",35,"B","jaipur"),
(110,"muqeed",23,"B","surat");""")
query = cursor.execute("select * from student")
data = cursor.fetchall()
for row in data:
    print(row)
data2 = cursor.rowcount
print(data2)
mycon.commit()
mycon.close()

# print(data)
# cursor.execute("drop table student;")