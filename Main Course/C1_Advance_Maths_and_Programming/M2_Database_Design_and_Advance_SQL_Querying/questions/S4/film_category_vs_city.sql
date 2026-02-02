SELECT 
    c.name AS name, 
    ci.city, 
    COUNT(*) AS category_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN store s ON i.store_id = s.store_id
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
GROUP BY c.name, ci.city
ORDER BY category_count DESC;