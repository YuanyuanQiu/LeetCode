select
    t1.pay_month,
    department_id,
    (case
        when t1.dept_avg > t2.all_avg then 'higher'
        when t1.dept_avg = t2.all_avg then 'same'
        when t1.dept_avg < t2.all_avg then 'lower'
    end) as comparison
from
    (select date_format(s.pay_date,'%Y-%m') as pay_month, e.department_id, avg(amount) as dept_avg
    from salary s
    join employee e
    on s.employee_id = e.employee_id
    group by pay_month, e.department_id) t1, 
    (select date_format(pay_date,'%Y-%m') as pay_month, avg(amount) as all_avg
    from salary s
    group by pay_month) t2
where t1.pay_month = t2.pay_month
order by pay_month desc, department_id