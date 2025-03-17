from django.shortcuts import render

def faq_page(request):
    """
    View function for the FAQ page.
    """

    faqs = [
        {'question': 'Can I add photos or videos to my event listing?', 
         'answer': 'Yes, you can enhance your event listing by adding media such as images to make it more appealing.'},
        
        {'question': 'Do I need an account to create or join an event?', 
         'answer': 'Yes, you must sign up for an account to either create or join events on Lagniappe.'},

        {'question': 'Are you able to edit an event once creating it?', 
         'answer': 'Yes, you can edit event details after creating it by navigating to your events dashboard and selecting "Edit Event".'},
    ]

    return render(request, 'faq/faq.html', {'faqs': faqs})
