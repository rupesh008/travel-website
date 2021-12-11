from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

     dest1 = Destination()
     dest1.name = 'Mumbai'
     dest1.desc = 'The city that never sleeps'
     dest1.price = 700
     dest2 = Destination()
     dest2.name = 'Delhi'
     dest2.desc = 'Delhi the capital of india'
     dest2.price = 600
     dest3 = Destination()
     dest3.name = 'kolkata'
     dest3.desc = 'The City of Joy'
     dest3.price = 500
     dest4 = Destination()
     dest4.name = 'Banglore'
     dest4.desc = 'The IT City of India'
     dest4.price = 400
     return render(request,'index.html',{'dest1': dest1,'dest2': dest2,'dest3':dest3,'dest4':dest4})
