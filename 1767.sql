WITH RECURSIVE f(n) AS
(SELECT 1
UNION ALL
SELECT n + 1 FROM f WHERE n < 20)

SELECT task_id, n AS subtask_id 
FROM Tasks, f
WHERE subtasks_count >= n
AND (task_id, n) NOT IN (SELECT * FROM Executed)
ORDER BY task_id, n