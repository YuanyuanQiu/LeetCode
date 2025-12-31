SELECT 
    type AS period_state,
    MIN(date) AS start_date, -- 3. 取出这一组里的最早日期
    MAX(date) AS end_date    -- 3. 取出这一组里的最晚日期
FROM
    (
    SELECT
        type,
        date,
        -- 2. 核心魔法：生成分组 ID (diff)
        -- 如果日期是连续的 (1日, 2日, 3日)，row_number 也是连续的 (1, 2, 3)
        -- 那么 "日期 - row_number" 得到的结果就是一个固定的“基准日期”
        -- 例如：Jan 1 - 1 = Dec 31; Jan 2 - 2 = Dec 31; -> 它们会算作同一组
        SUBDATE(date, ROW_NUMBER() OVER(PARTITION BY type ORDER BY date)) AS diff
    FROM
        (
        -- 1. 数据准备：将两张表合并，并打上标签
        SELECT 'failed' AS type, fail_date AS date FROM Failed
        UNION ALL
        SELECT 'succeeded' AS type, success_date AS date FROM Succeeded
        ) t1
    ) t
-- 4. 过滤 2019 年的数据
WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
-- 5. 按照 "状态" 和 "基准日期(diff)" 分组
GROUP BY type, diff
-- 6. 按题目要求排序
ORDER BY start_date;

'''
| run_date          |   state       | ROW_NUMBER |  SUBDATE |
| ----------------- | ---------     | ---------  | -------- |
| 2018-12-28        |   failed      | 1          | Dec 27   |
| 2018-12-29        |   failed      | 2          | Dec 27   |
| 2018-12-30        |   succeeded   | 1          | Dec 29   | 
| 2018-12-31        |   succeeded   | 2          | Dec 29   |
| 2019-01-01        |   succeeded   | 3          | Dec 29   |
| 2019-01-02        |   succeeded   | 4          | Dec 29   |
| 2019-01-03        |   succeeded   | 5          | Dec 29   |
| 2019-01-04        |   failed      | 3          | Jan 01   |
| 2019-01-05        |   failed      | 4          | Jan 01   |
| 2019-01-06        |   succeeded   | 6          | Dec 31   |
| 2019-01-07        |   failed      | 5          | Jan 02   |
| 2019-01-08        |   succeeded   | 7          | Jan 01   |
'''