SELECT current_date();
SELECT current_time();
SELECT current_timestamp();
SELECT curdate();
SELECT curtime();

SELECt NOW();
USE campusx;
-- CREATE TABLE rides (
--     ride_number INT PRIMARY KEY,
--     ride_start_date DATETIME,
--     ride_end_date DATETIME
-- );

-- Inserting a single row
-- INSERT INTO rides (ride_number, ride_start_date, ride_end_date)
-- VALUES (4, '2023-08-21 09:00:00', '2023-08-21 10:30:00');

-- Inserting multiple rows
-- INSERT INTO Rides (ride_number, ride_start_date, ride_end_date)
-- VALUES 
--     (1, '2023-08-21 11:00:00', '2023-08-21 12:15:00'),
--     (2, '2023-08-21 13:30:00', '2023-08-21 14:45:00'),
--     (3, '2023-08-21 15:15:00', '2023-08-21 16:00:00');

SELECT * from rides;

# date-month-year format
SELECT ride_start_date,date_format(ride_start_date,'%d-%b-%y') as date_month_year
FROM rides;

SELECT ride_start_date,date_format(ride_start_date,'%r') as am_pm
FROM rides;

SELECT ride_start_date,
date_format(ride_start_date,'%r') as h_m_s_am_pm,
date_format(ride_start_date,'%l:%i:%p') as h_m_am_pm
FROM rides;

SELECt CURRENt_DATE(),DATEDIFF(CURRENt_DATE(),'1995-03-09')/365 as days_diff;

SELECT NOW(),
DATE_ADD(NOW(),INTERVAL 11 DAY) as after_11_days;

SELECT NOW(),
DATE_SUB(NOW(),INTERVAL 9 MONTH) as before_9_months;

########################################################## FLIGHT DATASET ############################################################

use flights;

## 1. Find the month with most number of flights

SELECT DISTINCT monthname(date_of_journey) as month_name,
COUNT(*) OVER(PARTITION BY monthname(date_of_journey)) as number_of_flights
FROM flights_data
ORDER BY number_of_flights DESC
LIMIT 1;

## 2. Which week day has most costly flights 

SELECT DISTINCT DAYNAME(date_of_journey) as week_name,
AVG(price) OVER(PARTITION BY DAYNAME(date_of_journey)) as avg_price
from flights_data
ORDER BY avg_price DESC
LIMIT 1;

## 3. Find number of indigo flights every month
SELECT DISTINCt monthname(date_of_journey) as month_name,
COUNT(*) OVER(PARTITION BY monthname(date_of_journey)) as number_of_flights
FROM flights_data
WHERE airline = 'Indigo';

## 4. Find list of all flights that depart between 10AM and 2PM from Banglore to Delhi
SELECT *, 
    TIME_FORMAT(dep_time, '%h:%i %p') AS departure_time
FROM flights_data
WHERE dep_time BETWEEN '10:00:00' AND '14:00:00'
# WHERE HOUR(dep_time) BETWEEN '10' AND '14'
AND source = 'Banglore' AND destination = 'Delhi';  

-- not working
-- SELECT *, 
--     TIME_FORMAT(dep_time, '%h:%i %p') AS departure_time
-- FROM flights_data
-- WHERE TIME_FORMAT(dep_time, '%h:%i %p') BETWEEN '10:00 AM' AND '2:00 PM';

## 5. Find the number of flights departing on weekends from Bangalore

SELECT 
 # DAYNAME(date_of_journey) as day_of_week,
 COUNT(*) as no_flights_weekends
FROM flights_data
WHERE DAYNAME(date_of_journey) IN ('Saturday','Sunday')
AND `source` = 'Banglore';

## 6. Calculate the arrival time for all flights by adding the duration to the departure time.

-- ALTER TABLE flights_data ADD COLUMN departure DATETIME;
select * from flights_data;

-- making departure column as date + time:
-- UPDATE flights_data
-- SET departure= STR_TO_DATE(CONCAT(date_of_journey,' ',dep_time),'%Y-%m-%d %H:%i');

-- creating arrival column:
-- ALTER TABLE flights_data
-- ADD COLUMN arrival DATETIME;

-- making arrival column as departure + duration:
-- UPDATE flights_data
-- SET arrival = DATE_ADD(departure,INTERVAL duration MINUTE);

SELECT departure,arrival,TIME(arrival) from flights_data;

