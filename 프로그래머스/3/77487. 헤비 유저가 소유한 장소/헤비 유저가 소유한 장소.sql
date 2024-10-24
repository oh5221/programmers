-- PLACES: ID, NAME, HOST_ID
-- HOST_ID가 2개 이상이면 헤비 유저
-- 헤비 유저의 공간 정보 (ID, NAME, HOST_ID 전부 출력)
-- ORDER BY ID

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID  -- HEAVY 여부
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(ID) >= 2)
ORDER BY ID
