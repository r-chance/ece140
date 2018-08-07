# Unseen University Suffers Growing Pains

We've been working our way up the full stack from environments to containers. So far you've used HTML and CSS. This assignment will get you use another very common container: a database server.

Mustrum Ridcully has been Archchancellor at Unseen University for nearly forty years. Since wizards' favourite sports traditionally are things like Competitive Eating and Extreme Napping other wizards find him very tiring to be around. He is not stupid but finds it very difficult to deal with unexpected information, and generally ignores it until it goes away or becomes someone else's problem. He holds the view that if someone is still trying to explain something to him after about two minutes, it must be worth listening to, and if they give up earlier, it was not worth bothering him with in the first place.

Ridcully's right-hand man is called Ponder Stibbons. He's effectively the only person who can get anything done (often without the consent of the other Faculty members). One day, having become aware of the sudden growth in enrollment of the university, Ponder Stibbons proclaimed that it was urgent that office of Admissions immediately acquire a database to manage the information related to all the incoming wizards.

Sadly -- that task now falls to you!

## Part 1 - Make Some Tables

This step is pretty easy, and it follows the table creation pattern we used in lecture. Unseen University staff have been keeping this information on a clipboard. You will create the following tables with the information included below.

For this step in the homework, you must turn in the SQL statements you used to create your tables. Be specific!

```
Users Table
+------------+-------------+--------+--------+------------+-----------------+
| Field      | Type        | Null   | Key    | Default    | Extra           |
+------------+-------------+--------+--------+------------+-----------------+
| id         | int(11)     | NO     | PRI    | NULL       | auto_increment  |
| firstname  | varchar(30) | NO     |        | NULL       |                 |
| lastname   | varchar(30) | NO     |        | NULL       |                 |
| age        | int(11)     | NO     |        | NULL       |                 |
| is_prof    | int(11)     | NO     |        | NULL       |                 |
+------------+-------------+--------+--------+------------+-----------------+

Rooms Table
+------------+-------------+--------+--------+------------+-----------------+
| Field      | Type        | Null   | Key    | Default    | Extra           |
+------------+-------------+--------+--------+------------+-----------------+
| id         | int(11)     | NO     | PRI    | NULL       | auto_increment  |
| roomname   | varchar(30) | NO     |        | NULL       |                 |
| capacity   | int(11)     | NO     |        | NULL       |                 |
+------------+-------------+--------+--------+------------+-----------------+

Courses Table
+------------+-------------+--------+--------+------------+-----------------+
| Field      | Type        | Null   | Key    | Default    | Extra           |
+------------+-------------+--------+--------+------------+-----------------+
| id         | int(11)     | NO     | PRI    | NULL       | auto_increment  |
| coursename | varchar(30) | NO     |        | NULL       |                 |
| prof_id    | int(11)     | NO     |        | NULL       |                 |
| room_id    | int(11)     | NO     |        | NULL       |                 |
+------------+-------------+--------+--------+------------+-----------------+

Enrollments Table
+------------+-------------+--------+--------+------------+-----------------+
| Field      | Type        | Null   | Key    | Default    | Extra           |
+------------+-------------+--------+--------+------------+-----------------+
| id         | int(11)     | NO     | PRI    | NULL       | auto_increment  |
| course_id  | int(11)     | NO     |        | NULL       |                 |
| student_id | int(11)     | NO     |        | NULL       |                 |
+------------+-------------+--------+--------+------------+-----------------+
```

## Part 2 - Load Some Data

Here is a simple list of all the data you need to load into your tables:

For this step in the homework, you must turn in the SQL statements you used to insert the given data into your tables. Be specific!
```
Users Table
+--------+-------------+-------------+----------+----------+
 | id     | firstname   | lastname    | age      | is_prof  |
 +--------+-------------+-------------+----------+----------+
 | 1      | tom         | jones       | 19       | 0        |
 | 2      | bill        | smith       | 21       | 0        |
 | 3      | kim         | possible    | 20       | 0        |
 | 4      | jessica     | rabbit      | 18       | 0        |
 | 5      | veronica    | mars        | 22       | 0        |
 | 6      | marge       | simpson     | 45       | 0        |
 | 7      | ramsin      | khoshabeh   | 30       | 1        |
 | 8      | rick        | gessner     | 55       | 1        |
 +--------+-------------+-------------+----------+----------+
 
 Rooms Table
  +--------+-------------+-------------+
 | id     | roomname    | capacity    |
 +--------+-------------+-------------+
 | 1      | alcatraz    | 25          |
 | 2      | rikers      | 35          |
 | 3      | sing-sing   | 80          |
 +--------+-------------+-------------+
 
 Courses Table
  +--------+-------------+------------+----------+
 | id     | coursename  | prof_id    | room_id  |
 +--------+-------------+------------+----------+
 | 1      | patterns    | 8          | 2        |
 | 2      | 3dvision    | 7          | 3        |
 +--------+-------------+------------+----------+
 
 Enrollments Table
 +--------+-------------+-------------+
 | id     | course_id   | student_id  |
 +--------+-------------+-------------+
 | 1      | 1           | 1           |
 | 2      | 1           | 2           |
 | 3      | 1           | 3           |
 | 4      | 2           | 4           |
 | 5      | 2           | 5           |
 | 6      | 2           | 6           |
 +--------+-------------+-------------+
```

## Part 3 - Write (and run) Some Queries

For this step in the homework, you must turn in the SQL statements you used to perform your queries against your tables, along with the output of the query results. Be specific!

1. Write a query to count to the total number of records in the Users table
2. Write a query to compute the average age of all the Users 
3. Write a query to count the students enrolled in the 3dvision course
4. Write a query to show the names of the students enrolled in the patterns course
5. Write a query to count the students enrolled in each course taught by each professor. Your answer for each course should include professor-name, course-name, and student count.

## NOTE

If you don't have a database installed on your computer (or in your VM), you may use an online mysql tool to complete this assignment. 
A good example of such a tool can be [found here](https://www.tutorialspoint.com/codingground.htm). From this website, choose MySQL to get an online virtual machine where you can do simple database programming exercises.

To turn in your homework, copy your scripts into the single .sql file in your assignment project directory. Follow the comments in the file to organize your queries.
