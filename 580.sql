select d.dept_name, count(s.student_id) as student_number
from department d
left join student s
on s.dept_id = d.dept_id
group by d.dept_name
order by s.student_number desc, d.dept_name