use mohitdb;

select hello_world();

SET GLOBAL log_bin_trust_function_creators = 1;
select * from diab;

select *, bmi(BMI) from diab;

select *, preg_outcome(Pregnancies, Age) from diab;

select *, diab_or_not(Glucose) from diab;

select *, age_less_more(20,50) from diab;

select AVG(Age) from diab
WHERE Pregnancies = 10;

select *,preg_age(10) from diab;

select * from diab;

select preg_out(0,1) from diab;

select factorial(-2);

select GetNthFibonacciNumber(5);

select BMI*1000 from diab
where BloodPressure = 72 AND Insulin = 0 AND Age = 50;

select * from diab;



CALL glucose(50);

CALL update_BMI(72, 0, 50);

CALL generate_blood_glucose_report();

CALL preg_glucose(2);