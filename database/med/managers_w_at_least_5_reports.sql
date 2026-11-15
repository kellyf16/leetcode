/* Write your T-SQL query statement below */
select m.name
from employee e inner join employee m on e.managerId = m.id
group by m.name, m.id
having count(*) >= 5