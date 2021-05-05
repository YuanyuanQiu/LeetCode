# Write your MySQL query statement below
with recursive f(n) as (select 1 as n
                        union
                        select n + 1 as n
                        from f
                        where n < 12),

a as (select month, sum(cnt) as active_drivers
        from
            (select 1 as month, count(driver_id) as cnt
            from Drivers
            where join_date < '2020-01-01'
            union all
            select month(join_date) as month, count(driver_id) as cnt
            from Drivers
            where join_date >= '2020-01-01' and join_date < '2021-01-01'
            group by month) t
        group by month
        order by month),
b as (select
        month(r.requested_at) as month,
        count(r.ride_id) as accepted_rides
    from Rides r
    join AcceptedRides a
    on r.ride_id = a.ride_id
    where requested_at between '2020-01-01' and '2020-12-31'
    group by month),
c as
(select
    f.n as month,
    ifnull(a.active_drivers, 0) as active_drivers,
    ifnull(b.accepted_rides, 0) as accepted_rides
from f
left join a on f.n = a.month
left join b on f.n = b.month
order by month)

select month, sum(active_drivers) over(order by month) as active_drivers, accepted_rides
from c
group by month