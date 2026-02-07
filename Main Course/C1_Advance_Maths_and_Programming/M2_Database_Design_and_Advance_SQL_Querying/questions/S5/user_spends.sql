SELECT 
    payment_id,
    user_id,
    payment_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY user_id 
        ORDER BY payment_date
    ) AS running_total
FROM Payments;