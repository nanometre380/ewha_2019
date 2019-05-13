from django.shortcuts import render
from .models import Fest
import csv

# Create your views here.

def home(request): #메인화면
    return render(request, 'index.html')

def first(request): #첫날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 1).order_by('booth_num')
    return render(request, 'first.html', {'booths':booths})

def second(request): #둘째날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 2).order_by('booth_num')
    return render(request, 'second.html', {'booths':booths})

def third(request): #셋째날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 3).order_by('booth_num')
    return render(request, 'third.html', {'booths':booths})

def import_fest(request): #csvimport하는 함수
    with open("ewhafest2019.csv") as f: #csv파일 열기
        reader = csv.reader(f) #reader함수 : iterator타입 reader 객체 return
        i = 0
        for row in reader: #한 행씩 접근
            if(row[0] == '888888'):
                break
            fest = Fest() #모델
            if(row[0] == ''):
                fest.date = -1
            else :
                fest.date = int(row[0])

            if(row[1] == ''):
                fest.place = -1
            else :
                fest.place = row[1]

            if(row[2] == ''):
                fest.booth_num = -1
            else :
                fest.booth_num = int(row[2])

            if(row[3] == ''):
                fest.name = -1
            else : fest.name = row[3]

            if(row[4] == ''):
                fest.sold_out = -1
            else : fest.sold_out = int(row[4])

            if(row[5] == ''):
                fest.password = -1
            else :
                fest.password = int(row[5])
            fest.detail = row[6]
            fest.save()

    return redirect('home')

def search(request): #검색
    try :
        kind = request.GET['kind']
        keyword = request.GET['search']
        date = request.GET['date']
    except :
        kind = request.GET['kind']
        keyword = request.GET['search']
        date = "none"

    if(kind == "name"):
        results = Fest.objects.filter(name__contains = keyword)
    else :
        results = Fest.objects.filter(detail__contains = keyword)
    return render(request, 'search.html', {'results':results, 'kind':kind, 'keyword':keyword, 'date':date})
