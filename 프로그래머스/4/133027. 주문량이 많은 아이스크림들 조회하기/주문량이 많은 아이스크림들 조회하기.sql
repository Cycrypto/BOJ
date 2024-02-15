select flavor from (select * from first_half union select * from july) a
group by a.flavor
order by sum(total_order) desc
limit 3