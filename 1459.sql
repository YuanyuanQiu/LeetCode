select
	po1.id as p1,
    po2.id as p2,
    abs(po1.x_value - po2.x_value) *  abs(po1.y_value - po2.y_value) as area
from Points po1, Points po2
where po1.x_value != po2.x_value
	and po1.y_value != po2.y_value
    and po1.id < po2.id
order by area desc, p1, p2