# Write your MySQL query statement below
select
    t1.Category,
    ifnull(sum(case when week_day = 0 then quantity else 0 end),0) as Monday,
    ifnull(sum(case when week_day = 1 then quantity else 0 end),0) as Tuesday,
    ifnull(sum(case when week_day = 2 then quantity else 0 end),0) as Wednesday,
    ifnull(sum(case when week_day = 3 then quantity else 0 end),0) as Thursday,
    ifnull(sum(case when week_day = 4 then quantity else 0 end),0) as Friday,
    ifnull(sum(case when week_day = 5 then quantity else 0 end),0) as Saturday,
    ifnull(sum(case when week_day = 6 then quantity else 0 end),0) as Sunday
from
    (select distinct item_category as Category
    from Items) t1
left join
    (select i.item_category, weekday(o.order_date) as week_day, o.quantity
    from Orders o
    join Items i
    on o.item_id = i.item_id) t2
on t1.Category = t2.item_category
group by t1.Category
order by t1.Category