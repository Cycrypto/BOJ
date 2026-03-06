with EMP_GRADE
as(
    select
        emp_no, 
        case
            when avg(score) >= 96 then 'S'
            when avg(score) >= 90 then 'A'
            when avg(score) >= 80 then 'B'
            else 'C'
        end as grade
    from hr_grade
    group by emp_no
), EMP_GRADE_RATE
as(
    select 
        emp_no,
        grade,
        case
            when grade = 'S' then 0.2
            when grade = 'A' then 0.15
            when grade = 'B' then 0.1
            when grade = 'C' then 0
        end as rate
    from emp_grade eg
)

select
    h.emp_no,
    h.emp_name,
    eg.grade,
    eg.rate * h.sal as bonus
from hr_employees h
join EMP_GRADE_RATE eg on h.emp_no = eg.emp_no
