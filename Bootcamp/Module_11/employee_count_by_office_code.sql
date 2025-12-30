use upgrad;

# Write your code below
SELECT
    officeCode,
    COUNT(employeeNumber) AS no_Of_Employees
FROM Employees
GROUP BY officeCode
ORDER BY officeCode ASC;