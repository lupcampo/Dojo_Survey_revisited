from django.shortcuts import render, redirect

# Create your views here.


from django.shortcuts import render, redirect
LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Java'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'Online'
)

# Create your views here.
def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'index.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
#Files
 #No file chosen  or 
#Add Github Url
