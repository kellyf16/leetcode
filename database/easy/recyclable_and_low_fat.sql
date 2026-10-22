/* Write your T-SQL query statement below */
select p.product_id
from products p
where p.low_fats like 'Y' and p.recyclable like 'Y'