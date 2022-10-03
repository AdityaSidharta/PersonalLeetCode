# Write your MySQL query statement below
WITH first_install AS (
    SELECT player_id, MIN(event_date) AS install_date
    FROM Activity
    GROUP BY player_id
),

retention AS (
    SELECT f.player_id, f.install_date, DATE_ADD(f.install_date, INTERVAL 1 DAY) AS retention_date,
    CASE WHEN DATE_ADD(f.install_date, INTERVAL 1 DAY) = a.event_date THEN 1
    ELSE 0 END AS ret
    FROM first_install AS f
    LEFT JOIN Activity AS a 
    ON (f.player_id = a.player_id)
)

SELECT f.install_date AS install_dt, COUNT(f.player_id) AS installs, ROUND(sum_retention / COUNT(f.player_id), 2) AS Day1_retention
FROM first_install AS f
LEFT JOIN (SELECT install_date, SUM(ret) AS sum_retention FROM retention GROUP BY install_date) AS r
ON (f.install_date = r.install_date)
GROUP BY install_dt
ORDER BY install_dt