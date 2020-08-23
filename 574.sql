select c.Name
from Candidate c, Vote v
where c.id = v.CandidateId
group by c.id
order by count(v.id) desc
limit 1