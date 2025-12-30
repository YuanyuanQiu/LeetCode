WITH cte AS (
    SELECT
        o.seller_id,
        t.item_brand,
        -- 修正点1：增加 order_id 确保排序稳定
        ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date, o.order_id) as rn
    FROM Orders o
    LEFT JOIN Items t ON o.item_id = t.item_id
)

SELECT
    u.user_id AS seller_id,
    CASE
        -- 修正点2：注意 favorite 的拼写
        -- 逻辑解释：如果 a.item_brand 是 NULL (因为没有第2单)，这里不相等，自动返回 'no'
        WHEN u.favorite_brand = a.item_brand THEN 'yes'
        ELSE 'no'
    END AS "2nd_item_fav_brand" -- 建议加上引号，因为列名以数字开头在某些DB是违规的
FROM Users u
LEFT JOIN (
    SELECT seller_id, item_brand 
    FROM cte 
    WHERE rn = 2
) a ON u.user_id = a.seller_id;