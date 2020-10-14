select distinct s1.id, s1.visit_date, s1.people
from Stadium s1, Stadium s2, Stadium s3
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
    and (s1.id + 1 = s2.id and s2.id + 1 = s3.id
        or s2.id + 1 = s1.id and s1.id + 1 = s3.id
        or s2.id + 1 = s3.id and s3.id + 1 = s1.id)
order by s1.visit_date