from django.shortcuts import render
from.models import Contact
from.models import Blog
from.models import Aboutme
from calendar import HTMLCalendar
from datetime import date
from django.db import connection
from tabulate import tabulate




def about(request):

    pt3 = Aboutme.objects.all()

    return render(request,'about.html', {"pt3":pt3})


def resume(request):

    return render(request,'resume.html', {})


def calen(request, year=date.today().year, month=date.today().month):

    cal = HTMLCalendar().formatmonth(year, month)

    today_events = connection.cursor()

    try:

        today_events.execute("SELECT count (start_time) FROM mywebpage_event WHERE date(start_time) = date('now')")

    finally:

        query = (tabulate(today_events, tablefmt='html'))

        return render(request,'calendar.html', {"cal":cal, "query":query})


def skills(request):

    return render(request,'skills.html', {})


def contact(request):



    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()

    pt2 = connection.cursor()
    pt2.execute("select count(message) FROM mywebpage_contact")
    pt2query = (tabulate(pt2, tablefmt='html'))

    return render (request,'contact.html', {"pt2query":pt2query})




def comments(request):

    pt1 = Blog.objects.all()
    return render(request,'comments.html', {'pt1':pt1})


def linkedin ():

    return render ('https://www.linkedin.com/in/sebastien-gadiou-b532a1210')

#