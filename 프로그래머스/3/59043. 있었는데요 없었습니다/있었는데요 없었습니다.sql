-- 코드를 입력하세요
SELECT a.animal_id, a.name from animal_ins a
inner join animal_outs b using(animal_id)
where a.datetime > b.datetime
order by a.datetime asc