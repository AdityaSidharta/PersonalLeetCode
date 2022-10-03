# Write your MySQL query statement below
WITH managers AS (
    SELECT managerId, COUNT(*) AS report_count
    FROM Employee
    WHERE managerId IN (SELECT DISTINCT id FROM Employee)
    GROUP BY managerId
    HAVING report_count >= 5
)

SELECT name
FROM managers m
LEFT JOIN Employee e
ON (m.managerId = e.id)