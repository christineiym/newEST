# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from typing import List
from django.template import loader
import os


DATE_FORMAT_LENGTH: int = 10
TIME_FORMAT_LENGTH: int = 8
SECRET_KEY_NEWSAPI = os.environ['SECRET_KEY_NEWSAPI']

def index(request):
    """Displays all news articles related to entertainment, sports, or tech."""
    from newsapi import NewsApiClient
    import json

    # Initialize API KEY
    newsapi = NewsApiClient(api_key='SECRET_KEY_NEWSAPI')
    entertainment_articles = newsapi.get_top_headlines(category='entertainment')
    sports_articles = newsapi.get_top_headlines(category='sports')
    technology_articles = newsapi.get_top_headlines(category='technology')
    all_articles = entertainment_articles['articles'] + sports_articles['articles'] + technology_articles['articles']

    article_headline = []
    article_url = []
    article_source = []
    article_author = []
    article_date = []
    article_time = []
    article_description = []
    article_image = []
    article_content = []

    for i in range(len(all_articles)):
        myarticles = all_articles[i]
        article_headline.append(myarticles['title'])
        article_url.append(myarticles['url'])
        article_source.append(myarticles['source']["name"])
        article_author.append(myarticles['author'])
        article_date.append(myarticles['publishedAt'][0:DATE_FORMAT_LENGTH])
        article_time.append(myarticles['publishedAt'][(DATE_FORMAT_LENGTH + 1):(DATE_FORMAT_LENGTH + 1 + TIME_FORMAT_LENGTH)])
        article_description.append(myarticles['description'])
        article_image.append(myarticles['urlToImage'])
        article_content.append(myarticles['content'])
        
    mylist = zip(article_headline, article_url, article_source, article_author, article_date, article_time, article_description, article_image)
    
    return render(request, 'newEST/index.html', context={"mylist":mylist})