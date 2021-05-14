# Don't know which continent has the most students
select
    max(case when continent = 'America' then name else null end) America,
    max(case when continent = 'Asia' then name else null end) Asia,
    max(case when continent = 'Europe' then name else null end) Europe
from
    (select 
        name, 
        continent, 
        row_number() over (partition by continent order by name) cur_rank
    from
        student)t 
group by cur_rank