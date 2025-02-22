INSERT INTO ORDER_T (customer_id, order_number, payment_method, order_date, delivery_date, status, delivery_method, is_paid)
SELECT
    z.KLIENT as customer_id,
    z.NR_ZAMOWIENIA as order_number,
    UPPER(FORMAPLATNOSCI) AS payment_method,
    ADD_MONTHS(DATA_ZLOZENIA, 12) AS order_date,
    ADD_MONTHS(DATA_WYSLANIA, 12) AS delivery_date,
    UPPER(STATUS) AS status,
    UPPER(FO.NAZWA) AS delivery_method,
    1 AS is_paid

FROM ZAMOWIENIE z, FORMAODBIORU fo
WHERE z.FORMAODBIORU = fo.ID
;

COMMIT;

SELECT COUNT(1) 
FROM ORDER_T;

SELECT o.CUSTOMER_ID, c.ID, c.LAST_NAME
FROM ORDER_T o, CUSTOMER_T c
WHERE o.CUSTOMER_ID = c.ID;



SELECT DISTINCT o.ID
FROM CUSTOMER_T o;

SELECT DISTINCT o.CUSTOMER_ID, COUNT(1) CNT
FROM ORDER_T o
GROUP BY o.CUSTOMER_ID
ORDER BY 1;


INSERT INTO WAREHOUSE_T (product_id, QUANTITY_ON_STOCK)
SELECT ID, ON_STOCK
FROM PRODUCT_T;
COMMIT;

INSERT INTO DICTS_T (dict_name, dict_key, dict_value)
SELECT DISTINCT
    'STATUS' AS dict_name,
    UPPER(STATUS) AS dict_key,
    STATUS AS dict_value
FROM ZAMOWIENIE;
COMMIT
;

MERGE INTO ORDER_T t
USING DICTS_T d
ON (UPPER(t.PAYMENT_METHOD) = d.DICT_KEY AND d.DICT_NAME = 'PAYMENT_METHOD')
WHEN MATCHED THEN
    UPDATE SET t.PAYMENT_METHOD_ID = d.ID
;
COMMIT
;

MERGE INTO ORDER_T t
USING DICTS_T d
ON (UPPER(t.DELIVERY_METHOD) = d.DICT_KEY AND d.DICT_NAME = 'DELIVERY_METHOD')
WHEN MATCHED THEN
    UPDATE SET t.DELIVERY_METHOD_ID = d.ID
;
COMMIT
;

MERGE INTO ORDER_T t
USING DICTS_T d
ON (UPPER(t.STATUS) = d.DICT_KEY AND d.DICT_NAME = 'STATUS')
WHEN MATCHED THEN
    UPDATE SET t.STATUS_ID = d.ID
;
COMMIT
;

SELECT * 
FROM PRODUCT_T t, DICTS_T d
WHERE 1=1
    AND t.BRAND = d.DICT_KEY 
    AND d.DICT_NAME = 'BRAND'
;

CREATE OR REPLACE VIEW PRODUCTS_V
AS

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



SELECT 
report1_v.id, report1_v.customer_id, report1_v.order_number, report1_v.payment_method, report1_v.status, report1_v.order_value
FROM report1_v;

-- CREATE OR REPLACE FORCE EDITIONABLE VIEW "WEBSTORE"."REPORT1_V" ("ID", "CUSTOMER_ID", "ORDER_NUMBER", "PAYMENT_METHOD", "ORDER_VALUE") DEFAULT COLLATION "USING_NLS_COMP"  
-- AS 

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
    h.payment_method_id
    -- d.dict_value AS payment_method,
    -- h.status,
    -- ot.order_value
FROM ORDER_T h
    LEFT JOIN order_totals ot ON ot.order_id = h.id
    LEFT JOIN dicts_t d ON d.id = h.payment_method_id
;

SELECT STATUS, COUNT(1) CNT
FROM ORDER_T
GROUP BY STATUS;

DELETE FROM ORDER_T
WHERE STATUS = '5'; --IN ('1', '3', '5');
COMMIT;


create or replace trigger after_order
 AFTER insert
  ON ORDER_T
  FOR EACH ROW
  BEGIN
  INSERT INTO LOG_T
         VALUES(user, 'Dodano nowe zamówienie. Nr zamowienia: '||:NEW.ORDER_NUMBER||
         ', Klient id: '||:NEW.CUSTOMER_ID, systimestamp);
  END;
  
/


create or replace PROCEDURE update_customer_data
(customerid_ integer, fname_ varchar2, lname_ varchar2, phonenumber_ varchar2)
IS
BEGIN
UPDATE CUSTOMER_T
SET FIRST_NAME = fname_,
	LAST_NAME=lname_,
	PHONE_NUMBER=phonenumber_
WHERE id = customerid_;
END;
<<<<<<< HEAD
/



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
    h.payment_method_id
    -- d.dict_value AS payment_method,
    -- h.status,
    -- ot.order_value
FROM ORDER_T h
    LEFT JOIN order_totals ot ON ot.order_id = h.id
    LEFT JOIN dicts_t d ON d.id = h.payment_method_id
    ;

create or replace function SUM_ORDER_VALUE (order_id integer)
return NUMBER 
as
total_value number;
    

begin 
WITH 
    rows_calc AS (
        SELECT 
        orw.order_id,
        orw.product_id,
        orw.quantity,
        NVL(orw.quantity, 0) * NVL(p.price, 0) AS order_row_value
    
    FROM ORDER_ROW_T orw
        JOIN PRODUCT_T p ON p.ID = orw.PRODUCT_ID
    WHERE orw.order_id=order_id
    ),
    
    order_totals AS (
        SELECT 
        rows_calc.order_id,
        SUM(order_row_value) AS order_value
        FROM rows_calc
        GROUP BY rows_calc.order_id
    )

		select sum(order_totals.wartosc) into total_value 
        from order_totals;
        return concat(wynik, ' zl');

end;
=======
/
>>>>>>> ca36b6318d9b60cdb22ea069422a1bc5df8c34d9
