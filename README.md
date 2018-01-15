# Logs Analysis Project

This project consist of a reporting tool which print out the results of SQL queries which answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project design

The code consist of two files `logs_analysis.py` and `logs_analysis_db.py`.
The former calls the methods to get the data necessary to display the information required and print out all the information in plain text.
The latter contain the `LogsAnalysisDB` class which connect to the database and contains the methods to execute all the SQL queries.

## How to
Before to run the program is necessary to create all the views required.
You can find the `create view` statements below.

In order to see the results of the reporting tool, it's just necessary to make executable `logs_analysis.py`:
`chmod +x logs_analysis.py`

and then run the program `./logs_analysis.py`

## Views

Here all the statements for the necessary views

```
CREATE VIEW article_views AS
SELECT a.author, a.title, COUNT(*) AS views
FROM log AS l
JOIN articles AS a
ON replace(l.path, '/article/', '') = a.slug
GROUP BY a.title, a.author;
```

```
CREATE VIEW daily_errors AS
SELECT date_trunc('day', time) AS day, COUNT(*) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day;
```

```
CREATE VIEW daily_requests AS
SELECT date_trunc('day', time) AS day, COUNT(*) AS requests
FROM log
GROUP by day
```
