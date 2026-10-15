## 1: What are the top 5 patients who claimed the highest insurance amounts?

SELECT *,
DENSE_RANK() OVER(ORDER BY claim DESC) as claim_rank
FROM insurance
LIMIT 5;

## 2: What is the average insurance claimed by patients based on the number of children they have?

SELECT DISTINCT children,
ROUND(AVG(claim) OVER(PARTITION BY children),2) as avg_claim
FROM insurance;

## 3: What is the highest and lowest claimed amount by patients in each region?
SELECT DISTINCT region,
MAX(claim) OVER(PARTITION BY region) as max_claim_region,
MIN(claim) OVER(Partition by region) as min_claim_region
FROM insurance;

## 4: What is the percentage of smokers in each age group?

SELECT t1.age,
(smoker_yes/total_num)*100 as percent_smoker
from (SELECT DISTINCT age,
COUNT(smoker) OVER(PARTITION BY age) as smoker_yes
from insurance
WHERE smoker = 'Yes') t1
JOIN (SELECT DISTINCT age,
COUNT(age) OVER(PARTITION BY age) as total_num
from insurance) t2
ON t1.age=t2.age;

## 5. What is the difference between the claimed amount of each patient and the first claimed amount of the first patient?
SELECT claim,
ROUND(claim - FIRST_VALUE(claim) OVER(),2) as diff_claim
from insurance;  

## 6. For each patient, calculate the difference between their claimed amount and 
## the average claimed amount of patients with the same number of children.

SELECT *,
ROUND(AVG(claim) OVER(PARTITION BY children),2) as avg_claim,
ROUND(claim - AVG(claim) OVER(PARTITION BY children),2) as diff_claim
FROM insurance;

## 7: Show the patient with the highest BMI in each region and their respective rank.
SELECT * FROM
  (SELECT *,
  DENSE_RANK() OVER(ORDER BY BMI DESC) as overall_rank,
  DENSE_RANK() OVER(PARTITION BY region ORDER BY BMI DESC) as rank_bmi
  FROM insurance) 
t
WHERE t.rank_bmi=1;

## 8. Calculate the difference between the claimed amount of each patient and 
## the claimed amount of the patient who has the highest BMI in their region. (Good question)

SELECt *,
FIRST_VALUE(claim) OVER(PARTITION BY region ORDER BY bmi DESC) as highest_bmi_claim_region,
claim - FIRST_VALUE(claim) OVER(PARTITION BY region ORDER BY bmi DESC) as diff
from insurance;


## 9. For each patient, calculate the difference in claim amount between patient with the highest claim amount with smoker status and 
## within the same region and each patient with the same smoker status, within the that region. 
## Return the result in descending order difference.

SELECT *, 
MAX(claim) OVER(PARTITION BY smoker,region) as max_claim,
ROUND((MAX(claim) OVER(PARTITION BY smoker,region))-claim,2) as diff_claim
FROM insurance
ORDER BY diff_claim DESC;

## 10. For each patient, find the maximum BMI value among their next three records (ordered by age). (good question)
SELECT bmi,age,
MAX(bmi) OVER(ORDER BY age ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING) as 3_follow_max_bmi
FROM insurance;

## 11. For each patient, find the rolling average of the last 2 claims. ********** (good question)
SELECT *,
AVG(claim) OVER(ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING) as avg_claim
FROM insurance;

## 12. Find the first claimed insurance value for male and female patients, within each region order the data by patient age in ascending order, 
## and only include patients who are non-diabetic and have a bmi value between 25 and 30.

SELECT * from
  (SELECT *,
  FIRST_VALUE(claim) OVER(PARTITION BY gender,region ORDER BY age) as first_value_sex_region,
  ROW_NUMBER() OVER(PARTITION BY gender,region ORDER BY age) as row_num
  FROM insurance
  WHERE diabetic = 'No' AND bmi BETWEEN 25 AND 30)as 
  t
  WHERE row_num = 1;
