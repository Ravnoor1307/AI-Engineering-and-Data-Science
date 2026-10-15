-- 1. Find out the average sleep duration of top 15 male candidates who's sleep duration are equal to 7.5 or greater than 7.5.

Select 
AVG(sleep_duration) from sleep
WHERE sleep_duration >=7.5 AND gender = 'Male'
ORDER BY sleep_duration DESC
LIMIT 15;

-- 2. Show avg deep sleep time for both gender. Round result at 2 decimal places.
Select gender, 
ROUND(AVG(sleep_duration*0.01*deep_sleep_percentage),2) as avg_sleep
from sleep
GROUP BY gender;

-- 3. Find out the lowest 10th to 30th light sleep percentage records where deep sleep percentage values are between 25 to 45. 
        -- Display age, light sleep percentage and deep sleep percentage columns only.
        
SELECT age, light_sleep_percentage,deep_sleep_percentage
from sleep
WHERE deep_sleep_percentage Between 25 AND 45
ORDER by light_sleep_percentage
LIMIT 10,20;

-- 4. Group by on exercise frequency and smoking status and show average deep sleep time, average light sleep time and avg rem sleep time.

SELECT 
exercise_frequency,
smoking_status,
ROUND(AVG(sleep_duration*0.01*deep_sleep_percentage),2) as avg_deep_sleep,
ROUND(AVG(sleep_duration*0.01*light_sleep_percentage),2) as avg_light_sleep,
ROUND(AVG(sleep_duration*0.01*rem_sleep_percentage),2) as avg_rem_sleep
from sleep
GROUP BY exercise_frequency,smoking_status;

-- 5. Group By on Awekning and show AVG Caffeine consumption, AVG Deep sleep time 
-- and AVG Alcohol consumption only for people who do exercise atleast 3 days a week. 
-- Show result in descending order awekenings

SELECT awakenings,
ROUND(AVG(caffeine_consumption),2) as avg_coffee,
ROUND(AVG(sleep_duration*0.01*deep_sleep_percentage),2) as avg_deep_sleep,
ROUND(AVG(alcohol_consumption),2) as avg_alcohol
FROM sleep
WHERE exercise_frequency >2
GROUP BY awakenings
ORDER BY awakenings DESC;

-- 6. Display those power stations which have average 'Monitored Cap.(MW)' (display the values) between 1000 and 2000 and 
-- the number of occurance of the power stations (also display these values) are greater than 200. 
-- Also sort the result in ascending order.

SELECT
`Power Station`,
COUNT(*) as occurence,
AVG(`Monitored Cap.(MW)`) as avg_capacity
FROM task_campusx.power
GROUP BY `Power Station`
HAVING occurence > 200 AND (avg_capacity BETWEEN  1000 AND 2000)
ORDER BY avg_capacity;

-- 7. Display top 10 lowest "value" State names of which the Year either belong to 2013 or 2017 or 2021 and type is 'Public In-State'. 
-- Also the number of occurance should be between 6 to 10. 
-- Display the average value upto 2 decimal places, state names and the occurance of the states.

SELECT state,
ROUND(AVG(numbers),2) as avg_value,
COUNT(*) as frequency
FROM college
WHERE yearss IN (2013, 2017, 2021) AND typess = 'Public In-State'
GROUP BY state
HAVING frequency BETWEEN 6 AND 10
ORDER BY avg_value ASC
LIMIT 10;

-- 8. Best state in terms of low education cost (Tution Fees) in 'Public' type university.

SELECT state,
AVG(numbers) as avg_total_expense
FROM college
WHERE typess like '%Public%' AND expense LIKE '%Tuition%'
GROUP BY state
ORDER BY avg_total_expense ASC
LIMIT 1;

-- 9. 2nd Costliest state for Private education in year 2021. Consider, Tution and Room fee both.

SELECT 
state,
AVG(numbers)
FROM college
WHERE yearss = 2021 AND expense IN ('Fees/Tuition','Room/Board') AND typess like 'Private%'
GROUP BY state
ORDER BY AVG(numbers) DESC
LIMIT 1,1;

-- 10. Display total and average values of Discount_offered for all the combinations of 'Mode_of_Shipment' (display this feature) 
-- and 'Warehouse_block' (display this feature also) for all male ('M') and 'High' Product_importance. 
        -- Also sort the values in descending order of Mode_of_Shipment and ascending order of Warehouse_block.

SELECT
Mode_of_Shipment,Warehouse_block,Gender,Product_importance,
sum(Discount_offered) as total_discount,
avg(Discount_offered) as avg_discount
from shipping as s
WHERE Gender = 'M' AND Product_importance = 'High'
group by Mode_of_Shipment,Warehouse_block
ORDER BY Mode_of_Shipment DESC, Warehouse_block ASC;