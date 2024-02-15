-- 코드를 입력하세요
SELECT a.product_code, sum(a.price * b.sales_amount) sales
from product a
join offline_sale b
using (product_id)
group by a.product_id
order by sales desc, a.product_code asc