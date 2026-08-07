# SELECT I.ID, N.FISH_NAME, I.LENGTH
# FROM FISH_INFO I
# JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
# WHERE I.LENGTH = (
#     SELECT MAX(INF.LENGTH)
#     FROM FISH_INFO INF
#     WHERE INF.FISH_TYPE = I.FISH_TYPE)
# ORDER BY I.ID ASC;
# ===========================
# 서브쿼리로 물고기 종류별 최대 길이 먼저 구하기
# 메인쿼리에서 각 쿨고기 길이가 그 종류 최대 길이와 일치하는 행만 필터링

SELECT ID, FISH_NAME, LENGTH
FROM (
    SELECT
        I.ID, N.FISH_NAME, I.LENGTH,
        ROW_NUMBER() OVER (PARTITION BY I.FISH_TYPE ORDER BY I.LENGTH DESC) AS rk
    FROM FISH_INFO I
    JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
) t
WHERE rk = 1
ORDER BY ID ASC;
# ===========================
# PRTITION BY I.FISH_TYPE: 물고기 종류별로 그룹 나누기
# ORDER BY I.LENGTH DESC; 각 그룹 내에서 물고기 길이(LENGTH)가 긴 순서대로 정렬
# ROW_NUMBER() OVER() AS rk: 정렬된 순서대로 각 그룹 내에서 순번(rk) 매기기. 즉, 종류별로 가장 긴 물고기가 무조건 순번 1 받음
# WHERE rk = 1: 서브쿼리 결과에서 순번이 1인 행들만 필터링해서 각 물고기 종류별 최대 길이 행만 정확히 추출