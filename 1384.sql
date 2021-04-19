-- (select
--     Sales.product_id,
--     product_name,
--     '2018' as 'report_year',
--     if(period_start<'2019-01-01', (datediff(if(period_end<'2019-01-01', period_end, date('2018-12-31')), if(period_start>='2018-01-01', period_start, date('2018-01-01')))+1)*average_daily_sales, 0) as total_amount
-- from Sales  
-- join Product
-- on Sales.product_id = Product.product_id 
-- having total_amount>0)

-- union

-- (select
-- 	Sales.product_id,
--     product_name,
--     '2019' as 'report_year',
--     if( period_start<'2020-01-01', (datediff(if(period_end<'2020-01-01', period_end, date('2019-12-31')), if(period_start>='2019-01-01', period_start, date('2019-01-01')))+1)*average_daily_sales , 0) as total_amount
-- from Sales  
-- join Product
-- on (Sales.product_id = Product.product_id )
-- having total_amount>0)

-- union

-- (select
-- 	Sales.product_id,
--     product_name,
--     '2020' as 'report_year',
--     (datediff(if(period_end<'2021-01-01', period_end, date('2020-12-31')), if(period_start>='2020-01-01', period_start, date('2020-01-01')))+1)*average_daily_sales as total_amount
-- from Sales  
-- join Product
-- on (Sales.product_id = Product.product_id)
-- having total_amount>0)

-- order by product_id, report_year


select t.product_id, p.product_name, t.report_year, t.total_amount
from
    (select
        product_id,
        '2018' as report_year,
        average_daily_sales * (case
            when period_end >= '2019-01-01' then datediff('2019-01-01', period_start)
            when period_end < '2019-01-01' then datediff(period_end, period_start)+1
            else 0 end) as total_amount
    from Sales
    where period_start < '2019-01-01'

    union all
    select
        product_id,
        '2019' as report_year,
        average_daily_sales * (case
            when period_start >= '2019-01-01' and period_end >= '2020-01-01' then datediff('2020-01-01', period_start)
            when period_start >= '2019-01-01' and period_end < '2020-01-01' then datediff(period_end, period_start)+1
            when period_start < '2019-01-01' and period_end >= '2020-01-01' then datediff('2020-01-01', '2019-01-01')
            when period_start < '2019-01-01' and period_end < '2020-01-01' then datediff(period_end, '2019-01-01')+1
            else 0 end) as total_amount
    from Sales
    where period_start < '2020-01-01'

    union all
    select
        product_id,
        '2020' as report_year,
        average_daily_sales * (case
            when period_start >= '2020-01-01' then datediff(period_end, period_start)+1
            when period_start < '2020-01-01' then datediff(period_end, '2020-01-01')+1
            else 0 end) as total_amount
    from Sales
    where period_end >= '2020-01-01'
    ) t
join Product p
on t.product_id = p.product_id
where t.total_amount > 0
order by product_id, report_year