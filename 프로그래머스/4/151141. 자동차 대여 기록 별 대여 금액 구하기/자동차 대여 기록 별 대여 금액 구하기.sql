-- CAR: CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
-- RENTAL_HISTORY: HISTORY_ID, CAR_ID, START_DATE, END_DATE
-- DISCOUNT_PLAN: PLAN_ID, CAR_TYPE, DURATION_TYPE, DISCOUNT_RATE

-- CAR_TYPE = '트럭' 
-- GROUP BY CAR_TYPE 
-- FEE를 구해서 
-- HISTORY_ID, FEE 
-- ORDER BY FEE DESC, HISTORY_ID DESC

-- CAR과 RENTAL_HISTORY만 JOIN
-- WHERE 절에 CAR.CAR_TYPE = '트럭'
-- CAR_ID 별로 RENTAL DURATION을 구해 두고 -> 이걸 CTE로 묶음
WITH DURATION_BY_CAR_ID AS (
    SELECT HISTORY_ID, RH.CAR_ID, CAR_TYPE, DAILY_FEE,
            DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION_DATE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY RH 
        LEFT JOIN CAR_RENTAL_COMPANY_CAR C
        ON RH.CAR_ID = C.CAR_ID
    WHERE C.CAR_TYPE = '트럭'
)
# SELECT * FROM DURATION_BY_CAR_ID
/*
HISTORY_ID	CAR_ID	CAR_TYPE	DAILY_FEE	DURATION_DATE
524	8	트럭	107000	1
527	8	트럭	107000	5
546	8	트럭	107000	2
556	8	트럭	107000	8
558	6	트럭	133000	36
581	8	트럭	107000	2
586	8	트럭	107000	2
*/
-- 바깥 SELECT 문에서
-- DURATION이 7일 이상이면 5%, 30일 이상이면 7% ... 이렇게 DURATION TYPE에 맞게 FEE를 계산하면 될 거 같습니다.
SELECT HISTORY_ID,
        CASE WHEN DURATION_DATE >= 90 
                THEN ROUND(DAILY_FEE * (100 - (SELECT DISCOUNT_RATE
                                         FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                         WHERE DURATION_TYPE LIKE '90%'
                                            AND CAR_TYPE = DURATION_BY_CAR_ID.CAR_TYPE)) / 100
                                * DURATION_DATE, 0)
            WHEN DURATION_DATE >= 30
                THEN ROUND(DAILY_FEE * (100 - (SELECT DISCOUNT_RATE
                                         FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                         WHERE DURATION_TYPE LIKE '30%'
                                            AND CAR_TYPE = DURATION_BY_CAR_ID.CAR_TYPE)) / 100  * DURATION_DATE, 0)
            WHEN DURATION_DATE >= 7
                THEN ROUND(DAILY_FEE * (100 - (SELECT DISCOUNT_RATE
                                         FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                         WHERE DURATION_TYPE LIKE '7%'
                                                AND CAR_TYPE = DURATION_BY_CAR_ID.CAR_TYPE)) / 100  * DURATION_DATE, 0)
            ELSE ROUND(DAILY_FEE * DURATION_DATE, 0)                        
            END AS FEE
FROM DURATION_BY_CAR_ID
ORDER BY FEE DESC, HISTORY_ID DESC
