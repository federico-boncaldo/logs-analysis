#!/usr/bin/env python2.7
'''The class provides the methods that query the database for the specific
data required for the logs analysis
'''
import psycopg2


class LogsAnalysisDB():

    def __init__(self, dbname):
        '''Connects to the database and instantiates a cursor'''
        self.db = psycopg2.connect(database=dbname)
        self.cursor = self.db.cursor()

    def close_connection(self):
        self.db.close()

    def get_most_popular_articles(self):
        '''Provides the most 3 popular articles ordered with most popular
        articles on top
        '''
        self.cursor.execute(
            '''SELECT title, views
            FROM article_views
            ORDER BY views DESC
            LIMIT 3''')
        articles = self.cursor.fetchall()
        return articles

    def get_most_popular_authors(self):
        '''Provides the authors whose articles have more views ordered with
        most popular authors on top
        '''
        self.cursor.execute(
            '''SELECT authors.name, SUM(article_views.views) AS views
            FROM authors
            JOIN article_views
            ON authors.id = article_views.author
            GROUP BY authors.id
            ORDER BY views DESC
            ''')
        authors = self.cursor.fetchall()
        return authors

    def get_daily_error_percentage(self):
        '''Provides the days when the requests error percentage is above 1%'''
        self.cursor.execute(
            '''SELECT r.day, ((e.errors * 100) / r.requests) AS error_percentage
            FROM daily_requests AS r
            JOIN daily_errors AS e
            ON r.day = e.day
            WHERE ((e.errors * 100) / r.requests) > 1
            ''')
        daily_percentage = self.cursor.fetchall()
        return daily_percentage
