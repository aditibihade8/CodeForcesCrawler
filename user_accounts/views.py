from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
	return render(request, 'accounts/index.html')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')


def stats(request):
	return render(request, 'accounts/stats.html')

def schedule(request):
	colz = tt_generator()
	return render(request, 'accounts/schedule.html' , {"cols" : colz})
	# PUT STUFF HERE

def tt_generator() :
    
    page = requests.get("http://codeforces.com/contests")
    soup = BeautifulSoup(page.content, 'html.parser')
    table1 = soup.find('div' , attrs = {'class' : 'datatable'})
    rows = table1.find_all('tr')
    del rows[0]
    #rows
    #cols = rows[1].find_all('td')

    for row in rows :
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        
        yield cols
