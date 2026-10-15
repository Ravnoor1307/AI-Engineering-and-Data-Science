show databases;
use mohitdb;
show tables;
DESC employee;
select * from employee;
INSERT INTO employee (firstname, lastname, salary, phoneno, location) VALUES ('kapil', 'sharma', 10000, 943345566, 'bangalore'),('rohit','kumar',20000,746353532,'saharsa'),('mohit','kumar',50000,986559,'patna'),('mohit',NULL,40000,83736578,'patna');
select * from employee;
select * from employee where location = 'patna';
select lastname AS 'title' from employee;
select firstname, salary, location, lastname as Title from employee;
UPDATE employee set lastname = 'kr' where (firstname = 'mohit' and salary = 40000);
select * from employee;
UPDATE employee set salary = salary + 700;
select * from employee;
ALTER table employee ADD COLUMN age INT NOT NULL;
select * from employee;
DESC employee;
ALTER TABLE employee MODIFY COLUMN location varchar(27) DEFAULT  'Bangalore';
desc employee;
# drop table students;
CREATE TABLE students(
student_id int,
student_fname varchar(30) NOT NULL,
student_lname varchar(40),
student_email varchar(40) NOT NULL,
student_phone BIGINT NOT NULL,
enrollment_date TIMESTAMP NOT NULL,
student_company varchar(30),
batch_date varchar(30) NOT NULL,
source_of_joining varchar(30) NOT NULL,
location varchar(30) NOT NULL DEFAULT 'BANGALORE',
course_no int NOT NULL DEFAULT 1,
PRIMARY KEY (student_id),
UNIQUE KEY (student_email),
UNIQUE KEY (student_fname,student_phone),
FOREIGN KEY (course_no) REFERENCES courses(course_id)
);

desc students;

ALTER table students ADD COLUMN years_of_experience int;

ALTER table students MODIFY COLUMN student_id int AUTO_INCREMENT ;

ALTER table students MODIFY COLUMN enrollment_date TIMESTAMP DEFAULT NOW() ;


INSERT INTO students (student_fname, student_lname,student_email,student_phone,student_company,batch_date,source_of_joining,location,years_of_experience,course_no)
VALUES
('rohit','sharma','rohit@gmail.com',91919191, 'walmart','05-02-2021','linkedin','bangalore',6,2),
('virat','kohli','virat@gmail.com',766719191, 'flipkart','05-02-2021','linkedin','hyderabad',3,3),
('shikhar','dhawan','shikhar@gmail.com',98767191, 'google','19-02-2021','linkedin','bangalore',12,1),
('rahul','dravid','rahul@gmail.com',98767191, 'walmart','19-02-2021','friends','patna',8,2),
('ms','dhoni','dhoni@gmail.com',456719191, 'google','19-07-2022','friends','ranchi',6,3),
('zaheer','khan','khan@femail.com',89867191, 'amazon','19-07-2022','newspapaer','patna',1,4),
('ashish','nehra','nehra@femail.com',87644191, 'ajio','08-02-2023','articles','secundrabad',12,1),
('virendra','sehwag','sehwag@rediffmail.com',78964419, 'cricket','31-01-2020','articles','multan',NULL,4);

select * from students;

# drop table students;

create table mohitdb.courses(
course_id int auto_increment,
course_name VARCHAR(15) NOT NULL,
course_duration int,
course_fee int,
PRIMARY KEY (course_id));

#drop table courses;
show tables;

desc courses;

INSERT INTO courses (course_name, course_duration, course_fee) VALUES 
('big data',6,50000),
('web development',3,70000),
('data science',6,80000),
('dev ops',1,80000);
select * from courses;
desc students;

select * from students ORDER BY years_of_experience;

select student_fname, student_lname, location, course_no from students where location like 'pat%' or location like 'ra%';
select student_fname, student_lname, course_no from students where student_fname like '__';

select count(*) from students;

select count(DISTINCT location) as dist_location from students;
select count(*) from students where batch_date like '%-2023';
select student_fname,location,student_company,count(*) from students GROUP BY student_company;
select student_company,count(*)from students GROUP BY student_company;
select location, student_company,count(*)from students GROUP BY location,student_company;
select MIN(years_of_experience) from students;
select student_fname, years_of_experience from students ORDER BY years_of_experience LIMIT 1;
select student_company, years_of_experience from students ORDER BY student_company;
select student_company,SUM(years_of_experience) as total_exp from students GROUP BY student_company;
select student_company,ROUND(AVG(years_of_experience),2) as average_exp from students GROUP BY student_company;
select student_fname,student_lname,source_of_joining, student_company,years_of_experience from students WHERE years_of_experience between 8 and 12;
select student_fname,student_lname,source_of_joining, student_company,years_of_experience from students WHERE student_company in ('walmart','amazon','flipkart');
select student_fname,student_lname,source_of_joining, student_company,years_of_experience from students WHERE student_company NOT IN ('walmart','amazon','flipkart');

