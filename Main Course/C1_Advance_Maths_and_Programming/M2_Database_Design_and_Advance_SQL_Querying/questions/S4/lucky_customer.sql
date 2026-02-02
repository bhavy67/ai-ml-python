SELECT 
    first_name, 
    last_name
FROM customer
WHERE first_name LIKE 'A%' 
   OR first_name LIKE 'J%' 
   OR first_name LIKE 'T%' 
   OR last_name LIKE '%on'
ORDER BY first_name ASC;