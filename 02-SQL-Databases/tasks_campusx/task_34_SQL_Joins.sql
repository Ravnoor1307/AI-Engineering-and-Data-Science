# 1. Find out top 10 countries' which have maximum A and D values.

SELECT ab.Country,
SUM(A+D) 
from ab_country as ab
INNER JOIN cd_country as cd
ON ab.Country = cd.Country
GROUP BY ab.Country
ORDER BY SUM(A+D) DESC
LIMIT 10;

# 2. Find out highest CL value for 2020 for every region. Also sort the result in descending order. 
# Also display the CL values in descending order.

-- SELECT 
-- cl.*,
-- ab.Region,ab.A,ab.B,
-- cd.C,cd.D,
-- efg.E,efg.F,efg.G,
SELECT ab.Region,cl.Edition,
MAX(cl.CL) as max_cl
FROM cl_country as cl
LEFT JOIN ab_country as ab
ON (cl.Country = ab.Country AND cl.Edition = ab.Edition)
LEFT JOIN cd_country as cd
ON (ab.Country = cd.Country AND ab.Edition = cd.Edition AND ab.Region = cd.Region)
LEFT JOIN efg_country as efg
ON (ab.Country = efg.Country AND ab.Edition = efg.Edition AND ab.Region = efg.Region)
WHERE cl.Edition=2020
GROUP BY ab.region
ORDER BY max_cl DESC;

SELECT ab.Region,
MAX(cl.CL) as max_cl
FROM cl_country as cl
LEFT JOIN ab_country as ab
ON (cl.Country = ab.Country AND cl.Edition = ab.Edition)
WHERE cl.Edition = 2020
GROUP BY ab.Region
ORDER BY max_cl DESC;

# 3. Find top-5 most sold products.
select 
sales.ProductID,products.Name,SUM(sales.Quantity) as total_quantity
from sales1 as sales
LEFT JOIN products
ON sales.ProductID = products.ProductID
GROUP BY sales.ProductID,products.Name
ORDER By total_quantity DESC
LIMIT 5;

# 4. Find sales man who sold most no of products.
select sales.SalesPersonID, employees.FirstName, employees.MiddleInitial, employees.LastName,
SUM(sales.Quantity) as total_sales
from sales1 as sales
LEFT JOIN employees
ON sales.SalesPersonID = employees.EmployeeID
GROUP BY sales.SalesPersonID, employees.FirstName, employees.MiddleInitial, employees.LastName
ORDER BY total_sales DESC
LIMIT 1;

# 5. Sales man name who has most no of unique customer.
select employees.FirstName, employees.MiddleInitial, employees.LastName, t1.distinct_customers
 from (select sales.SalesPersonID, 
COUNT(DISTINCT(sales.CustomerID)) as distinct_customers
FROM sales1 as sales
GROUP BY sales.SalesPersonID
ORDER BY distinct_customers DESC LIMIT 1) t1
LEFT JOIN employees
ON t1.SalesPersonID = employees.EmployeeID;


# 6. Sales man who has generated most revenue. Show top 5.
select sales.SalesPersonID, COUNT(sales.ProductID) as no_of_order, SUM(sales.Quantity) as total_quantity,
SUM(sales.Quantity * products.Price)as total_revenue,employees.FirstName, employees.MiddleInitial,employees.LastName
from sales1 as sales
LEFT JOIN products
ON sales.ProductID = products.ProductID
LEFT JOIN employees
ON sales.SalesPersonID = employees.EmployeeID
GROUP BY sales.SalesPersonID,employees.FirstName, employees.MiddleInitial,employees.LastName
ORDER BY total_revenue DESC LIMIT 1;


# 7. List all customers who have made more than 10 purchases.
select sales.CustomerID, COUNT(sales.ProductID) as count_orders, 
CONCAT(c.FirstName,' ',c.LastName) as customer_name
from sales1 as sales
JOIN customers as c
ON sales.CustomerID = c.CustomerID
GROUP BY sales.CustomerID,c.FirstName, c.LastName
HAVING COUNT(sales.ProductID)>10
ORDER BY COUNT(sales.ProductID) DESC;

# 8. List all salespeople who have made sales to more than 5 customers.

SELECt sales.SalesPersonID, CONCAT(e.FirstName,' ',e.LastName) as salesp_name,
COUNT(DISTINCT(CustomerID)) as distinct_cust
from sales1 as sales
JOIN employees as e
ON sales.SalesPersonID = e.EmployeeID
GROUP BY SalesPersonID, e.FirstName, e.LastName
HAVING distinct_cust > 5
ORDER BY distinct_cust DESC;

# 9. List all pairs of customers who have made purchases with the same salesperson.

SELECT CONCAT(B.FirstName, ' ' , B.LastName)as first_customer_name,
CONCAT(C.FirstName, ' ' , C.LastName)as second_customer_name
FROM (SELECT DISTINCT s1.CustomerID as first_customer, 
s2.CustomerID as second_customer,
s1.SalesPersonID 
from sales1 as s1
JOIN sales1 as s2
ON s1.SalesPersonID = s2.SalesPersonID
WHERE s1.SalesPersonID = s2.SalesPersonID AND s1.CustomerID!=s2.CustomerID) as A
JOIN customers B
ON A.first_customer=B.CustomerID
LEFT JOIN customers C
ON A.second_customer=C.CustomerID
LEFT JOIN employees D
ON A.SalesPersonID = D.EmployeeID;