select student_id, student_fname, source_of_joining, student_company, years_of_experience,
CASE
WHEN years_of_experience < 4 THEN 'fresher'
WHEN years_of_experience BETWEEN 4 and 8 THEN 'Lead'
WHEN years_of_experience IS NULL THEN 'whoareyou'
ELSE 'MANAGER'
END AS 'POSITION' FROM students;
use mohitdb;
create table superhero(
id INT auto_increment,
superhero_name varchar(30) NOT NULL,
powers varchar(30),
villain varchar(40),
PRIMARY KEY (id),
unique (superhero_name)
);

desc superhero;

insert into superhero (superhero_name,powers,villain) 
values
('superman','x-ray vision','lex luthor'),
('batman','fear','joker'),
('ironman','wealth','mandarin'),
('thor','hammer','hella'),
('captain america','shield','red skull'),
('dr strange','magic','dormamu'),
('green lantern','ring','sinestro'),
('green arrow','arrow','merlin');

select * from superhero;

create table identity(
sup_id INT auto_increment,
superhero varchar(30) NOT NULL,
realname varchar(30) NOT NULL,
comics varchar (10),
PRIMARY KEY (sup_id)
);

desc identity;

INSERT INTO identity (superhero, realname, comics)VALUES
('superman','clark kent','dc'),
('batman','bruce wayne','dc'),
('ironman','tony stark','marvel'),
('captain america','steve rogers','marvel'),
('green lantern','hal jordan','dc'),
('spiderman','peter parker','marvel'),
('green arrow','oliver queen','dc'),
('hulk','bruce banner','marvel'),
('wonder woman','diana prince','dc');
select * from identity;



SELECT * from superhero 
LEFT JOIN identity ON superhero.superhero_name = identity.superhero
UNION
SELECT * from superhero
RIGHT JOIN identity ON superhero.superhero_name = identity.superhero;

select * from superhero CROSS JOIN identity;

SELECT *
FROM identity AS e1
JOIN identity AS e2
ON e1.superhero != e2.superhero;

select comics, count(*) as total from identity GROUP BY comics;
select * from students;
select student_fname, student_company, source_of_joining,course_no,years_of_experience from students where years_of_experience > 3;
select source_of_joining , count(*) as number from students where years_of_experience > 6 GROUP BY source_of_joining;

select location, count(location) as total, avg(salary) from employee GROUP BY location;
select student_fname, source_of_joining , count(*) as number from students where years_of_experience > 6 GROUP BY source_of_joining HAVING number >1;

select location, count(location) as total, avg(salary) from employee GROUP BY location;

select student_fname,student_lname, years_of_experience, row_number() OVER (order by years_of_experience desc) as ranking_exp from students;

select * from (select student_fname,student_lname, years_of_experience, row_number() OVER (order by years_of_experience desc) as ranking_exp from students)
temptable where ranking_exp = 5;

SELECT student_fname, student_lname, location, years_of_experience, row_number() OVER 
(PARTITION by location ORDER BY years_of_experience DESC) AS ranking_exp
FROM students;
SELECT * from 
(SELECT student_fname, student_lname, location, years_of_experience, row_number() OVER 
(PARTITION by location ORDER BY years_of_experience DESC) AS ranking_exp
FROM students) temptable where ranking_exp=1 ;

SELECT student_fname,student_lname, years_of_experience, 
row_number() 
OVER (ORDER BY years_of_experience DESC) AS row_num from students;

SELECT student_fname, student_lname, location, years_of_experience, RANK() over(ORDER BY years_of_experience DESC) as ranking from students;

SELECT student_fname, student_lname, location, years_of_experience, dense_rank() over(ORDER BY years_of_experience DESC) as dense_ranking from students;

SELECT student_fname, student_lname, students.location, total_count, average_experience from students 
JOIN 
(select location, count(location) as total_count, avg(years_of_experience) as average_experience from students GROUP BY location)
temptable on students.location = temptable.location;

