-- Option 1
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


-- Option 2
WITH RECURSIVE years AS (
    -- 1. 种子：从最小年份开始
    SELECT MIN(YEAR(period_start)) as year FROM Sales
    UNION ALL
    -- 2. 递归：自动一直加到最大年份
    SELECT year + 1
    FROM years
    WHERE year < (SELECT MAX(YEAR(period_end)) FROM Sales)
),
formatted_years AS (
    -- 把数字年份转成起止日期
    SELECT 
        CAST(year AS CHAR) as report_year,
        CONCAT(year, '-01-01') as year_start,
        CONCAT(year, '-12-31') as year_end
    FROM years
)
    s.product_id,
    p.product_name,
    y.report_year,
    -- 核心优化：直接计算重叠天数 * 日均销量
    (DATEDIFF(
        LEAST(s.period_end, y.year_end),           -- 横向比较，取结束时间取较早的
        GREATEST(s.period_start, y.year_start)     -- 横向比较，取开始时间取较晚的
    ) + 1) * s.average_daily_sales AS total_amount
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
JOIN formatted_years y 
    -- 这里用 ON 直接过滤掉完全不沾边的年份，替代最后的 WHERE total <> 0
    ON s.period_start <= y.year_end 
    AND s.period_end >= y.year_start
ORDER BY s.product_id, y.report_year;