select 
    fp.category,
    fp.price as max_price,
    fp.product_name
from food_product fp
join(
    SELECT  category, max(price) as max_price, product_name
    from food_product
    where category in ('과자', '국', '김치', '식용유')
    group by category
) m
on fp.category = m.category
and fp.price = m.max_price
order by max_price desc