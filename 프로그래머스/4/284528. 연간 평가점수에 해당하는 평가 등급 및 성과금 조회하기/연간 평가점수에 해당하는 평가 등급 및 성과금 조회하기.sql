-- HR_DEPARTMENT: DEPT-ID, DEPT_NAME_KR, DEP_NAME_EN, LOCATION
-- HR_EMPLOYEES: EMP_NO, EMP_NAME, DEPT_ID, POSITION, EMAIL, COMP_TEL, HIRE_DATE, SAL
-- HR_GRADE: EMP_NO, YEAR, HALF_YEAR, SCORE

-- 사원의 성과급 정보. 사번, 성명, 평가 등급 GRADE, 성과금 BONUS
-- HR_GRADE의 SCORE이 96 이상 -> S, 20% / 90 이상 -> A, 15%
-- 80 이상 -> B, 10% / ELSE -> C, 0%
WITH YEAR_SCORE AS (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT HE.EMP_NO, EMP_NAME, 
        CASE WHEN SCORE >= 96 THEN 'S'
        WHEN SCORE >= 90 THEN 'A'
        WHEN SCORE >= 80 THEN 'B'
        ELSE 'C' 
        END AS GRADE,
        ROUND(CASE WHEN SCORE >= 96 THEN SAL * 0.2
        WHEN SCORE >= 90 THEN SAL * 0.15
        WHEN SCORE >= 80 THEN SAL * 0.1
        ELSE 0 END, 1)
        AS BONUS
FROM HR_EMPLOYEES HE JOIN YEAR_SCORE HG
        USING (EMP_NO)
ORDER BY EMP_NO