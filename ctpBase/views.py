from django.shortcuts import render

# Create your views here.
def search_list(request):
    return render(request, 'ctpBase/search_list.html', {})
