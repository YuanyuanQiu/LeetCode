select
	l1.log_id as start_id,
    l2.log_id as end_id
from
	(select log_id from Logs where log_id-1 not in (select* from Logs)) l1,
	(select log_id from Logs where log_id+1 not in (select* from Logs)) l2
where l2.log_id >= l1.log_id
group by l1.log_id