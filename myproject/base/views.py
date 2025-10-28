from django.shortcuts import render

# Create your views here.

articles_data=[
    {
        'id':1,
        'title':'indian technology',
        'desc':'''
    this is all about indian tec Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':2,
        'title':'indian economy',
        'desc':'''
    this is all about indian economy Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':3,
        'title':'qspiders',
        'desc':'''
    this is all about qspiders tec Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':4,
        'title':'america taxes',
        'desc':'''
    this is all about america tec Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':5,
        'title':'china technology',
        'desc':'''
    this is all about china tec Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

    


]


def home(request):

    context={
        'article_data':articles_data
    }

    return render(request,'home.html',context)

def read(request,pk):
     print(pk)
     print(type(pk))
     
     for i in articles_data:
        #  print(i['id']) 
        if i['id']==pk:
         context={
             'article':i
         }
         return render(request,'read.html',context)
         

def news(request):


    return render(request,'news.html')

articles_events=[
    {
        'id':11,
        'title':'Ganesha festival',
        'desc':'''
    this is all about Ganesha festival Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':12,
        'title':'Birthday',
        'desc':'''
    this is all about Birthday Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':13,
        'title':'Engagement',
        'desc':'''
    this is all about Engagement Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':14,
        'title':'Office party',
        'desc':'''
    this is all about Office party Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },

     {
        'id':15,
        'title':'Marriage',
        'desc':'''
    this is all about Marriage Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti 
'''
    },


]

def events(request):
    context={
        'articles_events':articles_events
    }

    return render(request,'events.html',context)
def readmore(request,pk):
     print(pk)
     print(type(pk))
     
     for i in articles_events:
        #  print(i['id']) 
        if i['id']==pk:
         context={
             'article_event':i
         }
         return render(request,'readmore.html',context)

def about(request):

    about_data='''
   Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit eaque unde officiis numquam sint, inventore ipsa aspernatur voluptatem ullam voluptates odit quaerat vel odio. Praesentium perferendis totam soluta. Quasi veritatis quod iste, voluptate perspiciatis velit eius obcaecati laboriosam sint ab sit odit quia placeat quo mollitia saepe quis maxime magnam ad, temporibus, dicta voluptatibus officia delectus! Nulla dolores impedit, delectus sunt debitis enim hic magnam excepturi unde eveniet ipsum est voluptas aliquam possimus, ratione adipisci quod! Voluptates corrupti provident reiciendis aperiam voluptate distinctio repellendus, ducimus error possimus officiis nulla tempora iusto sunt nesciunt eum ipsam modi molestiae, nostrum sint culpa.
'''


    return render(request,'about.html',{'about_data':about_data})