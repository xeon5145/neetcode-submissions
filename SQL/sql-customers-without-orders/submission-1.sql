-- Write your query below
SELECT C.name FROM customers as C LEFT JOIN orders as O ON O.customer_id = C.id WHERE O.customer_id IS NULL;