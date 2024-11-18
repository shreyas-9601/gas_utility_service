from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Request submitted successfully!"})
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'customer_service/track_request.html', {'service_request': service_request})