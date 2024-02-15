-- 코드를 입력하세요
SELECT a.animal_id, a.animal_type, a.name
from animal_ins a
right join animal_outs b
using(animal_id)
where
    a.sex_upon_intake != b.sex_upon_outcome
    
order by a.animal_id