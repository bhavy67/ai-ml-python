SELECT 
    sales_id,
    product_id,
    sales_month,
    monthly_revenue,
    AVG(monthly_revenue) OVER (
        PARTITION BY product_id 
        ORDER BY sales_month
    ) AS avg_to_date
FROM Product_Sales;