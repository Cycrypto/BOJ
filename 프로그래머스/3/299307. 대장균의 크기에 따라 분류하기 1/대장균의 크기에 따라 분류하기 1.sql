select
    id,
    case
        when size_of_colony between 0 and 101 then 'LOW'
        when size_of_colony between 101 and 1001 then 'MEDIUM'
        else 'HIGH'
    end as size
from ecoli_data
order by id asc