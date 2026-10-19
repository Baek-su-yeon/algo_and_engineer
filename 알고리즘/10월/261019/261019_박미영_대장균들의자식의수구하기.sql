-- 코드를 작성해주세요--
-- 대장균 개체의 ID와 자식의 수 출력
-- 자식이 없다면 0으로 출력
-- 개체 ID에 대해 오름차순

SELECT A.ID, COUNT(B.ID) AS CHILD_COUNT
FROM ECOLI_DATA AS A
LEFT JOIN ECOLI_DATA AS B
ON A.ID = B.PARENT_ID
GROUP BY A.ID
ORDER BY A.ID ASC;
