-- CART_PRODUCTS: ID, CART_ID, NAME, PRICE
-- 같은 CART_ID에 NAME이 Milk랑 Yogurt가 있을 때
-- CART_ID를 ASC 정렬

-- CART_ID별로 GROUP BY를 해서
-- Milk인 거랑 Yogurt인 거랑 각각 구해서 -> 겹치는 id를 더하기 inner join으로
WITH M AS (
    -- 장바구니에 Milk가 들어 있을 때
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Milk'
),
Y AS (
    -- 장바구니에 Yogurt가 들어 있을 때
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Yogurt'
)
SELECT DISTINCT M.CART_ID
FROM M JOIN Y
    ON M.CART_ID = Y.CART_ID -- 장바구니 ID 동일할 때
ORDER BY 1