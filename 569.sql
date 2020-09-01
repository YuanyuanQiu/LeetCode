SELECT Id, Company, Salary
FROM Employee
WHERE Id in (
    SELECT e1.Id
    FROM Employee e1
    JOIN Employee e2
    ON e1.Company = e2.Company
    GROUP BY e1.Id
    HAVING SUM(CASE WHEN e1.Salary >= e2.Salary THEN 1 ELSE 0 END) >= COUNT(*)/2 
    AND SUM(CASE WHEN e1.Salary <= e2.Salary THEN 1 ELSE 0 END) >= COUNT(*)/2
    )
GROUP BY Company, Salary
ORDER BY Company