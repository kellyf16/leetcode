/* Write your T-SQL query statement below */
delete from person 
where id not in (
    select min(p.id)
    from person p
    group by p.email
)