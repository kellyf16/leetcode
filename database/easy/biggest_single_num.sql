/* Write your T-SQL query statement below */
select max(n.num) as num
from (
    select m.num, count(m.num) as c
    from mynumbers m
    group by m.num
) as n
where n.c = 1
