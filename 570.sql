select e2.Name
from Employee2 e1, Employee2 e2
where e1.ManagerId = e2.Id
group by e2.Id
having count(e1.Name) >= 5









