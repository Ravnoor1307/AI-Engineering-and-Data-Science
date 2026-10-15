# 1. highest grossing movies
SELECT * from movies
WHERE (gross-budget) = (select
MAX(gross-budget)
FROM movies);

# 2. Find how many movies have a rating > the avg of all the movie ratings(Find the count of above average movies)

SELECT COUNT(*) 
FROM movies
WHERE score > (SELECT AVG(score) FROM movies);

# 3. Find all movies of all those actors whose filmography's avg rating > 8.5(take 25000 votes as cutoff)

select * from movies 
where star IN (SELECT star from movies
WHERE votes > 25000
GROUP BY star
HAVING AVG(score)>8.5);

# 4. Find the most profitable movie of each year
SELECT * FROM movies
WHERE (year,gross - budget) IN
(select year,max(gross - budget) as profit from movies
GROUP BY year);

# 5. Find the highest grossing movies of top 5 actor/director combo in terms of total gross income

SELECT star,director,
MAX(gross) as profit
FROM movies
GROUP BY star,director
ORDER BY profit DESC
LIMIT 5;

# 6. Find all the movies that have a rating higher than the average rating of movies in the same genre.[Animation]


Select * from movies m1
WHERE score > (Select AVG(score) from movies m2 
                where m1.genre=m2.genre);

# 7. Get the percentage of votes for each movie compared to the total number of votes.
SELECT
name, 
SUM(votes),
ROUND(SUM(votes)/(SELECT SUM(votes) from movies),4)*100 as percent
from movies
GROUP BY name;

# 8. Display all movie names ,genre, score and avg(score) of genre

SELECT name,genre,score,(SELECT
ROUND(AVG(score),3)
FROM movies m2
GROUP By genre
HAVING m1.genre = m2.genre) as avg_genre
FROM movies m1;

SELECT name,genre,score,(SELECT
ROUND(AVG(score),3)
FROM movies m2
WHERE m1.genre = m2.genre) as avg_genre
FROM movies m1;