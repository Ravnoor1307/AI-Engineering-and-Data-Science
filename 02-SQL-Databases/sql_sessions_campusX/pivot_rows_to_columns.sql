-- use mohitdb;

-- -- Create a table named 'test3' with columns: sales_date, customer_id, amount
-- CREATE TABLE test3 (
--     sales_date DATE,
--     customer_id VARCHAR(10),
--     amount DECIMAL(10, 2)
-- );

-- -- Generate and insert data into the 'test2' table
-- INSERT INTO test3 (sales_date, customer_id, amount)
-- SELECT
--     DATE_ADD(DATE_ADD('2021-01-01', INTERVAL seq.seq MONTH), INTERVAL FLOOR(RAND() * 28) DAY) AS sales_date,
--     CONCAT('cust-', FLOOR((seq.seq - 1) / 3) + 1) AS customer_id,
--     ROUND(RAND() * 1000, 2) AS amount
-- FROM
--     (SELECT 0 AS seq UNION ALL
--      SELECT 1 UNION ALL
--      SELECT 2 UNION ALL
--      SELECT 3 UNION ALL
--      SELECT 4 UNION ALL
--      SELECT 5 UNION ALL
--      SELECT 6 UNION ALL
--      SELECT 7 UNION ALL
--      SELECT 8 UNION ALL
--      SELECT 9 UNION ALL
--      SELECT 10 UNION ALL
--      SELECT 11 UNION ALL
--      SELECT 12 UNION ALL
--      SELECT 13 UNION ALL
--      SELECT 14 UNION ALL
--      SELECT 15 UNION ALL
--      SELECT 16 UNION ALL
--      SELECT 17 UNION ALL
--      SELECT 18 UNION ALL
--      SELECT 19 UNION ALL
--      SELECT 20 UNION ALL
--      SELECT 21 UNION ALL
--      SELECT 22 UNION ALL
--      SELECT 23 UNION ALL
--      SELECT 24 UNION ALL
--      SELECT 25 UNION ALL
--      SELECT 26 UNION ALL
--      SELECT 27 UNION ALL
--      SELECT 28 UNION ALL
--      SELECT 29 UNION ALL
--      SELECT 30 UNION ALL
--      SELECT 31 UNION ALL
--      SELECT 32 UNION ALL
--      SELECT 33 UNION ALL
--      SELECT 34 UNION ALL
--      SELECT 35) seq
-- ORDER BY
--     customer_id, sales_date;


-- UPDATE test3
-- SET customer_id = 'cust-4'
-- WHERE customer_id = 'cust-6';     


-- Check the generated data
SELECT * FROM test3;

SELECT DISTINCT customer_id,monthname(sales_date),
SUM(amount) OVER(PARTITION BY customer_id, monthname(sales_date) ORDER BY customer_id)
FROM test3;

select t.*,t2.Total from 
  (select customer_id,
    SUM(CASE WHEN monthname(sales_date) = 'January' THEN amount ELSE 0 END) as 'Jan-21',
    SUM(CASE WHEN monthname(sales_date) = 'February' THEN amount ELSE 0 END) as 'Feb-21',
    SUM(CASE WHEN monthname(sales_date) = 'March' THEN amount ELSE 0 END) as 'Mar-21',
    SUM(CASE WHEN monthname(sales_date) = 'April' THEN amount ELSE 0 END) as 'Apr-21',
    SUM(CASE WHEN monthname(sales_date) = 'May' THEN amount ELSE 0 END) as 'May-21',
    SUM(CASE WHEN monthname(sales_date) = 'June' THEN amount ELSE 0 END) as 'June-21',
    SUM(CASE WHEN monthname(sales_date) = 'July' THEN amount ELSE 0 END) as 'July-21',
    SUM(CASE WHEN monthname(sales_date) = 'August' THEN amount ELSE 0 END) as 'Aug-21',
    SUM(CASE WHEN monthname(sales_date) = 'September' THEN amount ELSE 0 END) as 'Sept-21',
    SUM(CASE WHEN monthname(sales_date) = 'October' THEN amount ELSE 0 END) as 'Oct-21',
    SUM(CASE WHEN monthname(sales_date) = 'November' THEN amount ELSE 0 END) as 'Nov-21',
    SUM(CASE WHEN monthname(sales_date) = 'December' THEN amount ELSE 0 END) as 'Dec-21'
  from test3
  group by customer_id 
UNION
select 'Total' customer,
    SUM(CASE WHEN monthname(sales_date) = 'January' THEN amount ELSE 0 END) as 'Jan-21',
    SUM(CASE WHEN monthname(sales_date) = 'February' THEN amount ELSE 0 END) as 'Feb-21',
    SUM(CASE WHEN monthname(sales_date) = 'March' THEN amount ELSE 0 END) as 'Mar-21',
    SUM(CASE WHEN monthname(sales_date) = 'April' THEN amount ELSE 0 END) as 'Apr-21',
    SUM(CASE WHEN monthname(sales_date) = 'May' THEN amount ELSE 0 END) as 'May-21',
    SUM(CASE WHEN monthname(sales_date) = 'June' THEN amount ELSE 0 END) as 'June-21',
    SUM(CASE WHEN monthname(sales_date) = 'July' THEN amount ELSE 0 END) as 'July-21',
    SUM(CASE WHEN monthname(sales_date) = 'August' THEN amount ELSE 0 END) as 'Aug-21',
    SUM(CASE WHEN monthname(sales_date) = 'September' THEN amount ELSE 0 END) as 'Sept-21',
    SUM(CASE WHEN monthname(sales_date) = 'October' THEN amount ELSE 0 END) as 'Oct-21',
    SUM(CASE WHEN monthname(sales_date) = 'November' THEN amount ELSE 0 END) as 'Nov-21',
    SUM(CASE WHEN monthname(sales_date) = 'December' THEN amount ELSE 0 END) as 'Dec-21'
  from test3) as t
LEFT JOIN
(select customer_id,sum(amount) as `Total`
from test3
group by customer_id) as t2
ON t.customer_id=t2.customer_id;



