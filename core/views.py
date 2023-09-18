from django.http import JsonResponse
from .models import HomePage  # Import your HomePage model


def get_homepage_data(request):
    try:
        # Fetch the homepage data from the database (assuming you have only one homepage entry)
        homepage_data = HomePage.objects.first()
        
        if homepage_data:
            # Convert the model data to a dictionary
            data = {
                'title': homepage_data.title,
                'description': homepage_data.description,
                # Add more fields as needed
            }
            
            return JsonResponse(data)
        else:
            # Handle the case when there is no homepage data in the database
            return JsonResponse({'error': 'No homepage data found'})
    
    except Exception as e:
        # Handle exceptions (e.g., database errors) gracefully
        return JsonResponse({'error': str(e)})


# def get_homepage_data(request):
#     # Replace this with your logic to fetch homepage data from your database
#     homepage_data = {
#         'title': 'Your Homepage Title',
#         'description': 'Your homepage description.',
#         # Add more data fields as needed
#     }

#     return JsonResponse(homepage_data)