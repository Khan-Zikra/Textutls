
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which check box is on
    if(removepunc == "on"):
    #analyzed = djtext
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed = ""
       for char in djtext:
           if char  not in punctuations:
               analyzed = analyzed + char
       params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed }
       djtext = analyzed
       #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed= analyzed + char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover== "on"):
        analyzed= ""
        for char in djtext:
            if char !="\n" and char!="\r" :
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover== "on"):
        analyzed= ""
        for index, char in  enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]==" "):
                analyzed= analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select any opration and try again")

    return render(request, 'analyze.html', params)


