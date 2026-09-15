/* Write your T-SQL query statement below */
select c.class
from courses c
group by c.class
having count(c.student) >= 5