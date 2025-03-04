from django.shortcuts import render, redirect
from .forms import ComplaintForm

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_success')  # Redirect to success page
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_form.html', {'form': form})

def complaint_success(request):
    return render(request, 'complaints/complaint_success.html')
