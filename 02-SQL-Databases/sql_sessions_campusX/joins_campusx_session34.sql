Select * FROM order_details;

## Joining order_details and orders on order_id column
select * from order_details as t1
JOIN orders as t2
ON t1.order_id = t2.order_id
JOIN users as t3
ON t2.user_id = t3.user_id;

-- 1. Find all profitable orders 

Select
e1.order_id, 
SUM(e1.profit) as sum_profit 
FROM order_details as e1
GROUP BY e1.order_id
HAVING sum_profit>0;

-- 2. Find the customer who has placed the max number of orders 

Select 
t2.name,
COUNT(*) as total_order
FROM orders as t1
JOIN users as t2
ON t1.user_id=t2.user_id
GROUP BY t2.name
ORDER BY total_order DESC
LIMIT 1;

-- 3. Which is the most profitable category 
-- 4. Which is the most profitable state 
-- 5. Find all categories with profits higher than 5000 