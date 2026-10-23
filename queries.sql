-- create database churn_project;
-- use churn_project;
-- select * from customers;
Select count(*) as Customers, 
SUM(churn_value) as churned, 
Round(100.0*sum(Churn_Value)/count(*),1) as churn_rate_pct
from customers; 
-- use churn_project;
-- describe customers;

-- Select contract,
-- count(*) AS customers, 
-- Round(100.0*sum(Churn_Value)/count(*),1) as churn_rate_pct
-- from Customers
-- group by contract
-- order by churn_rate_pct desc;

-- Select tenure_group,
-- count(*) AS customers, 
-- Round(100.0*sum(Churn_Value)/count(*),1) as churn_rate_pct
-- from Customers
-- group by tenure_group
-- order by churn_rate_pct desc;

Select payment_method,
count(*) AS customers, 
Round(100.0*sum(Churn_Value)/count(*),1) as churn_rate_pct
from Customers
group by payment_method
order by churn_rate_pct desc;


Select churn_reason, Count(*) as cmt
from customers
where churn_reason is not null and churn_reason <> ' '
group by churn_reason
order by cmt desc;
-- limit 10;



