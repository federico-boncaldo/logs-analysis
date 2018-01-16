CREATE VIEW daily_requests AS
SELECT date_trunc('day', time) AS day, COUNT(*) AS requests
FROM log
GROUP by day