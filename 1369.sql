-- select *
-- from UserActivity
-- group by username
-- having count(*) = 1

-- union all

-- select u1.username, u1.activity, u1.startDate, u1.endDate
-- from UserActivity u1, UserActivity u2
-- where u1.username = u2.username and u1.startDate <= u2.startDate
-- group by u1.username, u1.startDate
-- having count(u2.startDate) = 2


-- select *
-- from UserActivity
-- group by username
-- having count(activity) = 1

-- union all

-- select username, activity, startDate, endDate
-- from
--     (select *, rank() over(partition by username order by startDate desc) as rank1
--     from UserActivity) t
-- where rank1 = 2


SELECT username, activity, startDate, endDate
from
    (SELECT
        *,
        rank() over (partition by username order by startDate desc ) as ranking,
        count(*) over (partition by username) as counting
    FROM UserActivity) as t
WHERE ranking = 2 or counting =1