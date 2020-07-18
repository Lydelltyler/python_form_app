from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "index.html")

def save_info(request):
    print("Got the POST info .......................")
    name = request.POST['your_name']
    location = request.POST['dojo_location']
    language = request.POST['language']
    comment = request.POST['comment']
    
    context = {
        "name_in_form": name,
        "location_in_form": location,
        "language_in_form": language,
        "comment_in_form": comment
        
    }
    
    print(request.POST)
    return render(request, "info.html", context)




