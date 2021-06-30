from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("hello Bhavya")
def htmltag(request):
	return HttpResponse("<h1>Hello Bhavya How are u</h1>")

def username(request,username):
	return HttpResponse("<h1>Hello <span style='color:red'>{}</span></h2>".format(username))

def user(request,username,age):
	return HttpResponse("<h1 style='text-align:center'>Hello {} and your age is {}</h1>".format(username,age))

def emp(request,username,id,sal):
	return HttpResponse("<script>alert('hello {}')</script><h1 style='background-color:pink'>Hello ms {} your name is {} and your sal is {}</h1>".format(username,id,username,sal))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,id,name):
	k={'i':id,'n':name}
	return render(request,'html/ytname.html',k)

def studentdetails(request):
	return render(request,'html/stddetails.html')

def internalJs(request):
	return render(request,'html/internalJs.html')

def myform(request):
	if request.method=="POST":
		#print(request.POST)
		uname=request.POST['uname']
		rollnum=request.POST['rollnum']
		mail=request.POST['mail']
		#print(uname,rollnum,mail)
		data={'u':uname,'r':rollnum,'e':mail}
		return render(request,'html/display.html',data)

	return render(request,'html/myform.html')

def register(request):
	if request.method=='POST':
		uname=request.POST['uname']
		mail=request.POST['email']
		pno=request.POST['pno']
		gender=request.POST['gender']
		add=request.POST['add']
		#print(fname,lname,mail,pno,gender,add)
		data={'u':uname,'m':mail,'p':pno,'g':gender,'a':add}
		return render(request,'html/registerdisplay.html',data)
	return render(request,'html/register.html')

def btrg(request):
	return render(request,'html/btr.html')


def register1(request):
	#name="sai"
	#email="sai@gmail.com"
	#reg=Register.objects.create(name="bhavya",email="bhavya@gmail.com")
	#reg.save()
	data1=Register.objects.filter(id=31).delete()
	return HttpResponse("row deleted sucessfully..")

def register2(request):
	if request.method=="POST":
		name=request.POST.get('name')
		email=request.POST.get('mail')
		reg=Register.objects.create(name=name,email=email)
		return HttpResponse("data enterend")
	return render(request,'html/register2.html')

def display2(request):
	a=Register.objects.all()
	return render(request,'html/display2.html',{'a':a})

def view2(request,num):
	re=Register.objects.get(id=num)
	return HttpResponse("your name is {} and your email id is {}".format(re.name,re.email))