SELECT DISTINCT a.Num AS ConsecutiveNums
FROM Logs AS a
INNER JOIN Logs AS b
ON  a.Id + 1 = b.Id
INNER JOIN Logs AS c
ON a.Id + 2 = c.Id
WHERE a.Num = b.Num
AND b.Num = c.Num;