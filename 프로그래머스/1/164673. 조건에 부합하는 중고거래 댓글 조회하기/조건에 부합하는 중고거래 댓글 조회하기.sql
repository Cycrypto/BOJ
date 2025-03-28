-- 코드를 입력하세요
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, TO_CHAR(B.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
FROM USED_GOODS_BOARD A, USED_GOODS_REPLY B
WHERE
    A.BOARD_ID = B.BOARD_ID AND
    TO_CHAR(A.CREATED_DATE, 'YYYYMM') = '202210'
    
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC