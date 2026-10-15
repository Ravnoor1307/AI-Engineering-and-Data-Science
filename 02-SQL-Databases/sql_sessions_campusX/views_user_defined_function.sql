use flights;

select * from flights_data;

CREATE VIEW indigo AS
SELECT * FROM flights_data
WHERE airline='Indigo';

SELECT * from indigo;

select * from persons; 

SET GLOBAL log_bin_trust_function_creators = 1;

select hello_world() as message;

select *, calculate_age(dob) from persons; 

select *, proper_title(first_name,gender,married) as title_name from persons; 

select *, format_date(DOB) from persons;

select flights_count('Banglore','New Delhi');

################################################ STORED PROCEDURE #################################
SET @message = '';
CALL add_user('mkr','mkru898',@message);

SELECT @message;
select * from users;

CALL user_orders('daniel.wilson@example.com');




