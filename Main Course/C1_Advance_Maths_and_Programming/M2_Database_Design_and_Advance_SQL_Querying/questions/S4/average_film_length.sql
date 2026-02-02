SELECT 
    ROUND(AVG(f.length)) AS avg_Length,
    c.name
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY avg_Length DESC;