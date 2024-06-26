-- 대여 시작일이 2022년 9월일 때
-- 대여 기간이 30일 이상이면 '장기 대여' 아니면 '단기 대여'
-- 컬럼명 RENT_TYPE, HISTORY_ID 기준 내림차순
SELECT HISTORY_ID, CAR_ID, 
        DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, 
        DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE, 
        IF (DATEDIFF(END_DATE, START_DATE) >= 29, '장기 대여', '단기 대여') AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC