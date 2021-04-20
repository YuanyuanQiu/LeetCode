# structure
with
RECURSIVE f(n) as(select 1
                    union all
                    select n+1 from f where n < 12),
# available driver
a1 as (select
            driver_id,
            date_format(join_date,'%Y-%m') as join_month,
            count(driver_id) as amount
        from drivers
        where date_format(join_date,'%Y-%m')<'2021-01'
        and date_format(join_date,'%Y-%m')>='2020-01'
        group by join_month
        order by join_month),
a2 as(select '2020-01' as join_month,count(driver_id) as amount
        from drivers
        where date_format(join_date,'%Y-%m')<'2020-01'
        union all 
        select join_month,amount from a1),
a3 as (select join_month, sum(amount) as amount
        from a2
        group by join_month),
# structure + available driver
b as (select n as join_month,
        ifnull(amount,0) as sm
        from f
        left join a3 
        on month(CONCAT(join_month,'-01'))=f.n),
b1 as (select join_month, sum(sm) over (order by join_month) as sm 
        from b),
# working driver
c1 as (select
        a.ride_id,
        a.driver_id,
        date_format(requested_at,'%Y-%m') as accept_month
    from acceptedRides a
    left join rides r
    on r.ride_id=a.ride_id
    where requested_at like '2020%'
    and a.driver_id in (select driver_id
                        from drivers
                        where date_format(join_date,'%Y-%m') <= date_format(r.requested_at,'%Y-%m'))
    order by accept_month),
c2 as (select * from c1 group by accept_month,driver_id),
c3 as(select month(CONCAT(accept_month,'-01')) as accept_month, count(ride_id) as sn
    from c2
    group by accept_month),
# structure + working driver
d as (select
        n as month,
        ifnull(sm ,0) as active_drivers,
        ifnull(sn,0) as accepted_rides 
    from f
    left join b1
    on b1.join_month=f.n
    left join c3
    on c3.accept_month=f.n)

select
    month,
    if(accepted_rides=0,0,round(accepted_rides/active_drivers*100,2)) as working_percentage
from d