select round(sqrt(min(power((p2.x - p1.x),2) + power((p2.y - p1.y),2))),2) as shortest
from point_2d p1, point_2d p2
where p1.x <> p2.x or p1.y <> p2.y