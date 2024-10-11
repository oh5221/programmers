-- ECOLI_DATA: ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
-- 부모의 형질을 모두 보유한 대장균의 ID, GENOTYPE, PARENT_GENOTYPE

# ID PARENT_ID GENOTYPE
# 1     null	1 = 01

# 2	    1	    1 = 01
# 3	    1	    3 = 11

# 4	    2	    2 = 10 부모 형질 X
# 7	    2	    5 = 101

# 6	    3	    5 = 101 부모 형질 X
# 8	    6	    13 = 1101

# 5	    4	    8 = 1000 부모 형질 X
-- 2진수이고 그냥 덧셈해서는 안 풀리는 거 보니까 & 연산이 필요할 듯함
-- SELF JOIN해서 자식 GENOTYPE & 부모 GENOTYPE = 부모 GENOTYPE 해야 함


SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA C JOIN ECOLI_DATA P
    ON C.PARENT_ID = P.ID
WHERE C.GENOTYPE & P.GENOTYPE = P.GENOTYPE
ORDER BY ID