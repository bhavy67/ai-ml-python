SELECT 
    MONTH(payment_date) AS Payment_month, 
    COUNT(payment_id) AS No_of_payments
FROM payment
GROUP BY Payment_month
ORDER BY No_of_payments DESC
LIMIT 1;