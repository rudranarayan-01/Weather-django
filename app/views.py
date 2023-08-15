from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def weather_app(request):
    if request.method == "POST":
        latt = request.POST.get('latt')
        longg = request.POST.get('longg')
        print(latt,longg)

    return render(request,'weather.html',{"latt":latt,"longg":longg})