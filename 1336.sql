with RECURSIVE f(n) as (select 0 as n
                    union all
                    select n + 1 as n
                    from f
                    where n < (select count(*) from Transactions)),
a as (select
        v.user_id,
        count(t.transaction_date) as transactions_count
        from Visits v
        left join Transactions t
        on v.user_id = t.user_id and v.visit_date = t.transaction_date
        group by v.user_id, v.visit_date)


select f.n as transactions_count, count(a.user_id) as visits_count
from f
left join a
on f.n = a.transactions_count
where f.n <= (select max(transactions_count) from a)
group by f.n
order by f.n