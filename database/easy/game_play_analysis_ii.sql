/* Write your T-SQL query statement below */
select a.player_id, a.device_id 
from activity a
where a.event_date = (
    select min(a2.event_date)
    from activity a2
    where a2.player_id = a.player_id
)