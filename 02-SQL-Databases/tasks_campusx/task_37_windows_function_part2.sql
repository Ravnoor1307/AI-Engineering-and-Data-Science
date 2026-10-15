## 1. Rank Employee in terms of revenue generation. Show employee id, first name, revenue, and rank

-- order_details + orders + employees
SELECT *,
RANK() OVER(ORDER BY t4.total_sales DESC) as rank_total_sales
from  
  (SELECT DISTINCT t1.EmployeeID,concat(TitleOfCourtesy,' ',FirstName,' ',LastName) as emp_name,Title,
  # t2.OrderID,
  # t3.ProductID,t3.UnitPrice,t3.Quantity,
  # ROUND((t3.UnitPrice*Quantity),2) as sales,
  ROUND(SUM(t3.UnitPrice*t3.Quantity) OVER(PARTITION BY t1.EmployeeID),2) as total_sales
  from nw_employees as t1
  JOIN nw_orders as t2
  ON t1.EmployeeID = t2.EmployeeID
  JOIN nw_order_details as t3
  ON t2.OrderID = t3.OrderID)
t4;

-- SELECT *,
-- RANK() OVER(ORDER BY t4.total_sales DESC)
-- from  
--   (SELECT DISTINCT t1.EmployeeID,concat(TitleOfCourtesy,' ',FirstName,' ',LastName) as emp_name,Title,
--   SUM(t3.UnitPrice*t3.Quantity) OVER(PARTITION BY t1.EmployeeID) as total_sales
--   from nw_employees as t1
--   JOIN nw_orders as t2
--   ON t1.EmployeeID = t2.EmployeeID
--   JOIN nw_order_details as t3
--   ON t2.OrderID = t3.OrderID)
-- t4;

## 2. Show All products cumulative sum of units sold each month.

SELECT DISTINCT t1.ProductID,
#t1.Quantity,
t2.ProductName,
month(t3.OrderDate) as month_name,
SUM(t1.Quantity) OVER(PARTITION BY ProductID,month(t3.OrderDate) ORDER BY ProductID,month(t3.OrderDate)) as sold_per_month
FROM task_campusx.nw_order_details as t1
JOIN nw_products as t2
ON t1.ProductID=t2.ProductID
JOIN nw_orders as t3
ON t1.OrderID = t3.OrderID;

## 3. Show Percentage of total revenue by each suppliers

SELECT *,
ROUND(table1.sum_sales_supplierid/sum(table1.sum_sales_supplierid) OVER() *100,2) as percent_sales
from
  (SELECT DISTINCT t1.SupplierID,
  t2.CompanyName,
  # t3.ProductID,t3.UnitPrice,t3.Quantity,
  # (t3.UnitPrice*t3.Quantity) as sales,
  SUM(t3.UnitPrice*t3.Quantity) OVER(PARTITION BY SupplierID) as sum_sales_supplierid
  from nw_products t1
  JOIN nw_suppliers as t2
  ON t1.SupplierID=t2.SupplierID
  JOIN nw_order_details as t3
  ON t1.ProductID = t3.ProductID) 
as table1
ORDER By percent_sales DESC;

## 4. Show Percentage of total orders by each suppliers

SELECT *,
ROUND(table1.sum_orders_supplierid/sum(table1.sum_orders_supplierid) OVER() *100,2) as percent_sales
from
  (SELECT DISTINCT t1.SupplierID,
  t2.CompanyName,
  # t3.ProductID,t3.UnitPrice,t3.Quantity,
  # (t3.UnitPrice*t3.Quantity) as sales,
  SUM(t3.Quantity) OVER(PARTITION BY SupplierID) as sum_orders_supplierid
  from nw_products t1
  JOIN nw_suppliers as t2
  ON t1.SupplierID=t2.SupplierID
  JOIN nw_order_details as t3
  ON t1.ProductID = t3.ProductID) 
as table1
ORDER By percent_sales DESC;

## 5. Show All Products Year Wise report of totalQuantity sold, percentage change from last year.

select *,
(sold_per_year - LAG(sold_per_year) OVER(PARTITION BY ProductID))/(LAG(sold_per_year) OVER(PARTITION BY ProductID)) *100 as yoy_growth
from
  (SELECT DISTINCT t1.ProductID,
  #t1.Quantity,
  t2.ProductName,
  year(t3.OrderDate) as `year`,
  SUM(t1.Quantity) OVER(PARTITION BY ProductID,year(t3.OrderDate) ORDER BY ProductID,year(t3.OrderDate)) as sold_per_year
  FROM task_campusx.nw_order_details as t1
  JOIN nw_products as t2
  ON t1.ProductID=t2.ProductID
  JOIN nw_orders as t3
  ON t1.OrderID = t3.OrderID)
