select sum(TIV_2016) as TIV_2016
from insurance
where TIV_2016 in (select TIV_2015
					from insurance
                    group by TIV_2015
                    having count(*) > 1)
	and concat(LAT, LON) in (select concat(lat, lon)
							from insurance
                            group by lat, lon
                            having count(*) = 1)