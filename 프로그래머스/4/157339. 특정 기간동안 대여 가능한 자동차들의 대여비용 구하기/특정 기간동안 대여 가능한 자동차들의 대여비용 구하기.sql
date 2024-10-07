-- car: car_id, car_type, daily_fee, options
-- rental_history: history_id, car_id, start_date, end_date
-- discount_plan: plan_id, car_type, duration_type, discount_rate

-- car과 rental_history는 car_id로 join 가능할 듯
-- car_type IN ('세단', 'SUV')인 자동차 중
-- start_date 2022-11-01 end_date 2022-11-30
-- daily_fee * 30 >= 500000 AND daily_fee * 30 < 2000000
-- 의 car_id, car_type, 총대여금액 AS FEE
-- FEE DESC, car_type ASC, car_id DESC

WITH CTYPE AS (
    SELECT DISTINCT C.CAR_ID, C.CAR_TYPE, C.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR C
        JOIN 
        (SELECT CAR_ID
         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
         GROUP BY CAR_ID
         HAVING COUNT(CASE WHEN START_DATE <= '2022-11-30'
                            AND END_DATE >= '2022-11-01' THEN 1
                     END) = 0
         ) H ON C.CAR_ID = H.CAR_ID
    WHERE C.CAR_TYPE IN ('세단', 'SUV')
),
DISCOUNT_FEE AS (
    SELECT C.CAR_ID, C.CAR_TYPE,
        ROUND((C.DAILY_FEE * 30 * (100 - DP.DISCOUNT_RATE) / 100), 0) AS FEE
    FROM CTYPE C
        JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP
        ON C.CAR_TYPE = DP.CAR_TYPE 
    WHERE DP.DURATION_TYPE = '30일 이상'
)
SELECT CAR_ID, CAR_TYPE, FEE
FROM DISCOUNT_FEE
WHERE FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC


