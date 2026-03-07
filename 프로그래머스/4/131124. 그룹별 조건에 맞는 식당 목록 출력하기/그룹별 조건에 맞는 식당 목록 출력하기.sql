with max_review_count as (
    select count(*) as c
    from rest_review
    group by member_id
    order by count(*) desc
    limit 1
)
select 
    m.member_name, 
    r.review_text, 
    date_format(r.review_date, '%Y-%m-%d') as review_date

from member_profile m
join rest_review r on m.member_id = r.member_id
where
    m.member_id in (
        select member_id
        from rest_review
        group by member_id
        having count(*) = (select c from max_review_count)
    )
    order by review_date, review_text