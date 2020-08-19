select
	left_operand,
    operator,
    right_operand, 
	case when (l-r>0 and operator='>')
		or(l=r and operator='=')
		or(l-r<0 and operator='<') then 'true'
		else 'false'
	end as 'value'
from
	(select e.left_operand, e.operator, e.right_operand, v1.value l, v2.value r
    from Expressions e
    left join Variables v1
	on e.left_operand = v1.name
    left join Variables v2
	on e.right_operand = v2.name) t