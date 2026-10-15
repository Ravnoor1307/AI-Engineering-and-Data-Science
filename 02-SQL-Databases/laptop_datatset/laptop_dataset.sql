### 1 hr 10 mins : Week 16 
use campusx;
########################################################### 1. Backup of data ##################################################

# CREATE TABLE laptops_backup LIKE laptop_data;

-- adding data to backup table
# INSERT INTO laptops_backup
# SELECT * from laptop_data;

########################################################### 2.  Check number of rows ########################################

SELECT COUNT(*) from laptop_data;
-- 1272 rows

########################################################### 3. Check memory consumption for reference #################################

SELECT DATA_LENGTH/1024 as data_in_kb 
from information_schema.TABLES
WHERE TABLE_SCHEMA = 'campusx'
AND TABLE_NAME = 'laptop_data'; 

-- TABLE_CATALOG : 'def', TABLE_SCHEMA : 'campusx', TABLE_NAME : 'laptop_data', TABLE_TYPE : 'BASE TABLE', ENGINE : 'InnoDB', 
-- VERSION : '10', ROW_FORMAT : 'Dynamic', TABLE_ROWS :  '1272', AVG_ROW_LENGTH : '206', DATA_LENGTH : '262144', MAX_DATA_LENGTH: '0', 
-- INDEX_LENGTH: '0', DATA_FREE :'0', AUTO_INCREMENT : 'NULL', CREATE_TIME : '2023-08-13 00:59:28', UPDATE_TIME:  '2023-08-13 00:59:30', 
-- CHECK_TIME : 'NULL', TABLE_COLLATION : 'utf8mb4_0900_ai_ci', CHECKSUM, CREATE_OPTIONS, TABLE_COMMENT

########################################################### 4. Dop non-important columns ###############################################

ALTER TABLE laptop_data DROP COLUMN `Unnamed: 0`;
SELECT * from laptop_data;

########################################################### 5. Drop rows with all null value #####################################

DELETE FROM laptop_data
WHERE `index` IN (SELECT `index` FROM laptop_data
WHERE Company IS NULL AND TypeName IS NULL AND Inches IS NULL
AND ScreenResolution IS NULL AND Cpu IS NULL AND Ram IS NULL
AND Memory IS NULL AND Gpu IS NULL AND OpSys IS NULL AND
WEIGHT IS NULL AND Price IS NULL);

SELECT COUNT(*) from laptop_data;

########################################################### 6. Drop duplicate rows from the table (3 steps) (IMP) #################

# CREATE TABLE temp_table AS
# SELECT DISTINCT * FROM your_table;

-- Drop the original table
# DROP TABLE your_table;

-- Rename the temporary table to the original table name
# RENAME TABLE temp_table TO your_table;

########################################################### 7. Clean RAM & weight-> change col data type (IMP) ######################

-- converting column INCHES datatype from DOUBLE to DECIMAL
ALTER TABLE laptop_data MODIFY COLUMN Inches DECIMAL(10,1);

-- removing 'GB' from RAM column and making it into INT from TEXT (3 steps)

UPDATE laptop_data l1
JOIN laptop_data l2 
ON l1.`index` = l2.`index`
SET l1.Ram = REPLACE(l2.Ram, 'GB','');

SELECT * FROM laptop_data;

ALTER TABLE laptop_data MODIFY COLUMN Ram INTEGER;

-- This query uses a self-join to match the rows of laptop_data with the same index, 
-- and then updates the Ram column of l1 based on the modified Ram value from l2. 
-- The purpose of this query is to update the Ram column of each row in the laptop_data table by removing the 'GB' string from the Ram value. 
-- The self-join is used to match rows with the same index and perform the update based on the modified Ram value from the other matched row.
-- By using this self-join approach, you're effectively working around the limitation of not being able to reference the same table in a 
-- subquery within the SET clause of an UPDATE statement. Instead, you're joining the table with itself and using the joined data to 
-- update the columns in a valid way.


-- Changing weight column. removing 'KG' and converting to INT type from TEXT

UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.Weight = REPLACE(l2.Weight, 'kg','');

SELECT * FROM laptop_data;

ALTER TABLE laptop_data MODIFY COLUMN Weight INTEGER;

UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.Weight = REPLACE(l2.Weight, '?','8');

-- converting price column, rounding

UPDATE laptop_data as l1
JOIN laptop_data as l2
ON l1.`index` = l2.`index`
SET l1.Price = (SELECT ROUND(l2.Price));

SELECT * FROM laptop_data;

ALTER TABLE laptop_data MODIFY COLUMN Price INTEGER;

############################### 8. Creating categories for values ################################# 

SELECt Opsys, COUNT(*)
FROM laptop_data
GROUP BY Opsys;

