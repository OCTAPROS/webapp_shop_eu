CREATE OR REPLACE VIEW "WEBSTORE"."REPORT1_V"  AS 
  WITH 
rows_calc AS (
    SELECT 
    orw.order_id,
    orw.product_id,
    orw.quantity,
    NVL(orw.quantity, 0) * NVL(p.price, 0) AS order_row_value

FROM ORDER_ROW_T orw
    JOIN PRODUCT_T p ON p.ID = orw.PRODUCT_ID
),

order_totals AS (
    SELECT 
    rows_calc.order_id,
    SUM(order_row_value) AS order_value
    FROM rows_calc
    GROUP BY rows_calc.order_id
)

SELECT 
    h.id,
    h.CUSTOMER_ID,
    h.order_number,
    h.payment_method_id,
     d.dict_value AS payment_method,
    -- h.status,
     ot.order_value
FROM ORDER_T h
    LEFT JOIN order_totals ot ON ot.order_id = h.id
    LEFT JOIN dicts_t d ON d.id = h.payment_method_id
;

CREATE OR REPLACE VIEW "WEBSTORE"."PRODUCTS_V" AS 
  SELECT 
    p.ID,
    p.BRAND_ID,
    db1.DICT_VALUE AS BRAND,
    p.PRICE,
    p.NAME,
    p.EAN,
    p.PRODUCT_TYPE_ID,
    dpt1.DICT_VALUE AS PRODUCT_TYPE,
    w.QUANTITY_ON_STOCK AS ON_STOCK
    FROM PRODUCT_T p
    LEFT JOIN DICTS_T db1 ON p.BRAND_ID = db1.ID
    LEFT JOIN DICTS_T dpt1 ON p.PRODUCT_TYPE_ID = dpt1.ID
    LEFT JOIN WAREHOUSE_T w ON p.ID = w.PRODUCT_ID
;

create or replace PROCEDURE "WEBSTORE".update_product_data
(productid_ integer, name_ varchar2, price_ number)
IS
BEGIN
UPDATE "WEBSTORE".PRODUCT_T
SET NAME = name_,
	PRICE=price_
WHERE id = productid_;
END;
/

create or replace PROCEDURE "WEBSTORE".update_customer_data
(customerid_ integer, fname_ varchar2, lname_ varchar2, phonenumber_ varchar2)
IS
BEGIN
UPDATE "WEBSTORE".CUSTOMER_T
SET FIRST_NAME = fname_,
	LAST_NAME=lname_,
	PHONE_NUMBER=phonenumber_
WHERE id = customerid_;
END;
/

create or replace function "WEBSTORE".GET_ORDER_VALUE (order_id integer) return NUMBER 
as
total_value number;
begin 
		select sum(REPORT1_V.ORDER_VALUE) into total_value 
        from "WEBSTORE".REPORT1_V;
        return total_value;
end;
/

CREATE OR REPLACE FUNCTION "WEBSTORE".customer_info(customer_id IN INTEGER) 
RETURN VARCHAR2 IS 
    name VARCHAR2(100);
BEGIN
    BEGIN
        SELECT u.first_name || ' ' || u.last_name 
        INTO name
        FROM WEBSTORE.CUSTOMER_T u
        WHERE u.id = customer_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RETURN 'Brak użytkownika';
    END;
    RETURN name;
END;
/