## 7. Calculate the arrival date for all the flights

SElect arrival,DATE(arrival) as arrival_date from flights_data;

## 8. Calculate the average duration of flights between two cities.

SELECt DISTINCT source,destination,
AVG(duration) OVER(PARTITION BY source,destination) as avg_time_mins,
TIME_FORMAT(sec_to_time((AVG(duration) OVER(PARTITION BY source,destination)* 60)),'%kh:%im') as avg_time_hrs_mins 
from flights_data;

## 9. Find all flights that arrive at their destination after midnight having no stops
SELECt airline,source,destination,departure,arrival,total_stops,
DATE(departure) as date_arrival,
DATE(arrival) as date_arrival 
from flights_data
WHERE DATE(arrival)- DATE(departure)>0
AND total_stops = 'non-stop';

## 10. Find quarter wise number of flights for each airline

SELECt
DISTINCT airline,QUARTER(departure) as quarter_no,
COUNT(*) OVER(PARTITION BY airline,QUARTER(departure) ORDER BY airline) as flights_per_quarter
from flights_data; 

## 11. Find the longest flight distance(between cities in terms of time) in India
SELECT * from flights_data
ORDER BY duration DESC
LIMIT 1;

## 12. Average time duration for flights that have 1 stop vs more than 1 stops
SELECT DISTINCT stops,
TIME_FORMAT(sec_to_time((AVG(avg_duration) OVER(PARTITION BY stops)* 60)),'%kh:%im') as avg_of_stops
from 
  (SELECT total_stops,
  AVG(duration) as avg_duration,
    CASE
    WHEN total_stops != '1 stop' THEN 'more than 1 stop'
    ELSE '1 stop'
    END AS stops 
  from flights_data
  GROUP BY total_stops
  HAVING total_stops!='non-stop') as 
t;

## 13. Find all Air India flights in a given date range originating from Delhi
SELECt *,
DATE(departure)  as date_of_dep 
from flights_data
WHERE airline = 'Air India' AND source = 'Delhi'
AND DATE(departure) BETWEEN '2019-01-01' AND '2019-01-31';

## 14. Find the longest flight of each airline
SELECT DISTINCT airline,
TIME_FORMAT(sec_to_time((MAX(duration) OVER(PARTITION BY airline ORDER BY duration DESC)* 60)),'%kh:%im') as max_duration
FROM flights_data;

## 15. Find all the pair of cities having average time duration > 3 hours
SELECT destination,source,
TIME_FORMAT(sec_to_time((AVG(duration)* 60)),'%kh:%im') as max_duration
FROM flights_data
GROUP BY source,destination
HAVING AVG(duration) > 180;

## 16. Make a weekday vs time grid showing frequency of flights from Banglore and Delhi

SELECT 
dayname(date_of_journey) as day_name,
SUM(CASE WHEN dep_time>='00:00' AND dep_time<'06:00' THEN 1 ELSE 0 END) as '12-06 AM',
SUM(CASE WHEN dep_time>= '06:00' AND dep_time<'12:00' THEN 1 ELSE 0 END) as '06-12 AM',
SUM(CASE WHEN dep_time>= '12:00' AND dep_time<'18:00' THEN 1  ELSE 0 END) as '12-06 PM',
SUM(CASE WHEN dep_time>= '18:00' AND dep_time<'24:00' THEN 1 ELSE 0 END) as '06-12 PM'
FROm flights_data
WHERE source='banglore' AND destination = 'Delhi'
GROUP BY dayname(date_of_journey);
  
## 17. Make a weekday vs time grid showing avg flight price from Banglore and Delhi

SELECT DAYNAME(departure) as day_of_week,
AVG(CASE WHEN HOUR(departure) BETWEEN 0 AND 5 THEN price ELSE NULL END) AS '12AM - 6AM',
AVG(CASE WHEN HOUR(departure) BETWEEN 6 AND 11 THEN price ELSE NULL END) AS '6AM - 12PM',
AVG(CASE WHEN HOUR(departure) BETWEEN 12 AND 17 THEN price ELSE NULL END) AS '12PM - 6PM',
AVG(CASE WHEN HOUR(departure) BETWEEN 18 AND 23 THEN price ELSE NULL END) AS '6PM - 12PM'
FROM flights_data
WHERE source = 'Banglore' AND destination = 'Delhi'
GROUP BY DAYNAME(departure);
