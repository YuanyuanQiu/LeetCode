select
	user_id,
    user_name,
    round(avg(credit) + ifnull(sum(if(user_id = paid_to, 1, -1) * amount),0),0) credit,
    if(avg(credit) + ifnull(sum(if(user_id = paid_to, 1, -1) * amount),0) < 0, 'Yes', 'No') credit_limit_breached
from Users
left join Transactions
on user_id = paid_by or user_id = paid_to
group by user_id