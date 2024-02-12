-- 코드를 입력하세요
select 
    a.category, sum(b.sales) as total_sales
    
from 
    book a, book_sales b
    
where
    a.book_id = b.book_id
    and to_char(b.sales_date, 'yyyymm') = '202201'
    
group by a.category
order by a.category asc