-- catgeories are :
-- Windows 7 -> 45, Windows 10 S ->	8, Windows 10 ->	1046  AS 'windows'
-- No OS ->	63 AS 'no os'
-- macOS ->	13, Mac OS X ->	8 AS 'macos'
-- Linux ->	61 AS 'linux'
-- Chrome OS ->	27, Android ->	1 AS 'Others'
 
SELECT Opsys,
CASE
    WHEN Opsys LIKE '%mac%' THEN 'macos'
    WHEN Opsys LIKE '%window%' THEN 'windows'
    WHEN Opsys LIKE '%linux%' THEN 'linux'
    WHEN Opsys LIKE '%no%os%' THEN 'N/A'
    ELSE 'other'
END as'os_brand'
FROM laptop_data;

-- updating values
UPDATE laptop_data 
SET Opsys = CASE
    WHEN Opsys LIKE '%mac%' THEN 'macos'
    WHEN Opsys LIKE '%window%' THEN 'windows'
    WHEN Opsys LIKE '%linux%' THEN 'linux'
    WHEN Opsys LIKE '%no%os%' THEN 'N/A'
    ELSE 'other'
END;

SELECT * from laptop_data;

############################# 9 . Adding a new column based on previous (V IMP)  ######################################

###################### on gpu column:

ALTER TABLE laptop_data
ADD COLUMN gpu_brand VARCHAR(255) after Gpu,
ADD COLUMN gpu_name VARCHAR(255) after gpu_brand;

SELECt * from laptop_data;

## gpu_brand: first word before space from Gpu column
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.gpu_brand = (SELECT SUBSTRING_INDEX(l2.Gpu,' ',1));

SELECt * from laptop_data;

## gpu_name
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.gpu_name = REPLACE(l2.Gpu, l2.gpu_brand,'');

SELECt * from laptop_data;

## droping GPU column

ALTER TABLE laptop_data Drop column Gpu;

SELECt * from laptop_data;

##### on CPU column
ALTER TABLE laptop_data
ADD COLUMN cpu_brand VARCHAR(255) after Cpu,
ADD COLUMN cpu_name VARCHAR(255) after cpu_brand,
ADD COLUMN cpu_speed DECIMAL(10,1) after cpu_name;

## cpu_brand
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.cpu_brand = (SELECT SUBSTRING_INDEX(l2.Cpu,' ',1));

## cpu_speed (replacing GHZ keyword too an converting it into decimal)
 
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.cpu_speed = CAST(REPLACE(SUBSTRING_INDEX(l2.Cpu,' ',-1),'Ghz','') AS DECIMAL (10,2));

SELECT * from laptop_data;

## cpu_name
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.cpu_name = (SELECT REPLACE(REPLACE(l2.Cpu,l2.cpu_brand,''),SUBSTRING_INDEX(REPLACE(l2.Cpu,l2.cpu_brand,''),' ',-1),''));
          
SELECT * from laptop_data;

ALTER TABLE laptop_data DROP COLUMN Cpu;

### Screen Resolution column

ALTER TABLE laptop_data
ADD COLUMN resolution_width INT after ScreenResolution,
ADD COLUMN resolution_height INT  after resolution_width;

## resolution width and resolution height
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.resolution_width=
(SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(l2.ScreenResolution,' ',-1),'x',1)),
l1.resolution_height=
(SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(l2.ScreenResolution,' ',-1),'x',-1));

SELECT * from laptop_data;

## adding column touchscreen or not
ALTER TABLE laptop_data
ADD COLUMN touchscreen INT after resolution_height;

UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.touchscreen= (l2.ScreenResolution like '%touch%');

ALTER table laptop_data DROP COLUMN ScreenResolution;

SELECT * from laptop_data;

#### making different variations as same in cpu column
UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.cpu_name = 
(SELECT SUBSTRING_INDEX(TRIM(l2.cpu_name),' ',2));

SELECT * from laptop_data;

######## Memory column
-- creating 3 new columns:

ALTER TABLE laptop_data
ADD COLUMN memory_type VARCHAR(255) AFTER Memory,
ADD COLUMN primary_storage INT AFTER memory_type,
ADD COLUMN secondary_storage INT AFTER primary_storage;

ALTER TABLE laptop_data
MODIFY COLUMN memory_type VARCHAR(255);

UPDATE laptop_data l1
JOIN laptop_data l2
ON l1.`index` = l2.`index`
SET l1.memory_type=
CASE
    WHEN l2.MEMORY LIKE '%SSD%' AND l2.MEMORY LIKE '%HDD%' THEN 'Hybrid'
    WHEN l2.Memory LIKE '%SSD%' THEN 'SSD'
    WHEN l2.Memory LIKE '%HDD%' THEN 'HDD'
    WHEN l2.Memory LIKE '%Flash Storage%' THEN 'Flash Storage'
    WHEN l2.Memory LIKE '%Hybrid%' THEN 'Hybrid'
    WHEN l2.MEMORY LIKE '%Flash Storage%' AND l2.MEMORY LIKE '%HDD%' THEN 'Hybrid'
    ELSE NULL
