from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):

    peoples =[
        {'name':'abhijeet', 'age':21},
        {'name':'deep', 'age':16},
        {'name':'kahti', 'age':25},
        {'name':'som', 'age':15},
        {'name':'khati', 'age':19},

    ]

    for people in peoples:
        if people['age'] :
            print('yes')

    vegetables = ['tomato' , 'potato' , 'pumpkon']
    

    text= """ 
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus corrupti ipsum totam eos magnam, voluptatum dolorem beatae dolore obcaecati eum voluptates perferendis quis explicabo sit nobis, error rerum. Ad, iste?
    """
    return render(request , "home/index.html",context={ 'page':'this is django tutorial','peoples':peoples, 'text': text , 'vegetables':vegetables})


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>hey dis is a success page</h1>")


def contact_page(request):
    context={'page':'Contact'}
    return render(request , "home/contact.html", context )


def about_page(request):
    context={'page':'About'}
    return render(request , "home/about.html",context)

