with cte as(
select lat_n,
row_number() over(order by lat_n) as rn,
count(*) over() as cnt
from station)

select round(lat_n,4) from cte where rn in ((cnt+1)/2, (cnt+2)/2)