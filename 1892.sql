WITH AllFriends AS (
    SELECT user1_id AS u, user2_id AS f FROM Friendship
    UNION ALL
    SELECT user2_id AS u, user1_id AS f FROM Friendship
)
SELECT 
    af.u AS user_id, 
    l.page_id, 
    COUNT(DISTINCT af.f) AS friends_likes
FROM AllFriends af
-- 1. Get pages liked by friends (INNER JOIN removes NULLs)
INNER JOIN Likes l ON af.f = l.user_id
-- 2. Exclude pages the user already likes (Left Join Exclusion)
LEFT JOIN Likes own_l ON af.u = own_l.user_id AND l.page_id = own_l.page_id
WHERE own_l.page_id IS NULL
GROUP BY af.u, l.page_id;