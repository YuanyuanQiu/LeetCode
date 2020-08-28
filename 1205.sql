select
	month,
	country,
	count(case when state='approved' and tag=1 then 1 end) as approved_count,
	sum(case when tag=1 then amount else 0 end) as approved_amount,
	count(case when tag=0 then 1 end) as chargeback_count,
	sum(case when tag=0 then amount else 0 end) as chargeback_amount
from (select country,state,amount,date_format(trans_date,"%Y-%m") as month,1 as tag
		from Transactions
		where state='approved'
		union all
		select country,state,amount,date_format(c.trans_date,"%Y-%m") as month,0 as tag
		from Transactions t
        right join Chargebacks c
		on c.trans_id=t.id) as a
group by month,country;
