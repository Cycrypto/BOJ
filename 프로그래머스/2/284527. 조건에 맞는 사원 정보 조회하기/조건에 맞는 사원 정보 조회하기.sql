SELECT
  SUM(g.score) AS SCORE,
  h.emp_no AS EMP_NO,
  h.emp_name AS EMP_NAME,
  h.position AS POSITION,
  h.email AS EMAIL
FROM hr_employees h
JOIN hr_grade g ON g.emp_no = h.emp_no
GROUP BY
  h.emp_no, h.emp_name, h.position, h.email
ORDER BY
  SCORE desc
LIMIT 1;