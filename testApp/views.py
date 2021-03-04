from django.shortcuts import render

def post_list(request):
    return render(request, 'testApp/post_list.html', {})