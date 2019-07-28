from django.shortcuts import render,redirect
from django.http import HttpResponse
import pyttsx3

# Create your views here.



def index(request):

    return render(request,'generator/index.html')

def checker(request):
    if request.method=='GET':
        innum = request.GET['inputtext']
        num_words = 0
        words = innum.split(" ")
        num_words += len(words)
        print("Number of words:")
        print(num_words)
        if(num_words>1000):
                flag = 'Sorry!!! Word Limit is 1000. You have used '+ str(num_words)+' words'
                return render(request,'generator/index.html', {'flag': flag})
        else:
                engine = pyttsx3.init()
                engine.say("{}".format(innum))
                engine.runAndWait()
                return redirect('/')
