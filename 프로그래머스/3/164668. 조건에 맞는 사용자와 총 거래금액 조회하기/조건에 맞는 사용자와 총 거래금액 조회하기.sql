WITH SUM_OF_PRICE AS(
    SELECT
        WRITER_ID, SUM(PRICE) AS TOTAL_SALES
    FROM
        USED_GOODS_BOARD
    WHERE
        STATUS = 'DONE'
    GROUP BY WRITER_ID
)

SELECT 
    B.USER_ID,
    B.NICKNAME,
    C.TOTAL_SALES
        
FROM
    USED_GOODS_USER B,
    SUM_OF_PRICE C
WHERE
    B.USER_ID = C.WRITER_ID AND
    C.TOTAL_SALES >= 700000

ORDER BY C.TOTAL_SALES ASC