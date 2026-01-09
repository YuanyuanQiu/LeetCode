WITH FrequencyStats AS (
    SELECT
        num,
        frequency,
        -- Running sum from top (0, 1, 2...)
        SUM(frequency) OVER (ORDER BY num ASC) as asc_acc,
        -- Running sum from bottom (3, 2, 1...)
        SUM(frequency) OVER (ORDER BY num DESC) as desc_acc,
        -- Total sum
        SUM(frequency) OVER () as total_cnt
    FROM Numbers
)
SELECT 
    AVG(num) as median
FROM FrequencyStats
WHERE asc_acc >= total_cnt / 2.0 
  AND desc_acc >= total_cnt / 2.0;