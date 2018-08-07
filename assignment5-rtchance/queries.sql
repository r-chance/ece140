/* Part 1 Queries below... */
/* Make Tables! */
create table Users(id int, firstname varchar(30), lastname varchar(30),age int,is_prof int);
create table Rooms(id int, roomname varchar(30), capacity int);
create table Courses(id int, coursename varchar(30),prof_id int, room_id int);
create table Enrollments(id int, course_id int, student_id int);

/* Part 2 Queries below */ 
/* Load data onto your tables! */
insert into Users values(1,'tom','jones',19,0);
insert into Users values(2,'bill','smith',21,0);
insert into Users values(3,'kim','possible',20,0);
insert into Users values(4,'jessica','rabbit',18,0);
insert into Users values(5,'veronica','mars',22,0);
insert into Users values(6,'marge','simpson',45,0);
insert into Users values(7,'ramsin','khoshabeh',30,1);
insert into Users values(8,'rick','gessner',55,1);

insert into Rooms values(1,'alcatraz',25);
insert into Rooms values(2,'rikers',35);
insert into Rooms values(3,'sing-sing',80);

insert into Courses values(1,'patterns',8,2);
insert into Courses values(2,'3dvision',7,3);

insert into Enrollments values(1,1,1);
insert into Enrollments values(2,1,2);
insert into Enrollments values(3,1,3);
insert into Enrollments values(4,2,4);
insert into Enrollments values(5,2,5);
insert into Enrollments values(6,2,6);

/* Part 3 Queries below */
/* Write a query to count to the total number of records in the Users table */
select count(*) from Users;

/* Write a query to compute the average of all the Users */
select avg(age) from Users;

/* Write a query to count the students enrolled in the 3dvision course */
select count(*) from Enrollments where course_id = 2;

/* Write a query to show the names of the students enrolled in the patterns course */
select Users.firstname, Users.lastname from Users inner join Enrollments on Users.id = Enrollments.student_id and Enrollments.course_id = 1;

/* Write a query to count the students enrolled in each course taught by each professor. Your answer for each course should include professor-name, course-name, and student count. */
select Users.firstname, Users.lastname, Courses.coursename, count(Courses.id) from Users inner join Courses on Users.id = prof_id inner join Enrollments on Courses.id =  Enrollments.course_id group by Users.firstname, users.lastname,courses.coursename,courses.id;
