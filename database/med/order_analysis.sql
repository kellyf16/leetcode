SET NOCOUNT ON;


/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
select x.order_type, x.product_name, x.total_orders, round(x.average_order_price, 2) as average_order_price
from (
    select order_type, agg.product_name, count(agg.price) as total_orders, avg(agg.price) as average_order_price, row_number() over (partition by order_type order by avg(agg.price) desc) as r_num
    from ((select *, 'buy' as order_type from buy_orders) 
    union all (select *, 'sell' as order_type from sell_orders)) as agg
    where agg.dt like "2024-02%"
    group by order_type, agg.product_name
) as x
where r_num <= 3
order by order_type asc, average_order_price desc;

go