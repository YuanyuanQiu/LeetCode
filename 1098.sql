select b.book_id, name
from Books b
where datediff('2019-06-23',available_from) > 30
	and b.book_id not in (select book_id
							from Orders
							where datediff('2019-06-23',dispatch_date) <= 365
							group by book_id
							having sum(quantity) >= 10)