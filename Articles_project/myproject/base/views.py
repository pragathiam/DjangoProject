from django.shortcuts import render,redirect
from base.models import TaskModel,HistoryModel
# Create your views here.
# article_data=[
#     {
#         'id':1,
#         'title':'indian politics',
#         'desc':'''
#     this is all about indian politics 
#     <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>    
# '''
#     },
#     {
#         'id':2,
#         'title':'indian tec',
#         'desc':'''
#      this is all about indian tec 
#     <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
# '''
#     },
#     {
#         'id':3,
#         'title':'indian eco',
#         'desc':'''
#     this is all about indian eco 
#     <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
# '''
#     },
#     {
#         'id':4,
#         'title':'america',
#         'desc':'''
#     this is all about indian america 
#     <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
# '''
#     },
#     {
#         'id':5,
#         'title':'china',
#         'desc':'''
#     this is all about indian china 
#     <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
# '''
#     },
# ]
def home(request):
    data=TaskModel.objects.all()
    # context={
    #     'data':article_data,
    #     'nav':True,
    #     'title':'thos is homepage'
    # }
    return render(request,'home.html',{'data':data})


def articles(request):   
     # print(request.GET)
    # print(request.POST)
    
    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        print(title_data,desc_data)
        TaskModel.objects.create(title=title_data,desc=desc_data)
        return redirect('home')

    return render(request,'articles.html')

def update(request,pk):
    data=TaskModel.objects.get(id=pk)

    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']

        data.title=title_data
        data.desc=desc_data
        data.save()
        return redirect('home')
        print(title_data,desc_data)
    
    return render(request,'update.html',{'data':data})

def confirm_delete(request,pk):
    data=TaskModel.objects.get(id=pk)

    return render(request,'confirm_delete.html',{'record':data})

def delete_(request,pk):
    data=TaskModel.objects.get(id=pk)
    HistoryModel.objects.create(title=data.title,desc=data.desc)
    data.delete()
    return redirect('home')

def history(request, pk):
    data = TaskModel.objects.get(id=pk)
    
 
 
