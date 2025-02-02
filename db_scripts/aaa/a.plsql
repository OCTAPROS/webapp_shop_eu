SELECT c.id, c.first_name, c.last_name, c.email, c.phone_number, c.city_id, c.postal_code, c.street, c.nip, c.company_name
FROM customer_t c;


SELECT order_t.id, order_t.customer_id, order_t.order_number, order_t.payment_method, order_t.value, order_t.delivery_method, order_t.order_date, order_t.delivery_date, order_t.status, order_t.updated_at, order_t.created_at
FROM order_t
 OFFSET 0 ROWS
 FETCH FIRST 10 ROWS ONLY;

INSERT INTO ORDER_ROW_T (order_id, product_id, quantity)
VALUES
(2, 7, 4)
;

ALTER INDEX PK_ORDER_ROW_P UNUSABLE
/

DROP INDEX PK_ORDER_ROW_P
/

alter table ORDER_ROW_T add constraint PK_ORDER_ROW_UN key (order_id, product_id)
enable novalidate;
