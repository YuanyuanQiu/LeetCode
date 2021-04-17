select
    t1.install_dt,
    count(t1.player_id) as installs,
    round(count(t2.event_date)/count(t1.player_id),2) as Day1_retention
from
    (select player_id, min(event_date) as install_dt
    from Activity
    group by player_id) t1
left join Activity t2
on t1.player_id = t2.player_id and t1.install_dt + 1 = t2.event_date
group by t1.install_dt