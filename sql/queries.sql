--1
SELECT * FROM fund_master;

--2
SELECT * FROM aum_data
ORDER BY aum DESC
LIMIT 5;

--3
SELECT AVG(nav)
FROM nav_history;

--4
SELECT *
FROM expense_ratios
WHERE expense_ratio<1;

--5
SELECT MAX(nav)
FROM nav_history;

--6
SELECT MIN(nav)
FROM nav_history;

--7
SELECT COUNT(*)
FROM fund_master;

--8
SELECT category,
COUNT(*)
FROM fund_master
GROUP BY category;

--9
SELECT fund_house,
COUNT(*)
FROM fund_master
GROUP BY fund_house;

--10
SELECT *
FROM risk_metrics
ORDER BY sharpe DESC;