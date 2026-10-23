/* Write your T-SQL query statement below */
select (max(x.sum) - min(x.sum)) as difference_in_score
from (
    select (s.assignment1 + s.assignment2 + s.assignment3) as [sum]
    from scores s
) x
