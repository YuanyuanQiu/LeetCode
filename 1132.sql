select round(avg(percent),2) * 100 as average_daily_percent
from (select a.action_date, count(r.post_id)/count(a.post_id) as percent
	from actions a
	left join removals r
	on a.post_id = r.post_id
	where a.action_date in (select action_date
							from actions
							where extra = 'spam')
	group by action_date) t