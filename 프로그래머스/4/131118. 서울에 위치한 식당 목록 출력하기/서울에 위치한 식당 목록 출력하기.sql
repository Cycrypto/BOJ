select i.rest_id, rest_name, food_type, favorites, address, round(avg(r.review_score), 2) as review_score from rest_info i
join rest_review r on r.rest_id = i.rest_id
where
substring(address, 1, 5) = '서울특별시' or
substring(address, 1, 3) = '서울시'
group by rest_id
order by review_score desc, favorites desc