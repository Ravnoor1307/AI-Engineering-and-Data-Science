################################ RANKING ##########################################################

# 1. top 5 batsman of each IPL team

SELECT * FROM (SELECT BattingTeam,batter,
SUM(batsman_run) as total_runs,
DENSE_RANK() OVER(PARTITION BY BattingTeam ORDER BY SUM(batsman_run) DESC) as rank_in_team
from ipl
GROUP BY BattingTeam,batter
ORDER BY BattingTeam , total_runs DESC) as t
WHERE t.rank_in_team<6;

###################################### CUMMULATIVE SUM #########################################################

# 2. carrer runs of viart kohli after 50th, 100th match

SELECT * FROM (SELECT 
CONCAT("Match-",CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_number,
SUM(batsman_run) as 'runs_scored',
SUM(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as career_runs
from ipl
WHERE batter = 'V Kohli'
GROUP BY ID) as t
WHERE match_number IN ('Match-50','Match-100','Match-200');

################################### CUMULATIVE AVERAGE #############################################

# 3. Cummulative Avergae of V Kohli

SELECT * FROM (SELECT 
CONCAT("Match-",CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_number,
SUM(batsman_run) as 'runs_scored',
SUM(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as career_runs,
AVG(SUM(batsman_run)) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as career_average
from ipl
WHERE batter = 'V Kohli'
GROUP BY ID) as t;

########################################### MOVING AVERAGE ################################################

SELECT *
 FROM (SELECT 
CONCAT("Match-",CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_number,
SUM(batsman_run) as 'runs_scored',
SUM(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as career_runs,
AVG(SUM(batsman_run)) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as career_average,
AVG(SUM(batsman_run)) OVER (ROWS BETWEEN 9 PRECEDING AND CURRENT ROW) as moving_average
from ipl
WHERE batter = 'V Kohli'
GROUP BY ID) as t;


############################ Percent of total #####################################

SELECT f_name,
(total_value/SUM(total_value) OVER())*100 AS 'percent_of_total'
FROM 
  (SELECT f_id,SUM(amount) AS 'total_value' FROM orders t1
  JOIN order_details t2
  ON t1.order_id = t2.order_id
  WHERE r_id = 5
  GROUP BY f_id) t
JOIN food t3
ON t.f_id = t3.f_id
ORDER BY (total_value/SUM(total_value) OVER())*100 DESC;


#-------------------------------------Session 37 (Cont..) Window Functions Part 3-----------------------------------------
# use task_campusx;

## PERCENTILE NOT WORKING
-- SELECT m.*,
--        (SELECT percentile_disc(0.5) WITHIN GROUP (ORDER BY marks) FROM marks) as median_marks
-- FROM marks m;
