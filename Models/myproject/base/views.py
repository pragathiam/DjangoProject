from django.shortcuts import render,redirect
from base.models import ArticleModel

# Create your views here.

def home(request):
    # print('home view triggered')
    # print(request) # <WSGIRequest: GET '/'>
    # print(request.method) # GET
    # print(request.GET) 
    # <QueryDict: {}>
    # <QueryDict: {'title': ['india'], 'desc': ['alll about india']}>

    # MultiValueDictKeyError 
    # if 'title_attr' in request.GET:
    #     title_data=request.GET['title_attr']
    #     desc_data=request.GET['desc_attr']
    #     print(title_data,desc_data)
    #     ArticleModel.objects.create(title=title_data,desc=desc_data)

    # post method 

    print(request.method)

    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        # print(title_data,desc_data)
        ArticleModel.objects.create(title=title_data,desc=desc_data)


# read
    article_data=ArticleModel.objects.all()
    print(article_data)

    return render(request,'home.html',{'data':article_data})

def update(request,pk):
    article=ArticleModel.objects.get(id=pk)
    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        article.title=title_data
        article.desc=desc_data
        article.save()
        return redirect('home')

    return render(request,'update.html',{'data':article})

def delete_(request,pk):
    article=ArticleModel.objects.get(id=pk)
    article.delete()
    return redirect('home')