-- Option 1
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

-- Option 2
with RECURSIVE 
-- 1. 先算出实际数据的统计所有user单次visit的transactions_count (你的 CTE a)
ActualStats as (
    select count(t.transaction_date) as cnt
    from Visits v
    left join Transactions t
    on v.visit_date = t.transaction_date and v.user_id = t.user_id
    group by v.user_id, v.visit_date
),
-- 2. 生成序列 (你的 CTE f)，但优化上限逻辑
Seq(n) as (
    select 0 
    union all -- 优化点1：使用 UNION ALL
    select n + 1 
    from Seq
    -- 优化点2：直接在这里限制递归深度，而不是生成后再在主查询过滤
    -- 这样如果最大值是5，递归就只跑5次，不会跑100万次
    where n < (select max(cnt) from ActualStats) 
)

select 
    Seq.n as transactions_count, 
    count(ActualStats.cnt) as visits_count
from Seq
left join ActualStats
on Seq.n = ActualStats.cnt
group by Seq.n
order by Seq.n;