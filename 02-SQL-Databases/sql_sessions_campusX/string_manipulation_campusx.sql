use campusx;

# 5 letter movie starting with 'A'

SELECT name
from movies
WHERE name LIKE 'A____';

# 

SELECt name from movies
WHERE name like '%man%';

SELECT concat_ws(' @ ',name,director,writer)
FROM movies;

# 5th letter and onwards
Select name, substr(name,5)
from movies;

# 5th to 10th letter
Select name, substr(name,5,5)
from movies;

# last letter
select name, substr(name,-1)
from movies;

# from last 3 letter onwards
select name, substr(name,-3)
from movies;

# last 3rd last and 2nd last letter
select name, substr(name,-3,2)
from movies;

# last 3rd last letter
select name, substr(name,-3,1)
from movies;

# REPLACE
SELECT REPLACE("Hello world","world","India") as replaced_value;

# replace man with woman
SELECT name,REPLACE(name,"man","wom@n") as man_replaced
from movies
WHERE name like '%man%';

# reversing string
SELECT REVERSE("Hello");

# palindrome movie name
SELECT lower(name), lower(reverse(name)) as reversed_name
from movies
WHERE name= reverse(name); 

# char_length and length
SELECT name, char_length(name) as `char_length`,length(name) as `length`
from movies
WHERE char_length(name)!=length(name)
AND length(name) - char_length(name)> 1;

# insert and replace
SELECT INSERT("hello world",7,5,"india") as inset_edited;

# insert without replace
SELECT INSERT("hello world",7,0,"india") as inset_edited;

# first 3 charcaters using LEFT

SELECT name, LEFT(name, 3)
FROM movies;

# Last 3 charcaters using RIGHT

SELECT name, RIGHT(name, 3)
FROM movies;

# Repeat
SELECT repeat(name,3)
from movies;

# trim
SELECT TRIM('   mohit          kr                ') as trimmed;

select LENGTH("           mohit kumar         ") as original_length,
length(LTRIM("           mohit kumar         ")) as left_trimmed,
length(RTRIM("           mohit kumar         ")) as right_trimmed;

select substring_index("www.campusx.com",".",1) as `1st_occurence`,
substring_index("www.campusx.com",".",2) as `2nd_occurence`,
substring_index("www.campusx.com",".",3) as `3rd_occurence`;

select substring_index("www.campusx.com",".",-1) as `last_occurence`,
substring_index("www.campusx.com",".",-2) as `last_and_2nd_last_occurence`,
substring_index("www.campusx.com",".",-3) as `3rd_last_2nd_last__and_last_occurence`;

SELECT TRIM(BOTH '-' FROM '------------mohit          kr----------') as trimmed;

SELECT STRCMP("Delhi","Ahmedabad"), STRCMP("Ahmedabad","Mumbai");

SELECT locate("world","hello world");

SELECT LPAD('8888888888',13,'+91');

SELECT RPAD("mohit", 15, '_'), char_length(RPAD("mohit", 15, '_')), RPAD("mohit kumar", 15, '_'),char_length(RPAD("mohit kumar", 15, '_'));