table1;

## 6. For each condition, what is the average satisfaction level of drugs that are "On Label" vs "Off Label"?

select DISTINCT `Condition`,Indication,
ROUND(AVG(Satisfaction) OVER(PARTITION BY `Condition`,Indication),2) as avg_satisfaction
from drug_clean
WHERE Indication in ('Off Label','On Label');

######################################################################################################################################

## 7. For each drug type (RX, OTC, RX/OTC), what is the average ease of use and 
## satisfaction level of drugs with a price above the median for their type? ########### (how to find median?????????)

SELECT * from
(SELECT `Condition`,Drug,Type,EaseOfUse,Satisfaction,Price,
AVG(EaseOfUse) over(Partition by Type) as avg_easeofuse,
AVG(Satisfaction) over(Partition by Type) as avg_satisfaction,
AVG(Price) over(Partition by Type) as avg_price
from drug_clean) as t1
WHERE t1.Price>t1.avg_price;
#################################################################################################################################

## 8. What is the cumulative distribution of EaseOfUse ratings for each drug type (RX, OTC, RX/OTC)? 
## Show the results in descending order by drug type and cumulative distribution. 
## (Use the built-in method and the manual method by calculating on your own. For the manual method, 
## use the "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW" and see if you get the same results as the built-in method.)

SELECT `Condition`,Drug,Type,EaseOfUse,Satisfaction,Price,
CUME_DIST() OVER(PARTITION BY Type ORDER BY EaseOfuse DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cume_dist_easeofuse
FROM drug_clean;

#######################################################################################################################################

## 9. What is the median satisfaction level for each medical condition? Show the results in descending order by median satisfaction level. 
## (Don't repeat the same rows of your result.)

SELECT DISTINCT `Condition`,
AVG(Satisfaction) OVER(PARTITION BY `Condition`) as avg_satisfaction
from drug_clean
ORDER BY avg_satisfaction DESC;

###############################################################################################################################

## 10. What is the running average of the price of drugs for each medical condition?
## Show the results in ascending order by medical condition and drug name.

SELECT `Condition`,Drug,Price,
ROUND(AVG(Price) OVER(PARTITION BY `Condition` ORDER BY `Condition`,Drug ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),2) as moving_avg_price
from drug_clean;

## 11.  What is the percentage change in the number of reviews for each drug between the previous row and the current row? 
## Show the results in descending order by percentage change.

SELECT Drug,Reviews,
LAG(Reviews) OVER(PARTITION BY Drug) as next_review,
ROUND(((Reviews - LAG(Reviews) OVER(PARTITION BY Drug))/LAG(Reviews) OVER(PARTITION BY Drug))*100,2) as percent_change
FROM drug_clean;

## 12. What is the percentage of total satisfaction level for each drug type (RX, OTC, RX/OTC)? 
## Show the results in descending order by drug type and percentage of total satisfaction.

SELECT DISTINCT Type,
SUM(Satisfaction) OVER(Partition by Type ORDER BY Type DESC) as sum_satisfaction,
SUM(Satisfaction) OVER() as total_sat,
ROUND((SUM(Satisfaction) OVER(Partition by Type ORDER BY Type DESC)/SUM(Satisfaction) OVER())*100,2) as percent_satisfaction
from drug_clean;

## 13. What is the cumulative sum of effective ratings for each medical condition and drug form combination? 
## Show the results in ascending order by medical condition, drug form and the name of the drug.

SELECT DISTINCT `Condition`,Form,Drug,Effective,
SUM(Effective) OVER(Partition by `Condition`,Form ORDER BY `Condition`,Form,Drug ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cum_sum_effective
from drug_clean;

## 14. What is the rank of the average ease of use for each drug type (RX, OTC, RX/OTC)? 
## Show the results in descending order by rank and drug type.

SELECT *,
RANK() OVER(ORDER BY avg_ease_of_use DESC) as rank_ease_of_use
FROM 
  (SELECT DISTINCT Type,
  AVG(EaseOfUse) OVER(PARTITION BY Type) as avg_ease_of_use
  #RANK() OVER(ORDER BY AVG(EaseOfUse))
  from drug_clean) as 
t1
ORDER BY rank_ease_of_use DESC;

## 15. For each condition, what is the average effectiveness of the top 3 most reviewed drugs?

SELECT DISTINCT `Condition`,
ROUND(AVG(Effective) OVER(PARTITION BY `Condition`),2) as avg_effective
from 
  (SELECT `Condition`,Drug,Effective,Reviews,
  ROW_NUMBER() OVER(PARTITION BY `Condition` ORDER BY Reviews DESC) as top_3
  from drug_clean) as t1
WHERE t1.top_3 <4
ORDER BY avg_effective DESC;