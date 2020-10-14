from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hithere':'This is me'})

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            #Increase
            worddic[word] +=1
        else:
            #Add to the dictionary
            worddic[word] =1

            sortedword = sorted(worddic.items(), key=operator.itemgetter(1), reverse = True)

    return render(request,'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedword':worddic.items})
