/* Write your T-SQL query statement below */
select s.score, dense_rank() over (order by s.score desc) as [rank]
from scores s

