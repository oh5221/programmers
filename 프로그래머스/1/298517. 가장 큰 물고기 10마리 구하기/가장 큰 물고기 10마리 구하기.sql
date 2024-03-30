-- 가장 큰 물고기 10마리의 ID와 길이 출력
-- 길이 기준 내림차순 정렬, 길이 같으면 ID 기준 오름차순 정렬

SELECT *
FROM (SELECT ID, LENGTH
     FROM FISH_INFO
     ORDER BY LENGTH DESC, ID ASC) A LIMIT 10