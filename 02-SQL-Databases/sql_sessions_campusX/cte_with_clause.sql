use mohitdb;


-- Create the table
## CREATE TABLE emp_test (
    ## emp_id INT PRIMARY KEY,
    ## emp_name VARCHAR(50),
    ## dept_name VARCHAR(50),
    ## salary DECIMAL(10, 2)
## );

-- Insert sample data
## INSERT INTO emp_test (emp_id, emp_name, dept_name, salary)
## VALUES
    ## (1, 'John Doe', 'Engineering', 75000.00),
    ## (2, 'Jane Smith', 'Sales', 35000.00),
    ## (3, 'Michael Johnson', 'Marketing', 42000.00),
    ## (4, 'Emily Williams', 'Finance', 65000.00),
    ## (5, 'William Brown', 'HR', 29000.00),
    ## (6, 'Olivia Davis', 'Engineering', 82000.00),
    ## (7, 'James Wilson', 'Sales', 41000.00),
    ## (8, 'Sophia Lee', 'Marketing', 57000.00),
    ## (9, 'Robert Taylor', 'Finance', 90000.00),
    ## (10, 'Emma Anderson', 'HR', 25000.00),
    ## (11, 'Liam Martinez', 'Engineering', 78000.00),
    ## (12, 'Ava Garcia', 'Sales', 39000.00),
    ## (13, 'Noah Rodriguez', 'Marketing', 48000.00),
    ## (14, 'Isabella Hernandez', 'Finance', 72000.00),
    ## (15, 'Ethan Moore', 'HR', 22000.00),
    ## (16, 'Mia Clark', 'Engineering', 86000.00),
    ## (17, 'Alexander White', 'Sales', 43000.00),
    ## (18, 'Abigail Hall', 'Marketing', 61000.00),
    ## (19, 'James Johnson', 'Finance', 88000.00),
    ## (20, 'Ella Martin', 'HR', 18000.00);

SELECT * from emp_test;

select *,
CASE WHEN salary > (AVG(salary) OVER()) THEN 'higher'
ELSE 'low'
END as higher_lower,
AVG(salary) OVER()  as oa 
from emp_test;

-- Insert duplicate sets of rows

INSERT INTO emp_test (emp_id, emp_name, dept_name, salary)
SELECT emp_id, emp_name, dept_name, salary
FROM employee
LIMIT 5;

