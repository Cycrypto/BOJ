select a.apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from appointment a
join doctor d on a.mddr_id = d.dr_id
join patient p on a.pt_no = p.pt_no
where 
    date_format(apnt_ymd,'%Y-%m-%d') = date_format('2022-04-13','%Y-%m-%d')
    and a.mcdp_cd = 'CS'
    and a.apnt_cncl_yn = 'N'
    
order by apnt_ymd asc