--CREATE TABLE Students (
--    ID int NOT NULL,
--    LastName varchar(255) NOT NULL,
--    FirstName varchar(255),
--    PRIMARY KEY (ID)
--);
--CREATE TABLE Courses (
--    ID int NOT NULL,
--    Name varchar(255) NOT NULL,
--    PRIMARY KEY (ID)
--);
--CREATE TABLE RegisterCourse (
--    ID int NOT NULL,
--    StudentId int NOT NULL,
--    CourseId int NOT NULL,
--    PRIMARY KEY (ID),
--    FOREIGN KEY (StudentId) REFERENCES Students(ID),
--    FOREIGN KEY (CourseId) REFERENCES Courses(ID)
--);

--INSERT INTO Students
--VALUES (1, 'Naeem', 'Jahanzeb')

--SELECT * FROM Students;

--UPDATE Students
--SET lastname='Ashraf'
--WHERE id=1;

--DELETE from Students WHERE id=1;