-- Create the table
CREATE TABLE emp_data (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    dept_name VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert sample data with duplicates
INSERT INTO emp_data (emp_name, dept_name, salary)
VALUES
    ('John Doe', 'Engineering', 75000.00),
    ('Jane Smith', 'Sales', 35000.00),
    ('Michael Johnson', 'Marketing', 42000.00),
    ('Emily Williams', 'Finance', 65000.00),
    ('William Brown', 'HR', 29000.00),
    ('Olivia Davis', 'Engineering', 82000.00),
    ('James Wilson', 'Sales', 41000.00),
    ('Sophia Lee', 'Marketing', 57000.00),
    ('Robert Taylor', 'Finance', 90000.00),
    ('Emma Anderson', 'HR', 25000.00),
    ('Liam Martinez', 'Engineering', 78000.00),
    ('Ava Garcia', 'Sales', 39000.00),
    ('Noah Rodriguez', 'Marketing', 48000.00),
    ('Isabella Hernandez', 'Finance', 72000.00),
    ('Ethan Moore', 'HR', 22000.00),
    ('Mia Clark', 'Engineering', 86000.00),
    ('Alexander White', 'Sales', 43000.00),
    ('Abigail Hall', 'Marketing', 61000.00),
    ('James Johnson', 'Finance', 88000.00),
    ('Ella Martin', 'HR', 18000.00),
    ('John Doe', 'Engineering', 75000.00),
    ('Jane Smith', 'Sales', 35000.00),
    ('Michael Johnson', 'Marketing', 42000.00),
    ('Emily Williams', 'Finance', 65000.00),
    ('William Brown', 'HR', 29000.00);
    
    
SELECT * from emp_data;

### Fetch employees who earn more than average salary of all employees:

with average_salary(avg_sal) as
    (select avg(salary) from emp_data)
select *
 from emp_data as e, average_salary
 where e.salary > average_salary.avg_sal; 
 
--  CREATE TABLE store_inventory (
--     store_id INT PRIMARY KEY AUTO_INCREMENT,
--     store_name VARCHAR(50),
--     product VARCHAR(50),
--     quantity INT,
--     cost DECIMAL(10, 2)
-- );



-- -- Insert sample data
-- INSERT INTO store_inventory (store_name, product, quantity, cost)
-- VALUES
--     ('Apple Original 1', 'iPhone 11', 10, 699.99),
--     ('Apple Original 1', 'iPhone 12', 8, 799.99),
--     ('Apple Original 1', 'iPhone 13', 15, 899.99),
--     ('Apple Original 1', 'iPhone SE', 5, 399.99),
--     ('Apple Original 1', 'iPhone 13 Pro', 6, 1099.99),
--     ('Apple Original 2', 'iPhone 11', 12, 699.99),
--     ('Apple Original 2', 'iPhone 12', 7, 799.99),
--     ('Apple Original 2', 'iPhone 13', 18, 899.99),
--     ('Apple Original 2', 'iPhone SE', 3, 399.99),
--     ('Apple Original 2', 'iPhone 13 Pro', 9, 1099.99),
--     ('Apple Original 3', 'iPhone 11', 5, 699.99),
--     ('Apple Original 3', 'iPhone 12', 10, 799.99),
--     ('Apple Original 3', 'iPhone 13', 13, 899.99),
--     ('Apple Original 3', 'iPhone SE', 8, 399.99),
--     ('Apple Original 3', 'iPhone 13 Pro', 2, 1099.99),
--     ('Apple Original 4', 'iPhone 11', 9, 699.99),
--     ('Apple Original 4', 'iPhone 12', 6, 799.99),
--     ('Apple Original 4', 'iPhone 13', 11, 899.99),
--     ('Apple Original 4', 'iPhone SE', 4, 399.99),
--     ('Apple Original 4', 'iPhone 13 Pro', 7, 1099.99),
--     ('Apple Original 5', 'iPhone 11', 7, 699.99),
--     ('Apple Original 5', 'iPhone 12', 9, 799.99),
--     ('Apple Original 5', 'iPhone 13', 14, 899.99),
--     ('Apple Original 5', 'iPhone SE', 6, 399.99),
--     ('Apple Original 5', 'iPhone 13 Pro', 3, 1099.99),
--     ('Apple Original 1', 'iPhone 11', 8, 699.99),
--     ('Apple Original 1', 'iPhone 12', 7, 799.99),
--     ('Apple Original 1', 'iPhone 13', 12, 899.99),
--     ('Apple Original 1', 'iPhone SE', 6, 399.99),
--     ('Apple Original 1', 'iPhone 13 Pro', 5, 1099.99),
--     ('Apple Original 2', 'iPhone 11', 11, 699.99),
--     ('Apple Original 2', 'iPhone 12', 8, 799.99),
--     ('Apple Original 2', 'iPhone 13', 16, 899.99),
--     ('Apple Original 2', 'iPhone SE', 4, 399.99),
--     ('Apple Original 2', 'iPhone 13 Pro', 8, 1099.99);


# Apple Stores with sales greater than average sale of combined stores :

select * from store_inventory;
# doesnot works
-- select *,
-- SUM(quantity * cost) OVER (Partition by store_name) as sales_per_store,
-- ROUND(avg(quantity * cost) over(),2) as overall_avg
-- from store_inventory as t1
-- Having t1.sales_per_store > t1.overall_avg;

WITH CalculatedData AS (
    SELECT
        si.*,
        SUM(si.quantity * si.cost) OVER (PARTITION BY si.store_name) as sales_per_store,
        AVG(si.quantity * si.cost) OVER () as overall_avg
    FROM store_inventory si
)
SELECT *
FROM CalculatedData
WHERE sales_per_store > overall_avg;


-- CREATE TABLE iphone (
--     store_id INT,
--     store_name VARCHAR(50),
--     product VARCHAR(50),
--     quantity INT,
--     cost DECIMAL(10, 2)
-- );


-- Insert sample data
-- INSERT INTO iphone (store_id, store_name, product, quantity, cost)
-- VALUES
--     (1, 'Apple Original 1', 'iPhone 11', 10, 699.99),
--     (1, 'Apple Original 1', 'iPhone 12', 8, 799.99),
--     (1, 'Apple Original 1', 'iPhone 13', 15, 899.99),
--     (1, 'Apple Original 1', 'iPhone SE', 5, 399.99),
--     (1, 'Apple Original 1', 'iPhone 13 Pro', 6, 1099.99),
--     (2, 'Apple Original 2', 'iPhone 11', 12, 699.99),
--     (2, 'Apple Original 2', 'iPhone 12', 7, 799.99),
--     (2, 'Apple Original 2', 'iPhone 13', 18, 899.99),
--     (2, 'Apple Original 2', 'iPhone SE', 3, 399.99),
--     (2, 'Apple Original 2', 'iPhone 13 Pro', 9, 1099.99),
--     (3, 'Apple Original 3', 'iPhone 11', 5, 699.99),
--     (3, 'Apple Original 3', 'iPhone 12', 10, 799.99),
--     (3, 'Apple Original 3', 'iPhone 13', 13, 899.99),
--     (3, 'Apple Original 3', 'iPhone SE', 8, 399.99),
--     (3, 'Apple Original 3', 'iPhone 13 Pro', 2, 1099.99),
--     (4, 'Apple Original 4', 'iPhone 11', 9, 699.99),
--     (4, 'Apple Original 4', 'iPhone 12', 6, 799.99),
--     (4, 'Apple Original 4', 'iPhone 13', 11, 899.99),
--     (4, 'Apple Original 4', 'iPhone SE', 4, 399.99),
--     (4, 'Apple Original 4', 'iPhone 13 Pro', 7, 1099.99),
--     (5, 'Apple Original 5', 'iPhone 11', 7, 699.99),
--     (5, 'Apple Original 5', 'iPhone 12', 9, 799.99),
--     (5, 'Apple Original 5', 'iPhone 13', 14, 899.99),
--     (5, 'Apple Original 5', 'iPhone SE', 6, 399.99),
--     (5, 'Apple Original 5', 'iPhone 13 Pro', 3, 1099.99),
--     (1, 'Apple Original 1', 'iPhone 11', 8, 699.99),
--     (1, 'Apple Original 1', 'iPhone 12', 7, 799.99),
--     (1, 'Apple Original 1', 'iPhone 13', 12, 899.99),
--     (1, 'Apple Original 1', 'iPhone SE', 6, 399.99),
--     (1, 'Apple Original 1', 'iPhone 13 Pro', 5, 1099.99),
--     (2, 'Apple Original 2', 'iPhone 11', 11, 699.99),
--     (2, 'Apple Original 2', 'iPhone 12', 8, 799.99),
--     (2, 'Apple Original 2', 'iPhone 13', 16, 899.99),
--     (2, 'Apple Original 2', 'iPhone SE', 4, 399.99),
--     (2, 'Apple Original 2', 'iPhone 13 Pro', 8, 1099.99);
--     
select * from iphone;

# with clause () Apple Stores with sales greater than average sale of combined stores :

with Total_sales(store_id, store_name,total_sales_each_store) AS
                (select s.store_id,s.store_name,sum(s.quantity * s.cost) as total_sales_each_store
                from iphone as  s
                group by s.store_id,store_name),
                
      Avg_sales(avg_overall) AS (select ROUND(avg(total_sales_each_store),2) as avg_overall from Total_sales)
      
select * from
Total_sales as ts
join Avg_sales as av
on ts.total_sales_each_store > av.avg_overall; 


######################## VIEW() ########################


CREATE OR REPLACE VIEW iphone_sales AS
SELECT 
    store_name,
    SUM(3*cost) as thrice_cost,
    SUM(2*cost) as twice_cost,
    CONVERT(store_id, CHAR(255)) AS ids, 
    SUM(cost * quantity) AS total_sales
FROM 
    iphone
GROUP BY 
    store_id, store_name;


select * from iphone_sales;

UPDATE iphone_sales
SET store_name = 'Apple Original 1'
WHERE store_name = 'apple Original 1';

select * from iphone
WHERE cost < 799.99;

ALTER TABLE iphone
ADD column total_sales INT;

CREATE OR REPLACE VIEW iphone2 AS
SELECT *
FROM 
    iphone
WHERE cost < 799.99;

select * from iphone2;

insert into iphone2 
values(4,'apple original 24','iphone 27s',34,765.99,23456);

select * from iphone2;

select * from iphone
WHERE cost < 799.99;