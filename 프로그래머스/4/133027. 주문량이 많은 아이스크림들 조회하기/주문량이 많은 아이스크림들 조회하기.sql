-- FIRST_HALF: SHIPMENT_ID, FLAVOR, TOTAL_ORDER
-- JULY: SHIPMENT_ID(상반기 테이블로 연결), FLAVOR, TOTAL_ORDER
-- 7월 총주문량 + 상반기 총주문량 값 DESC로 상위 3개
WITH JULY_FLAVOR AS (
    SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
)
SELECT FH.FLAVOR
FROM FIRST_HALF FH LEFT JOIN JULY_FLAVOR J
    ON FH.FLAVOR = J.FLAVOR
GROUP BY FH.FLAVOR
ORDER BY FH.TOTAL_ORDER + J.TOTAL_ORDER DESC
LIMIT 3