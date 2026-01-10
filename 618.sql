-- Option 1
WITH Student_rn AS (
    SELECT
        name,
        continent,
        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rn
    FROM Student
)
SELECT
    s1.name AS America,
    s2.name AS Asia,
    s3.name AS Europe
FROM (SELECT * FROM Student_rn WHERE continent = 'America') s1
LEFT JOIN (SELECT * FROM Student_rn WHERE continent = 'Asia') s2
ON s1.rn = s2.rn
LEFT JOIN (SELECT * FROM Student_rn WHERE continent = 'Europe') s3
ON s1.rn = s3.rn

-- Option 2
SELECT 
    MAX(CASE WHEN continent = 'America' THEN name END) AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM (
    SELECT 
        name, 
        continent, 
        -- 核心步骤：给每个洲内部的人按名字排序并编号
        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) as rn
    FROM Student
) t
GROUP BY rn;