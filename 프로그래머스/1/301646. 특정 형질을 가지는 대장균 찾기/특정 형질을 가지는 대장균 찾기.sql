-- ECOLI_DATA: ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE 
-- 2번 형질은 해당X 1번OR3번 형질은 보유 개체의 수

# 0001 => 1번 형질: 1
# 0010 => 2번 형질: 2
# 0100 => 3번 형질: 4
# 1000 => 4번 형질: 8
# 1번과 3번 형질을 가지려면: 0101 => 5


SELECT COUNT(*) AS 'COUNT'
FROM ECOLI_DATA E1 
WHERE GENOTYPE & 2 = 0
    AND GENOTYPE & 5 > 0