-- 1. Show records of 'male' patient from 'southwest' region.

SELECT * from insurance 
WHERE gender = 'male' AND region = 'southwest';

-- 2. Show all records having bmi in range 30 to 45 both inclusive. 
SELECT * from insurance
WHERE bmi >= 30 AND bmi <= 45;
              -- OR -- 
SELECT * from insurance
WHERE bmi between 30 AND 45;

-- 3. Show minimum and maximum bloodpressure of diabetic patient who smokes. Make column names as MinBP and MaxBP respectively.

SELECT MIN(bloodpressure) as MinBP, MAX(bloodpressure) as MaxBP
FROM insurance
WHERE diabetic = 'Yes' AND smoker = 'Yes';

-- 4. Find no of unique patients who are not from southwest region.

SELECT count(*) as unique_patients
FROM insurance
WHERE region!= 'southwest';

-- 5. Total claim amount from male smoker.

SELECT SUM(claim)
FROM insurance
where gender = 'male' AND smoker = 'Yes';

-- 6. Select all records of south region.
SELECT *
FROM insurance
WHERE region like 'south%';

-- 7. No of patient having normal blood pressure. Normal range[90-120]

select COUNT(*)
FROM insurance
WHERE bloodpressure BETWEEN 90 AND 120;

-- 8. No of pateint belo 17 years of age having normal blood pressure as per below formula - 
              -- BP normal range = 80+(age in years × 2) to 100 + (age in years × 2)

SELECT COUNT(*) from insurance
where AGE <17 
AND (bloodpressure BETWEEN 80 + (age * 2) AND 100 + (age * 2)); 
          
-- 9. What is the average claim amount for non-smoking female patients who are diabetic?

SELECT AVG(claim)
FROM insurance
WHERE
gender = 'female' 
AND smoker = 'NO' 
AND diabetic = 'Yes';

-- 10. Write a SQL query to update the claim amount for the patient with PatientID = 1234 to 5000.

UPDATE insurance
SET claim = 5000
WHERE PatientID = '1234';


-- 11. Write a SQL query to delete all records for patients who are smokers and have no children.
-- DELETE from insurance
-- where smoker = 'Yes' AND children = 0;