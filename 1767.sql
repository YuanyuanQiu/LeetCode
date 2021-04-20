WITH RECURSIVE a AS
(SELECT 1 AS k
UNION ALL
SELECT k+1 FROM a 
WHERE k<20)

SELECT task_id, k AS subtask_id 
FROM Tasks, a
WHERE subtasks_count>=k
AND (task_id, k) NOT IN (SELECT * FROM Executed)
ORDER BY task_id, k