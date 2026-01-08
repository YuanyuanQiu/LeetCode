-- Option 1
WITH RECURSIVE f(n) AS
(SELECT 1
UNION ALL
SELECT n + 1 FROM f WHERE n < 20)

SELECT task_id, n AS subtask_id 
FROM Tasks, f -- 笛卡尔积 + 过滤
WHERE subtasks_count >= n
AND (task_id, n) NOT IN (SELECT * FROM Executed)
ORDER BY task_id, n

-- Option 2
WITH RECURSIVE AllSubtasks AS (
    -- Anchor Member: Start with subtask 1 for all tasks
    SELECT 
        task_id, 
        subtasks_count, 
        1 AS subtask_id
    FROM Tasks
    
    UNION ALL
    
    -- Recursive Member: Increment subtask_id until we reach subtasks_count
    SELECT 
        task_id, 
        subtasks_count, 
        subtask_id + 1
    FROM AllSubtasks
    WHERE subtask_id < subtasks_count
)

SELECT 
    a.task_id, 
    a.subtask_id
FROM AllSubtasks a
LEFT JOIN Executed e 
    ON a.task_id = e.task_id AND a.subtask_id = e.subtask_id
WHERE e.subtask_id IS NULL;