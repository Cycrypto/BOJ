# with march_total_sales as(
#     select book_id, sum(sales) as total_sales from book_sales
#     where sales_date like "2022-01%"
#     group by book_id
#     order by book_id
# ), march_total_sales_by_id as (
#     select a.book_id, a.author_id, a.category, sum(a.price * b.total_sales) total_sales
#     from book a
#     join march_total_sales b
#     using(book_id)
#     group by a.book_id
# )

# select a.author_id, a.author_name, b.category, b.total_sales
# from author a
# join march_total_sales_by_id b
# using(author_id)
# order by a.author_id asc, b.category desc

select a.author_id, a.author_name, b.category, sum(s.sales * b.price) from book b
join author a
using(author_id)
join book_sales s
using(book_id)
where
    s.sales_date like "2022-01%"
    
group by b.author_id, b.category
order by a.author_id asc, b.category desc