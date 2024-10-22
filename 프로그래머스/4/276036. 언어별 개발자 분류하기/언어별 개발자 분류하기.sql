-- A : Front End(16, 2048, 8192) + Python(256) +@
-- B : C#
-- C : 그 외의 Front End 개발자

# 일단 FE 개발자를 찾음
# 그 중에서 Python 스킬을 갖고 있는 사람을 찾음
# C# 가진 사람을 찾음

-- FE skillcodes만 모아 둔 테이블
WITH FE AS (
    SELECT ID, FIRST_NAME
    FROM SKILLCODES S, DEVELOPERS D
    WHERE S.CATEGORY = 'Front End'
            AND S.CODE & D.SKILL_CODE = S.CODE
),
GRADES AS (
    SELECT
        CASE
            WHEN ID IN (SELECT ID FROM FE)
                    AND SKILL_CODE & (SELECT CODE
                                        FROM SKILLCODES
                                        WHERE NAME='Python') > 0 THEN 'A'
            WHEN SKILL_CODE & (SELECT CODE 
                                FROM SKILLCODES
                              WHERE NAME = 'C#') > 0 THEN 'B'
            WHEN ID IN (SELECT ID FROM FE) THEN 'C'
            END AS GRADE,
        ID,
        EMAIL
    FROM DEVELOPERS
)
SELECT * 
FROM GRADES
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID