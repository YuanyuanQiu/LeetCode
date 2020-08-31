select
	i.invoice_id,
    c.customer_name,
    i.price,
    c.contacts_cnt
    c.trusted_contacts_cnt
from Invoices i
left join (select customer_id,
					customer_name,
                    count(user_id) as contacts_cnt,
                    sum(case
							when contact_name in (select customer_name from Customers) then 1 else 0
						end) as trusted_contacts_cnt
			from Customers
            left join Contacts
            on customer_id = user_id
            group by cu.customer_id) c
on i.user_id = c.customer_id
group by i.invoice_id
order by i.invoice_id