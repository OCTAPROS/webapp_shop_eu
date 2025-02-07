CREATE OR REPLACE VIEW AAA AS 

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
    FROM aa
    GROUP BY aa.order_id
)

SELECT 
    h.id,
    h.CUSTOMER_ID,
    h.order_number,
    h.payment_method, 
    bb.order_value
FROM ORDER_T h
JOIN bb ON bb.order_id = h.id
;




SELECT COUNT(1) 
FROM zamowienie;


ALTER SESSION SET nls_date_format='yyyy-mm-dd';
COMMIT;

SELECT * FROM zamowienie; 

UPDATE ORDER_T
SET ORDER_NUMBER =  'A' || '/' || EXTRACT(YEAR FROM ORDER_DATE) || '/' || ID
;

CREATE UNIQUE INDEX IDX_UNIQUE_ORDER_NUMBER ON ORDER_T(ORDER_NUMBER);

SELECT * 
FROM ORDER_T 
WHERE ORDER_NUMBER IN ('A/2024/9175', 'A/2024/694', 'A/2024/1903'); 

SELECT *
FROM ORDER_T o
JOIN CUSTOMER_T c ON o.CUSTOMER_ID = c.ID
WHERE c.CITY = 'Legionowo';

CREATE INDEX IDX_CUSTOMER_ID ON ORDER_T(CUSTOMER_ID);

DROP INDEX IDX_CUSTOMER_CITY;

create or replace trigger after_order_insert
AFTER insert
ON ORDER_T
FOR EACH ROW
BEGIN
INSERT INTO LOGS_T (USER_NAME, DESCRIPTION, WHEN_TS)
VALUES(user, 'Dodano nowe zamówienie. Nr zamowienia: ' || :NEW.ORDER_NUMBER || ', Klient id: '|| :NEW.CUSTOMER_ID, systimestamp);
END;
 
/

TRUNCATE TABLE LOGS_T;


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

SELECT customer_info(2)
FROM DUAL;
-- 6813

CREATE OR REPLACE FUNCTION customer_info(customer_id IN INTEGER) 
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