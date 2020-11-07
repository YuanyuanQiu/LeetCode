/*select *
from UserActivity
group by username
having count(activity) = 1

union all

select username, activity, startDate, endDate
from
    (select *, rank() over(partition by username order by startDate desc) as rank1
    from UserActivity) t
where rank1 = 2*/


SELECT username, activity, startDate, endDate
from
    (SELECT
        *,
        rank() over (partition by username order by startDate desc ) as ranking,
        count(*) over (partition by username) as counting
    FROM UserActivity) as t
WHERE ranking = 2 or counting =1