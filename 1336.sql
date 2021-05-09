with RECURSIVE f(n) as (select 0 as n
                        union
                        select n + 1 as n
                        from f
                        where n < (select count(*) from Transactions)),
a as (select
        count(t.transaction_date) as cnt
    from Visits v
    left join Transactions t
    on v.visit_date = t.transaction_date and v.user_id = t.user_id
    group by v.user_id, v.visit_date)

select
    f.n as transactions_count, count(cnt) as visits_count
from f
left join a
on f.n = a.cnt
where f.n <= (select max(cnt) from a)
group by f.n
order by f.n