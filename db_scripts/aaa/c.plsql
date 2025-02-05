CREATE VIEW AAA AS 

WITH 
aa AS (
    SELECT 
    orw.order_id,
    orw.product_id,
    orw.quantity,
    orw.quantity * p.price AS order_row_value

FROM ORDER_ROW_T orw
    JOIN PRODUCT_T p ON p.ID = orw.PRODUCT_ID
),

bb AS (
    SELECT 
    aa.order_id,
    SUM(order_row_value) AS order_value
    FROM (
        SELECT 
            orw.order_id,
            orw.product_id,
            orw.quantity,
            orw.quantity * p.price AS order_row_value

        FROM ORDER_ROW_T orw
            JOIN PRODUCT_T p ON p.ID = orw.PRODUCT_ID
        )
    GROUP BY aa.order_id
)

SELECT h.*, bb.order_value
FROM ORDER_T h
JOIN bb ON bb.order_id = h.id
;


