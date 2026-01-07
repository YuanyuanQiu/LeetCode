-- Option 1
select student_id, student_name
from Student
where student_id in (select student_id from Exam)
and student_id not in (select student_id
                        from Exam
                        where (exam_id, score) in (select exam_id, min(score)
                                                    from Exam
                                                    group by exam_id)
                        or (exam_id, score) in (select exam_id, max(score)
                                                    from Exam
                                                    group by exam_id))

-- Option 2
WITH Ranked AS (
    SELECT 
        student_id,
        score,
        -- 正向排名：第一名是 min_score
        RANK() OVER (PARTITION BY exam_id ORDER BY score ASC) as rank_asc,
        -- 反向排名：第一名是 max_score
        RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) as rank_desc
    FROM Exam
)
SELECT DISTINCT 
    s.student_id, 
    s.student_name
FROM Student s
JOIN Ranked r ON s.student_id = r.student_id
GROUP BY s.student_id
-- 核心逻辑：该学生所有的考试记录中，都不可以是第一名(min)或最后一名(max)
HAVING SUM(CASE WHEN rank_asc = 1 OR rank_desc = 1 THEN 1 ELSE 0 END) = 0
ORDER BY s.student_id;