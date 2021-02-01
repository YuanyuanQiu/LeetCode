# Method 1
select
    a.Score as score,
    (select count(distinct b.Score)
    from Scores b
    where b.Score >= a.Score) as `Rank`
from Scores a
order by a.Score desc

# Method 2
SELECT
	Score,
	DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank'
FROM Scores;