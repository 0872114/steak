from django.shortcuts import render_to_response, redirect

def main_page(request):
    return render_to_response('content/main_page.html')

def about(request):
    return render_to_response('content/about.html')

def printing1(request):
    return render_to_response('content/printing1.html')

def printing2(request):
    return render_to_response('content/printing2.html')

def printing3(request):
    return render_to_response('content/printing3.html')