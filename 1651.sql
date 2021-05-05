# Write your MySQL query statement below
with RECURSIVE f(n) as (select 1
                        union all
                        select n+1 from f
                        where n < 12),
a as (select
        month(r.requested_at) as month,
        sum(a.ride_distance) as ride_distance,
        sum(a.ride_duration) as ride_duration
    from Rides r
    join AcceptedRides a
    on r.ride_id = a.ride_id
    where r.requested_at >= '2020-01-01' and r.requested_at < '2021-01-01'
    group by month
    order by month),
b as (select
        f.n as month,
        ifnull(a.ride_distance,0) as ride_distance,
        ifnull(a.ride_duration,0) as ride_duration
    from f
    left join a
    on f.n = a.month)

select *
from
    (select
        month,
        round((sum(ride_distance) over(order by month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING))/3, 2) as average_ride_distance,
        round((sum(ride_duration) over(order by month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING))/3, 2) as average_ride_duration
    from b
    group by month
    order by month)t
where month < 11