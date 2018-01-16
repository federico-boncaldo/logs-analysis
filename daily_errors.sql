CREATE VIEW daily_errors AS
SELECT date_trunc('day', time) AS day, COUNT(*) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day;