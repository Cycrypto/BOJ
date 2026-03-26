select count(*) as users
from user_info
where date_format(joined, '%Y') = date_format('2021-00-00', '%Y')
and age between 20 and 29