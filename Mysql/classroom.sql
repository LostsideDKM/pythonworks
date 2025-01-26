CREATE DATABASE collage; 
USE collage;
CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR(50),
 marks INT NOT NULL,
 grade VARCHAR(1),
 city VARCHAR(30)
);
INSERT INTO student
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
(110,"muqeed",23,"B","surat");

