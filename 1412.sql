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