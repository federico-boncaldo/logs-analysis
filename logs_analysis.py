#!/usr/bin/env python2.7
'''Retrieve the data for the report and print them out'''
import logs_analysis_db

logs_db = logs_analysis_db.LogsAnalysisDB("news")

articles = logs_db.get_most_popular_articles()
authors = logs_db.get_most_popular_authors()
daily_percentage = logs_db.get_daily_error_percentage()

print "\nMost popular 3 articles\n"
for article in articles:
    title = article[0]
    views = str(article[1])
    print "%s - %s views" % (title, views)
print "\n"

print "Most popular article authors\n"
for author in authors:
    name = author[0]
    views = str(author[1])
    print "%s - %s views" % (name, views)
print "\n"

print "Days when more than 1% requests lead to errors\n"
for percentage in daily_percentage:
    day = str(percentage[0])
    percentage = str(percentage[1])
    print "%s - %s%% errors" % (day[:10], percentage)
print "\n"

logs_db.close_connection()
