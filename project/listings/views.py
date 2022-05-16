from django.shortcuts import render

from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator



# Create your views here    


def listings(request):
    #listing_data=Listing.objects.all()
    #context={'listing':listing_data}
    
    contact_list = Listing.objects.all()
    paginator = Paginator(contact_list, 1) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'listing': page_obj}
    return render(request,'listings/listings.html',context)

def listone(request):
    return render(request,'listings/listone.html')

def search(request):
    return render(request,'listings/search.html')



