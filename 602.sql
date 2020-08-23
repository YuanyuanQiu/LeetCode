select t1.id, COUNT(*) as num
from
   (select requester_id as id from request_accepted
    UNION ALL
    select accepter_id as id from request_accepted) as t1
group by t1.id
order by num desc
limit 1