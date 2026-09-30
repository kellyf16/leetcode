/* Write your T-SQL query statement below */
select sp.name
from salesperson sp
where sp.sales_id not in (
    select s.sales_id
    from salesperson s inner join orders o on s.sales_id = o.sales_id inner join company c on o.com_id = c.com_id
    where c.name = 'RED'
) 
