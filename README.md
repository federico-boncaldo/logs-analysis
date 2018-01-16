# Logs Analysis Project

This project consists of a reporting tool which print out the results of SQL queries which answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project design

The code consists of two files `logs_analysis.py` and `logs_analysis_db.py`.
The former calls the methods to get the data necessary to display the information required and print out all the information in plain text.
The latter contain the `LogsAnalysisDB` class which connect to the database and contains the methods to execute all the SQL queries.

## How to
Before run the program is **necessary** to create all the views required.
You can find the scripts to create the views below.

In order to see the results of the reporting tool, it's just necessary to make executable `logs_analysis.py`:
`chmod +x logs_analysis.py`

and then run the program `./logs_analysis.py`

## Views

The project includes three sql file, each of these will create the views necessary to run properly the tool.

Before to run the program execute these scripts in your Database Management System: `article_views.sql` `daily_errors.sql` `daily_requests.sql`