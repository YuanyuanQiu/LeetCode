SELECT ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM
	Activity AS a
LEFT JOIN
	(SELECT player_id, MIN(event_date) AS first_login
	FROM Activity
	GROUP BY player_id) AS b
ON a.player_id = b.player_id
AND DATEDIFF(a.event_date, b.first_login) = 1