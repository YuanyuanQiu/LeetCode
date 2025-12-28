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