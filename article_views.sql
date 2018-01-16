CREATE VIEW article_views AS
SELECT a.author, a.title, COUNT(*) AS views
FROM log AS l
JOIN articles AS a
ON replace(l.path, '/article/', '') = a.slug
GROUP BY a.title, a.author;