-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, to_char(hire_ymd, 'yyyy-mm-dd') from doctor
where mcdp_cd = 'CS' or mcdp_cd = 'GS'
order by hire_ymd desc, dr_name asc