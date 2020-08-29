(select u.name as results
from Movie_Rating m
left join Users u
on m.user_id = u.user_id
group by u.name
order by count(m.user_id) desc, u.name
limit 1)
union all
(select m.title as results
from Movie_Rating mr
left join Movies m
on mr.movie_id = m.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by m.title
order by avg(rating) desc, m.title
limit 1)