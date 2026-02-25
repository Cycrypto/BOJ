select id, length
from fish_info
where length is NOT NULL
order by length desc, id asc
limit 10