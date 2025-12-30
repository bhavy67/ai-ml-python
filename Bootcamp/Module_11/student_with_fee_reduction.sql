use upgrad;

/*
 * Enter your query below.
 * Please append a semicolon ";" at the end of the query
 */
SELECT
    s_fee * 0.8 AS new_s_fee
FROM student
WHERE s_percentage > 90;