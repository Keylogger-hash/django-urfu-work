from django.shortcuts import render
from formsapp.form import StudentForm
from django.http import HttpResponse
# Create your views here.
def form_request(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            data = ['Your registration is completed successfully.<br />',
            'Name:', name, 'Email:', email, 'Username:', username]
            return HttpResponse(data)
    else:
        student = StudentForm()
        return render(request, 'form.html', {'form':student})