SELECT student_fname, student_lname, location, COUNT(location) OVER (PARTITION BY location) as total_students,
avg(years_of_experience)  OVER (PARTITION BY location) AS avg_exp from students;

use mohitdb;

CREATE TABLE relations(
member_id varchar(10),
name varchar(20),
age int NOT NULL default 20,
parent_id varchar(10)
);

desc relations;

INSERT INTO relations(member_id, name,age,parent_id) 
VALUES
('F1','Pam',4,'F5'),
('F2','Dwight',10,'F5'),
('F3','Stanley',12,'F5'),
('F4','Micheal',36,NULL),
('F5','Angela',40,'F6'),
('F6','Kelly',70,NULL),
('F7','Jim',6,'F4'),
('F8','Ryan',8,'F4');

select * from relations;

select child.member_id as parent_id, child.name as parent_name, child.age as parent_age ,parent.name as child_name,parent.age as child_age
FROM relations as child
JOIN
relations as parent
ON child.member_id = parent.parent_id;

# ---------------------------------------SELF JOIN-----------------------------------------------------------------------------------
select child.member_id as child_id, child.name as child_name, child.age as child_age, parent.name as parent_name, parent.age as parent_age, child.parent_id as parent_id
from relations as child
JOIN
relations as parent
ON child.parent_id = parent.member_id;

select child.member_id as child_id, child.name as child_name, child.age as child_age, parent.name as parent_name, parent.age as parent_age, child.parent_id as parent_id
from relations as child
LEFT JOIN
relations as parent
ON child.parent_id = parent.member_id
WHERE parent.member_id is NOT NULL;


select student_id, source_of_joining,years_of_experience,
lag(years_of_experience, 2, 0) over (partition by source_of_joining order by student_id) as previous_yoe
from students
;

select student_id, source_of_joining,years_of_experience,
LEAD(years_of_experience) over (partition by source_of_joining order by student_id) as previous_yoe
from students
;

select student_id, source_of_joining,years_of_experience,
LEAD(years_of_experience, 2,0) over (partition by source_of_joining order by student_id) as previous_yoe
from students
;

select student_id, student_fname, location,source_of_joining,years_of_experience, 
first_value(years_of_experience) over (partition by source_of_joining order by years_of_experience desc ) as most_experienced
from students;

select student_id, student_fname, location,source_of_joining, years_of_experience,
last_value(years_of_experience) 
over (partition by source_of_joining order by years_of_experience desc 
range between unbounded preceding and unbounded following)  as least_experienced
from students;

select student_id, student_fname, location,source_of_joining, years_of_experience,
nth_value(years_of_experience, 2) 
over (partition by source_of_joining order by years_of_experience desc 
range between unbounded preceding and unbounded following)  as 2nd_most_experienced
from students;

select *,
case
when x.ntile_groups = 1 then 'Experienced Student'
when x.ntile_groups = 2 then 'Inexperienced Student'
END experience_category
from(
select student_id, student_fname, location,source_of_joining, years_of_experience,
ntile(2) over (order by years_of_experience desc) as ntile_groups from students
where source_of_joining = 'linkedin') x;


select student_id, student_fname, location,source_of_joining, years_of_experience,
cume_dist() over (partition by source_of_joining order by years_of_experience desc) as cume_distri
from students;

select *
from (
select student_id, student_fname, location,source_of_joining, years_of_experience,
round(cume_dist() over (partition by source_of_joining order by years_of_experience desc),3) as cume_distri
from students
) x
where x.cume_distri between 0.35 and 0.9;


select *
from (
  select student_id, student_fname, location, source_of_joining, years_of_experience,
  round(cume_dist() over (partition by source_of_joining order by years_of_experience desc),3) as cume_distri
  from students
) x
where x.cume_distri <=35;


select student_id, student_fname, location,source_of_joining, years_of_experience,
round(percent_rank() over (partition by source_of_joining order by years_of_experience desc),3) as cume_distri
from students;

use mohitdb;

CREATE TABLE test1 (
id INT auto_increment,
city_name VARCHAR(30),
PRIMARY KEY (id)
);

INSERT into test1(city_name) VALUES
('pak'),
('INDIA'),
('SYDNEY'),
('CHINA'),
('AUS'),
('USA'),
('pak'),
('bengal'),
('BIHAR'),
('BIHAR');

select MAX(LENGTH(city_name)) from test1;