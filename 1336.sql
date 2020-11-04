with 
t1 as # join两个table后的结果
(select v.user_id,v.visit_date,ifnull(amount,0) as amount
from Visits as v
left join Transactions as t
on v.visit_date = t.transaction_date and v.user_id = t.user_id),

t2 as # 从t1处得到每个类别的count. 用tag区分transactions_count次数(为0时tag=1，为>0时tag=0)
(select if(tag=0,cnt,0) as transactions_count, count(cnt) as visits_count
from
    (select tag, user_id,count(amount) as cnt
    from (select *, if(amount=0,1,0) as tag
          from t1) as b
    group by user_id, visit_date, tag) as a
group by cnt, tag),

t3 as # t3用两个table union后生成一列连续数字用于填补漏掉的index
(select row_number() over () - 1 as rn
from
    (select user_id from Visits
    union all
    select user_id from Transactions) as a)

select
    ifnull(transactions_count,rn) as transactions_count,
    ifnull(visits_count,0) as visits_count 
from t3 left join t2
on t2.transactions_count = t3.rn
where rn <= (select max(transactions_count) from t2)