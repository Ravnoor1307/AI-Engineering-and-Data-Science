# Week 15 : https://learnwith.campusx.in/s/courses/637339afe4b0615a1bbed390/take

# 1. select a particular database
-- create database zomato;
use zomato;

-- 2. count number of rows
SELECT count(*) from order_details;

-- 3. return 5 random records
SELECT * from users
ORDER BY rand()
LIMIT 5;

-- 4. find null values
SELECT * from zomato.orders
WHERE restaurant_rating IS NULL; 

-- 5. find orders placed by each customer
select users.user_id, users.name,
count(*) as no_of_orders
from orders
JOIN users
ON orders.user_id = users.user_id
Group by orders.user_id, users.name;

-- 6. find restaurants with most number of menu items

select r_id,count(DISTINCT(f_id)) from menu
group by r_id;

-- 7. find number of votes and avg rating for all the restaurants
select restaurants.r_id,restaurants.r_name,
count(*) as votes,
ROUND(AVG(restaurant_rating),2) as average_rating
from orders
JOIN restaurants
ON orders.r_id = restaurants.r_id
GROUP BY restaurants.r_id,restaurants.r_name;


-- 8. find the food that is being sold at most number of restaurants

select food.f_id,food.f_name,
count(menu.f_id) as sold
from menu
JOIN food
on menu.f_id = food.f_id
GROUP BY food.f_id,food.f_name
ORDER BY sold DESC
LIMIT 1;

-- 9. fins restaurant with max revenue in a given month
SELECT orders.r_id,r.r_name,
SUM(orders.amount) as revenue,
MONTHNAME(date) as month_name
from orders
JOIN restaurants as r
ON orders.r_id = r.r_id
GROUP BY orders.r_id,MONTHNAME(date), r.r_name
ORDER BY revenue DESC;

-- 10. find restaurant with sales > x
SELECT orders.r_id,r.r_name,
SUM(orders.amount) as revenue
from orders
JOIN restaurants as r
ON orders.r_id = r.r_id
GROUP BY orders.r_id, r.r_name
HAVING revenue > 1500;

-- 11. find customers who have never ordered
SELECT e1.user_id,e2.name from (select user_id from users
EXCEPT 
select t1.user_id from orders t1) as e1
LEFT JOIN users as e2
ON e1.user_id=e2.user_id;


-- 12. show order details of a particular customer in a given date range
SELECT t1.order_id,t1.user_id,t1.amount,t1.date,t3.f_name
from orders as t1
JOIN order_details as t2
ON t1.order_id=t2.order_id
JOIN food as t3
ON t2.f_id=t3.f_id
WHERE t1.date BETWEEN '2022-05-15' AND '2022-06-15';
--------------------------------------------------------------------------------------------------------


-- 13. customer favourite food
SELECT t1.user_id,t2.order_id,t2.f_id,
COUNT(t2.f_id)
FROM orders as t1
JOIN order_details as t2
ON t1.order_id = t2.order_id
GROUP BY t1.user_id,t2.order_id,t2.f_id;

----------------------------------------------------------------------------------------------------------------------------


-- 14. find most costly restuarant(avg price/dish)

select o1.r_id, t2.r_name,
SUM(o1.price)/Count(o1.r_id) as total
from menu as o1
JOIN restaurants as t2
ON o1.r_id = t2.r_id
GROUP BY o1.r_id, t2.r_name
ORDER BY total DESC
LIMIT 1;

-- 15. find delivery partner compensation using the formula (#deliveries * 100 + 1000 * avg_rating)

SELECT t1.partner_id,t2.partner_name,
COUNT(*)*100 + (1000 * AVG(delivery_rating)) as compensation
FROM orders as t1
JOIN delivery_partner as t2
ON t1.partner_id = t2.partner_id
GROUP BY t1.partner_id,t2.partner_name
ORDER BY compensation DESC;


-- 16. find revenue per month for a restaurant
SELECT t1.r_id,t2.r_name,
count(DISTINCT(monthname(t1.date))) as no_of_months,
SUM(amount)/count(DISTINCT(monthname(t1.date))) as sale_per_month
from orders as t1
JOIN restaurants as t2
ON t1.r_id=t2.r_id
GROUP BY t1.r_id,t2.r_name;

-------------------------------------------------------------------------------------------------------------------------------------

-- 17. find correlation between delivery_time and total rating

-- 18. find corr between #orders and avg price for all restuarants 
--------------------------------------------------------------------------------------------------------------------------------------


########################### IMP
-- 19. Find all veg restaurants
select t1.r_id,t4.r_name
from orders as t1
JOIN order_details as t2
ON t1.order_id = t2.order_id
JOIN food as t3
ON t2.f_id = t3.f_id
JOIN restaurants as t4
ON t1.r_id = t4.r_id
GROUP BY t1.r_id,t4.r_name
HAVING MIN(t3.type) = 'Veg' AND MAX(t3.type) = 'Veg';


-- 20. find min and max order value for all customers

SELECT t1.user_id, t2.name, MAX(t1.amount_per_order)as max_order,
MIN(t1.amount_per_order) as min_order,AVG(t1.amount_per_order) as average_spent
FROM 
  (select user_id,order_id, 
  SUM(amount) as amount_per_order
  from orders
  GROUP BY user_id,order_id
  ORDER BY user_id) as 
t1
JOIN users as t2
ON t1.user_id=t2.user_id
GROUP BY t1.user_id,t2.name;