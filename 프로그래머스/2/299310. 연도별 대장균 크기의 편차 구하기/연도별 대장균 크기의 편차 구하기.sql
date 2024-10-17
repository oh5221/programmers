-- ECOLI_DATA: ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
-- YEAR(DATE), YEAR_DEV -> SIZE의 편차, ID를 출력하기
-- YEAR_DEV = MAX(SIZE) - SIZE
-- ORDER BY YEAR, YEAR_DEV 

-- CTE로 연도별 MAX SIZE를 테이블
WITH MAX_SIZE AS (
    SELECT MAX(SIZE_OF_COLONY) AS MAX_COL, 
            YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA
    GROUP BY YEAR
)
SELECT YEAR, 
        (MAX_COL - SIZE_OF_COLONY) AS YEAR_DEV,
        ID
FROM ECOLI_DATA ED LEFT JOIN MAX_SIZE MS
    ON DATE_FORMAT(ED.DIFFERENTIATION_DATE, '%Y') = MS.YEAR
ORDER BY 1, 2