-- FOOD_PRODUCT: PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
-- 식품 분류 별로 가격이 제일 비싼 식품 분류, 가격, 이름 조회
-- 분류가 과자 국 김치 식용유일 때만
-- ORDER BY 가격
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT 
WHERE CATEGORY IN ('식용유', '과자', '국', '김치')
        AND PRICE IN (SELECT MAX(PRICE) 
                      FROM FOOD_PRODUCT 
                      GROUP BY CATEGORY)
ORDER BY 2 DESC