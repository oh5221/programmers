-- FISH_INFO에서 잡은 BASS와 SNAPPER의 수를 FISH_COUNT로 출력
SELECT COUNT(FI.FISH_TYPE) AS FISH_COUNT
FROM FISH_INFO FI, FISH_NAME_INFO FNI
WHERE (FNI.FISH_NAME = 'BASS' OR FNI.FISH_NAME = 'SNAPPER') AND FI.FISH_TYPE = FNI.FISH_TYPE