#!/usr/bin/env python3

from newsdb import get_popular_article, get_popular_author, get_request_error


def display_popular_article():
	"""Display formatted articles for each article in the database""" 
	popular_article = get_popular_article()
	for title, no_view in popular_article:
		print(f"{title} -- {no_view} views")


def display_popular_author():
	"""Display formatted authors for each author in the database"""
	popular_author = get_popular_author()
	for author, no_view in popular_author:
		print(f"{author} -- {no_view} views")
    
        
def display_request_error():
	"""Display request error in the database"""
	request_error = get_request_error()
	for date, error in request_error:
		print(f"{date} -- {error}% errors")

def display_results():
    print("\n1. What are the most popular three articles of all time?\n")
    display_popular_article()
    print()
    print("\n2. Who are the most popular article authors of all time?\n") 
    display_popular_author()
    print()
    print("\n3. On which days did more than 1% of requests lead to errors?\n")
    display_request_error()

# display results
display_results()

