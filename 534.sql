SELECT
a.player_id, a.event_date, SUM(b.games_played) AS games_played_so_far
FROM Activity AS a
INNER JOIN Activity AS b
ON a.Player_id = b.Player_id AND b.event_date <= a.event_date
GROUP BY a.player_id, a.event_date