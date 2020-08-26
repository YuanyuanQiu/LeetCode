select distinct v1.viewer_id as id
from Views v1, Views v2
where v1.viewer_id = v2.viewer_id
	and v1.article_id != v2.article_id
    and v1.view_date = v2.view_date
order by v1.viewer_id