-- 1. find top 5 samsung phones with biggest screen size

SELECT brand_name, model, screen_size from smartphones
WHERE brand_name = 'samsung'
ORDER BY (screen_size) DESC
LIMIT 5;

-- 2. sort all the phones in descending order of the number of total cameras 

SELECT brand_name, model, (num_rear_cameras + num_front_cameras) AS total_cameras
FROM smartphones
ORDER BY total_cameras DESC;

--  3. sort data on the basis of ppi in decreasing order

SELECT model, 
sqrt(resolution_width * resolution_width + resolution_height * resolution_height)/screen_size as ppi
FROM smartphones
ORDER BY ppi DESC;


-- ##############  4. find the phone with 2nd largest battery

SELECT model, battery_capacity
FROM smartphones
ORDER BY battery_capacity DESC
LIMIT 1,1;

SELECT model, battery_capacity
FROM smartphones
ORDER BY battery_capacity DESC
LIMIT 2,2;

 
--  5. find the name and rating of the worst rated apple phone

SELECT model,rating FROM smartphones
WHERE brand_name = 'apple'
ORDER BY rating
LIMIT 1;


--  6. sort phones alphabetically and then on the basis of rating in desc order

SELECt model,rating
FROM smartphones
ORDER BY model ASC, rating DESC;
--  7. sort phones alphabetically and then on the basis of price in ascending order

############################### GROUP BY #################################################################################

-- 1. Group smartphones by brand and get the count, average price, max rating, avg screen size, and avg battery capacity

SELECT brand_name, 
count(*) as num_phones, 
AVG(price) as average_price, 
MAX(rating) as max_rating,
AVG(screen_size) as average_screen_size,
AVG(battery_capacity) as average_battery
FROM smartphones
GROUP BY brand_name
ORDER BY num_phones DESC
LIMIT 5;

-- 2. Group smartphones by whether they have an NFC and get the average price and rating 

SELECT 
has_nfc,
AVG(price) as average_price,
AVG(rating) as average_rating
FROM smartphones
GROUP BY has_nfc;

-- 3. Avg price of 5g phones vs avg price of non 5g phones
SELECT 
has_5g,
AVG(price) as average_price,
AVG(rating) as average_rating
FROM smartphones
GROUP BY has_5g;


-- 4. Group smartphones by the extended memory available and get the average price
SELECT 
extended_memory_available,
AVG(price) as average_price,
AVG(rating) as average_rating
FROM smartphones
GROUP BY extended_memory_available;

-- 5.  Group smartphones by the brand and processor brand and get the count of models and the average primary camera resolution (rear)
SELECT brand_name, processor_brand,
count(model) as total_phones,
AVG(price) as average_price,
AVG(primary_camera_rear) as average_primary_camera_rear
FROM smartphones
GROUP BY brand_name,processor_brand
ORDER BY brand_name;



-- 6. Find the top 5 most costly phone brands
SELECT brand_name,
MAX(price) as max_price_brand
FROM smartphones
GROUP BY brand_name
ORDER BY  max_price_brand DESC
LIMIT 6;

-- 7. Which brand makes the smallest-screen smartphones

SELECT brand_name, 
AVG(screen_size) as avg_screen_size,
COUNT(model) as total_phones
FROM smartphones
GROUP BY brand_name
ORDER BY avg_screen_size
LIMIT 4;

-- 1:16:35 8. Group smartphones by the brand, and find the brand with the highest number of models that have both NFC and an IR blaster
-- 1:20:18 9. Find all Samsung 5g enabled smartphones and find out the avg price for NFC and Non-NFC phones

############################################################## HAVING ############################################################

SELECT brand_name, 
COUNT(*) as count_phones,
ROUND(AVG(rating)) as avg_rating
FROM smartphones
GROUP BY brand_name
HAVING count_phones>20
ORDER BY avg_rating DESC;


--  Find the top 3 brands with the highest avg ram that has a refresh rate of at least 90 Hz and 
-- 			fast charging available and don't consider brands that have less than 10 phones

SELECT brand_name, 
count(*) as phone_count,
ROUND(avg(ram_capacity)) as average_ram
FROM smartphones
WHERE refresh_rate >= 90 AND fast_charging_available = 1
GROUP BY brand_name
HAVING phone_count > 10
ORDER BY average_ram DESC
LIMIT 3;