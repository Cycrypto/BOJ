select count(*) as users from user_info
where 
    age is not null
    and extract(year from joined) = 2021
    and age >= 20
    and age <= 29