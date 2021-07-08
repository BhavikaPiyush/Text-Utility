from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')
#
def about(request):
   return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter', 'off')
    purpose = ""

    if djtext=="":
        return HttpResponse("Error: Please enter some text to be analyzed")

    else:
        if removepunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            djtext = analyzed
            purpose += "Removed Punctuations"

        if fullcaps == 'on':
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            djtext = analyzed
            purpose += "| Changed to uppercase"

        if newlineremover == 'on':
            analyzed = ""
            for char in djtext:
                if char != '\n' and char != "\r":
                    analyzed = analyzed + char
            djtext = analyzed
            purpose += "| Removed New Lines"

        if extraspaceremover == 'on':
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
            djtext = analyzed
            purpose += "| Removed Space"

        if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on':
            return HttpResponse("Error: Please select at least one operation")

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
