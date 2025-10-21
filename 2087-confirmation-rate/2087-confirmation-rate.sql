# Write your MySQL query statement below
WITH confirmed_table AS (
    SELECT user_id, COUNT(action) AS confirmed
    FROM Confirmations
    WHERE action = "confirmed"
    GROUP BY user_id
), timeout_table AS (
    SELECT user_id, COUNT(action) AS timeout
    FROM Confirmations
    WHERE action = "timeout"
    GROUP BY user_id
), all_user_id AS (
    SELECT distinct user_id
    FROM Signups
)
    SELECT s.user_id, ROUND(IFNULL(IFNULL(c.confirmed,0) / (IFNULL(c.confirmed,0) + IFNULL(t.timeout,0)), 0), 2) AS confirmation_rate
    FROM all_user_id AS s
    LEFT JOIN confirmed_table AS c USING (user_id)
    LEFT JOIN timeout_table AS t USING (user_id)