select 
    history_id,
    car_id,
    date_format(start_date, "%Y-%m-%d") as start_date,
    date_format(end_date, "%Y-%m-%d") as end_date,
    if(datediff(end_date, start_date) + 1 >= 30, "장기 대여", "단기 대여")

from car_rental_company_rental_history
where
    start_date between "2022-09-01" and "2022-09-30"
    
order by history_id desc


# SELECT HISTORY_ID,
#         CAR_ID,
#         DATE_FORMAT(start_date,'%Y-%m-%d') AS START_DATE,
#         DATE_FORMAT(end_date,'%Y-%m-%d') AS END_DATE,
#         IF(DATEDIFF(END_DATE, START_DATE)+1 >= 30, "장기 대여","단기 대여") AS RENT_TYPE
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE DATE_FORMAT(START_DATE,'%Y-%m') = '2022-09'
# ORDER BY history_id DESC