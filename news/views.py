from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article
# Create your views here.

def news_of_day(request):
    date=dt.date.today()
    day=convert_dates(date)
    news= Article.objects.all()


    return render (request,'all-news/today-news.html',{"date":date,"news":news})
def convert_dates(dates):
    #function that gets the weekday number for the date.
    day_number=dt.date.weekday(dates)
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','saturday','Sunday']

    #Returning the actual day of the week
    day = days[day_number]
    return day
def past_days_news(request,past_date):
    #converts data from the string url into date format
    try:
        date=dt.datetime.strptime(past_date,'%y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False
    day=convert_dates(date)
    #we get the day of the date
    if date == dt.date.today():
        return redirect(news_of_day)


    return render (request, 'all-news/past-news.html',{"date":date})
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term=request.GET.get("article")
        searched_articles=Article.search_by_title(search_term)
        message=f"{search_term}"
        return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})
    else:
        message ="you haven't searched for any term"
        return render(request,'all-news/search.html',{"message":message})
def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html",{"article":article})
