-- 1. Display the names of athletes who won a gold medal in the 2008 Olympics 
-- and whose height is greater than the average height of all athletes in the 2008 Olympics.

SELECT *
FROM olympics as o1
WHERE (Medal = 'Gold') AND (`Year`=2008) 
AND (Height > (SELECT AVG(Height) from olympics o2 WHERE `Year`=2008)); 

-- 2. Display the names of athletes who won a medal in the sport of basketball in the 2016 Olympics 
-- and whose weight is less than the average weight of all athletes who won a medal in the 2016 Olympics.

SELECT `Name`,Sport,Medal,`Year`,Weight
FROM olympics as o1
WHERE (Sport='BasketBall') AND (Medal IS NOT NULL) AND (`Year`=2016)
AND (Weight < (SELECT AVG(Weight) from olympics o2 WHERE (`Year`=2016) AND (Medal IS NOT NULL))); 

-- 3. Display the names of all athletes who have won a medal in the sport of swimming in both the 2008 and 2016 Olympics.
SELECT `Name`,Medal,`Year`,Sport
FROM olympics
WHERE Sport = 'Swimming' 
AND `Year` in (2008,2016) 
AND (Medal IS NOT NULL);

-- 4. Display the names of all countries that have won more than 50 medals in a single year.
SELECT country,`Year`,COUNT(*)
FROM olympics
WHERE Medal IS NOT NULL
GROUP BY country,`Year`
HAVING COUNT(*)>50
ORDER BY Year;

-- 5. Display the names of all athletes who have won medals in more than one sport in the same year.
SELECT `Name`,Year,
COUNT(DISTINCT(Sport)) as no_of_sport
FROM olympics
WHERE Medal IS NOT NULL
GROUP BY `Name`,`Year`
HAVING no_of_sport>1;

-- 6. What is the average weight difference between male and female athletes in the Olympics who have won a medal in the same event?
SELECT *
 FROM olympics o1
RIGHT JOIN (SELECT o2.`Event`
FROM olympics as o2
WHERE Medal in ('Gold','Silver','Bronze')
GROUP BY `Event`
HAVING COUNT(DISTINCT(Sex))>1) o2
ON o2.Event=o1.Event
WHERE Medal in  ('Gold', 'Silver', 'Bronze');

SELECT o1.*
FROM olympics o1
INNER JOIN (
    SELECT o2.`Event`
    FROM olympics as o2
    WHERE Medal in ('Gold', 'Silver', 'Bronze')
    GROUP BY `Event`
    HAVING COUNT(DISTINCT(Sex)) > 1
) AS filtered_events
ON o1.`EVENT` = filtered_events.`Event`
WHERE Medal in  ('Gold', 'Silver', 'Bronze');


-- 7. How many patients have claimed more than the average claim amount for patients who are smokers 
-- and have at least one child, and belong to the southeast region? 

SELECT COUNT(*)
FROM insurance
WHERE claim>(SELECT AVG(claim) from insurance WHERE smoker = 'Yes' AND children>=1 AND region = 'southeast');


-- 8. How many patients have claimed more than the average claim amount for patients who are not smokers 
-- and have a BMI greater than the average BMI for patients who have at least one child?

SELECT COUNT(*)
FROM insurance
WHERE claim>(SELECT AVG(claim) from insurance WHERE smoker = 'No'
AND bmi > (SELECT AVG(bmi) from insurance WHERE children>=1));

-- 9. How many patients have claimed more than the average claim amount for patients who have a BMI greater than the average BMI 
-- for patients who are diabetic,  have at least one child, and are from the southwest region?

SELECT COUNT(*)
FROM insurance as i1
WHERE i1.claim > (SELECT AVG(i2.claim) from insurance as i2 
WHERE i2.bmi > (SELECT AVG(i3.bmi) from insurance as i3 WHERE i3.diabetic = 'Yes' AND i3.children>0 AND i3.region = 'southwest'));

-- 10. What is the difference in the average claim amount between patients who are smokers 
-- and patients who are non-smokers, and have the same BMI and number of children?

SELECT children,bmi,smoker,AVG(claim)
from insurance
GROUP BY children,bmi,smoker
ORDER BY bmi,children,smoker;