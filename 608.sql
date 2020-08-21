select t1.id, (case
					when t1.p_id is null then 'Root'
					when t2.id is null then 'Leaf'
					else 'Inner'
				end) as Type
from tree t1
left join tree t2
on t1.id = t2.p_id
group by t1.id
