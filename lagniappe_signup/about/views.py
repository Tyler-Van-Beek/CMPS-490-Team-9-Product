from django.shortcuts import render

def about_page(request):
    """
    View function for the About Us page.
    """
    return render(request, 'about/about.html')  # Ensure this template exists