END;

SELECT * from laptop_data;

-- extracting primary storage from memory column:

SELECT Memory,
REGEXP_SUBSTR(SUBSTRING_INDEX(Memory, '+' , 1),'[0-9]+'),
CASE WHEN memory LIKE '%+%' THEN REGEXP_SUBSTR(SUBSTRING_INDEX(Memory, '+', -1),'[0-9]+') ELSE 0 END
From laptop_data;

UPDATE laptop_data
SET primary_storage = REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',1),'[0-9]+'),
secondary_storage = CASE WHEN Memory LIKE '%+%' THEN REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',-1),'[0-9]+') ELSE 0 END;

SELECT * from laptop_data;

-- converting 1 and 2 TB into gbs
UPDATE laptop_data
SET primary_storage = CASE WHEN primary_storage <= 2 THEN primary_storage*1024 ELSE primary_storage END,
secondary_storage = CASE WHEN secondary_storage <= 2 THEN secondary_storage*1024 ELSE secondary_storage END;

SELECT * from laptop_data;

ALTER TABLE laptop_data DROP COLUMN gpu_name;

SELECT * FROM laptop_data;

########################################################### EDA #############################################################

###################### 1. head, tail and sample
use campusx;
# head
SELECT * FROM laptop_data
ORDER BY `index` LIMIT 5;

# tail
SELECT * FROM laptop_data
ORDER BY `index` DESC LIMIT 5;

# sample data
SELECT * FROM laptop_data
ORDER BY rand() LIMIT 5;

#################### 2. Univariate of numerical column (eg: PRICE column) # not working

SELECT
    COUNT(Price) AS TotalCount,
    MIN(Price) AS MinPrice,
    MAX(Price) AS MaxPrice,
    AVG(Price) AS AvgPrice,
    STD(Price) AS StdDevPrice,
    (SELECT Price FROM laptop_data ORDER BY Price LIMIT 1 OFFSET FLOOR(COUNT(*) * 0.25)) AS Q1,
    (SELECT Price FROM laptop_data ORDER BY Price LIMIT 1 OFFSET FLOOR(COUNT(*) * 0.5)) AS Median,
    (SELECT Price FROM laptop_data ORDER BY Price LIMIT 1 OFFSET FLOOR(COUNT(*) * 0.75)) AS Q3
FROM laptop_data;

###################### 3. missing values
SELECT COUNT(Price)
FROM laptop_data
WHERE Price IS NULL;

####################### 4. Outliers (not working)

SELECT * FROM (SELECT *,
PERCENTILE_CONT(0.25) WITHIN GROUP(ORDER BY Price) OVER() AS 'Q1',
PERCENTILE_CONT(0.75) WITHIN GROUP(ORDER BY Price) OVER() AS 'Q3'
FROM laptop_data) t
WHERE t.Price < t.Q1 - (1.5*(t.Q3 - t.Q1)) OR
t.Price > t.Q3 + (1.5*(t.Q3 - t.Q1));


##################### 5. horizontal / vertical histogram - creating buckets

-- creating seperate columns for each bucket
SELECT price,
CASE WHEN Price between 0 AND 25000 THEN 1 ELSE 0 END AS '0-25K',
CASE WHEN Price between 25001 AND 50000 THEN 1 ELSE 0 END AS '25K-50K',
CASE WHEN Price between 50001 AND 75000 THEN 1 ELSE 0 END AS '50K-75K',
CASE WHEN Price between 75001 AND 100000 THEN 1 ELSE 0 END AS '75K-100K',
CASE WHEN Price > 100000 THEN 1 ELSE 0 END AS '>100K'
FROM laptop_data;

-- repeat * symbol equal to count of laptops:

SELECT t.buckets,REPEAT('*',COUNT(*)/5) FROM (SELECT price, 
CASE 
	WHEN price BETWEEN 0 AND 25000 THEN '0-25K'
    WHEN price BETWEEN 25001 AND 50000 THEN '25K-50K'
    WHEN price BETWEEN 50001 AND 75000 THEN '50K-75K'
    WHEN price BETWEEN 75001 AND 100000 THEN '75K-100K'
	ELSE '>100K'
END AS 'buckets'
FROM laptop_data) t
GROUP BY t.buckets;

#############################################3 categorical colums

############# 6. Value count for categorical columns

SELECT  company,Count(company) from laptop_data
GROUP BY company;

############# 7. Bi-variate analysis

SELECT Company,
SUM(CASE WHEN Touchscreen = 1 THEN 1 ELSE 0 END) AS 'Touchscreen_yes',
SUM(CASE WHEN Touchscreen = 0 THEN 1 ELSE 0 END) AS 'Touchscreen_no'
FROM laptop_data
GROUP BY Company;
















