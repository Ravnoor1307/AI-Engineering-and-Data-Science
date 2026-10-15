use mohitdb;

select * from test3;



select customer_id,sum(amount) 
from test3
group by customer_id;

select 
sum(`Jan-21`),
sum(`Feb-21`),
sum(`Mar-21`),
sum(`Apr-21`),
sum(`May-21`),
sum(`June-21`),
sum(`July-21`),
sum(`Aug-21`),
sum(`Sept-21`),
sum(`Oct-21`),
sum(`Nov-21`),
sum(`Dec-21`)
 from (select
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
  group by monthname(sales_date)) as t3;
  
  select monthname(sales_date),sum(amount) 
from test3
group by monthname(sales_date);

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
  from test3;