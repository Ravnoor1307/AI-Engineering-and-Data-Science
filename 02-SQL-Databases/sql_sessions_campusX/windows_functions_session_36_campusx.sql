use task_campux;
 SELECT * from marks;
 
 # avg marks of each branch
 SELECt *,
AVG(marks) OVER(Partition by (branch)) as branch_avg_marks
 FROM task_campusx.marks;

# marks greater than respective branch's avg marks
SELECT * FROM (SELECt *,
AVG(marks) OVER(Partition by (branch)) as branch_avg_marks
 FROM task_campusx.marks) as t
 WHERE marks > branch_avg_marks;

# overall rank of students in descending marks
SELECT *, 
RANK() OVER(ORDER BY marks DESC) as rank_student
from  task_campusx.marks;

# rank and dense_rank branch wise

SELECT *, 
RANK() OVER(PARTITION BY (branch) ORDER BY marks DESC) as rank_student,
DENSE_RANK() OVER(PARTITION BY (branch) ORDER BY marks DESC) as dense_rank_student
from  task_campusx.marks;


# Find top 2 most paying customers of each month
select user_id,SUM(amount) as total_spent,
MONTHNAME(date) as months,
RANK() OVER(PARTITION BY (MONTHNAME(date)) ORDER BY SUM(amount) DESC) as user_rank
FROM orders
GROUP BY MONTHNAME(date),user_id;

SELECT * from (select user_id,SUM(amount) as total_spent,
MONTHNAME(date) as months,
RANK() OVER(PARTITION BY (MONTHNAME(date)) ORDER BY SUM(amount) DESC) as user_rank
FROM orders
GROUP BY MONTHNAME(date),user_id) as t1
WHERE t1.user_rank <3
ORDER BY t1.months DESC,user_rank;

# name of students with highest marks of any student

SELECT *,
FIRST_VALUE(name) OVER (ORDER BY marks DESC) as highest_marks
from task_campusx.marks;

SELECT *,
LAST_VALUE(marks) OVER (ORDER BY marks DESC ROWS BETWEEN  UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as highest_marks
from task_campusx.marks;

# 2nd topper using nth value:

SELECT *,
NTH_VALUE(name,2) OVER (PARTITION BY branch ORDER BY marks DESC 
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as 2nd_topper
from task_campusx.marks;

# name and branch of only toppers
SELECT name,branch,marks from 
  (SELECT *,
  FIRST_VALUE(name) OVER (PARTITION BY branch ORDER BY marks DESC) as topper,
  FIRST_VALUE(marks) OVER (PARTITION BY branch ORDER BY marks DESC) as marks_topper
  from task_campusx.marks) as 
table1
WHERE table1.name=table1.topper;

# name and branch of lowest marks
SELECT name,branch,marks from 
  (SELECT *,
  LAST_VALUE(name) OVER (PARTITION BY branch ORDER BY marks DESC
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as topper,
  LAST_VALUE(marks) OVER (PARTITION BY branch ORDER BY marks DESC
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as marks_topper
  from task_campusx.marks) as 
table1
WHERE table1.name=table1.topper;

#### OR

SELECT name,branch,marks from 
  (SELECT *,
  LAST_VALUE(name) OVER w as topper,
  LAST_VALUE(marks) OVER w as marks_topper
  from task_campusx.marks
  WINDOW w AS (PARTITION BY branch ORDER BY marks DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING))as 
table1
WHERE table1.name=table1.topper;

## USING LAG AND LEAD

SELECT MONTHNAME(date) as monthname,SUM(amount) as revenue,
((SUM(amount) - LAG(SUM(amount)) OVER())/LAG(SUM(amount)) OVER())*100 as mom_growth
FROM orders
GROUP BY MONTHNAME(date);