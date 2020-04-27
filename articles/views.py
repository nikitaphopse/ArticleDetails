from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import ArticleForm
from .models import Article
from .filters import ArticleFilter
from django.db.models import Count
import json


# Create your views here.


# def articles_list(request):
# context = {'articles_list': Article.objects.all()}
# return render(request, 'articles/articles_list.html', context)


def articles_list(request):
    article_list = Article.objects.all()
    myFilter = ArticleFilter(request.GET, queryset=article_list)
    article_list = myFilter.qs
    context = {'articles_list': article_list, 'myFilter': myFilter}
    return render(request, 'articles/articles_list.html', context)


# get and post function
def articles_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ArticleForm()
        else:
            art = Article.objects.get(pk=id)
            form = ArticleForm(instance=art)
        return render(request, 'articles/articles_form.html', {'form': form})
    elif request.method == 'POST':
        if id == 0:  # insert operation
            form = ArticleForm(request.POST)
        else:  # update operation
            art = Article.objects.get(pk=id)
            form = ArticleForm(request.POST, instance=art)
        if form.is_valid():
            form.save()
    return redirect('/articles/list')


def articles_delete(request, id):
    art = Article.objects.get(pk=id)
    art.delete()
    return redirect('/articles/list')


def get_chart(request):
    json_res = []
    result = Article.objects.values('storage_location').order_by('storage_location').annotate(count=Count('rfid'))

    [json_res.append(j) for j in ([(result[i]["storage_location"], result[i]["count"]) for i in range(len(result))])]

    dictionary = {str(i): [j] for i, j in json_res}
    print(dictionary)
    return JsonResponse(dictionary)

