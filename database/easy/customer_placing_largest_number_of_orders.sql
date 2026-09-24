/* Write your T-SQL query statement below */
select top 1 o.customer_number
from orders o
group by o.customer_number
order by count(o.order_number) desc