select
	t.team_id,
    t.team_name,
    sum(CASE
			WHEN t.team_id= m.host_team and m.host_goals>m.guest_goals THEN 3
			WHEN m.host_goals = m.guest_goals THEN 1
			WHEN t.team_id = m.guest_team and m.guest_goals>m.host_goals THEN 3
			ELSE 0
        END) as num_points 
from Teams t 
left join Matches m 
on t.team_id = m.host_team or t.team_id = m.guest_team 
group by t.team_id 
order by num_points desc ,team_id asc