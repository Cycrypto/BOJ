SELECT hour(datetime) hour, count(*) from animal_outs
where hour(datetime) >=  9 and hour(datetime) <= 19
group by hour
order by hour asc