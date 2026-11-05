/* Write your T-SQL query statement below */
select ad.actor_id, ad.director_id
from actordirector ad
group by ad.actor_id, ad.director_id
having count(*) >= 3
