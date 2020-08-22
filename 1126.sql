select business_id 
from Events
join (select event_type, avg(occurences) avg_occ
    from Events 
    group by event_type) as temp
on events.event_type = temp.event_type and events.occurences > temp.avg_occ
group by business_id
having count(*)>1