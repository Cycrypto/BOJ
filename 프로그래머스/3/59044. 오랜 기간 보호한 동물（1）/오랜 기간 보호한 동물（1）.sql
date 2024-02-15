-- 코드를 입력하세요
SELECT a.name, a.datetime
from animal_ins a
left join animal_outs b
using(animal_id)
where
b.animal_id is null
order by a.datetime asc
limit 3