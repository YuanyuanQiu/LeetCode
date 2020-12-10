# Method 1
select
    a.Score as score,
    (select count(distinct b.Score)
    from Scores b
    where b.Score >= a.Score) as `Rank`
from Scores a
order by a.Score desc

# Method 2
select s1.score, s2.Rank
from 
    Scores s1
left join 
    (select score, dense_rank() over (order by score desc) as 'Rank'
    from
        (select distinct score
        from Scores) t) s2
on s1.score = s2.score
order by s1.score desc