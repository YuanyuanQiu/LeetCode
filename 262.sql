select
    Request_at as 'Day',
    round(avg(Status !='completed'),2) as 'Cancellation Rate'
from Trips
where Request_at between '2013-10-01' and '2013-10-03'
    and Driver_Id not in (select Users_Id from Users where Banned = 'Yes')
    and Client_Id not in (select Users_Id from Users where Banned = 'Yes')
group by Request_at