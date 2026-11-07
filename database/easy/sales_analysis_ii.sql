/* Write your T-SQL query statement below */
select x.buyer_id
from sales x left join product y on x.product_id = y.product_id
where x.buyer_id not in (
    select s.buyer_id
    from sales s left join product p on s.product_id = p.product_id
    where p.product_name = 'iPhone'
) and y.product_name = 'S8'
group by x.buyer_id
