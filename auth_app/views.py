from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from django.http import JsonResponse
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer  # Import your CustomUserSerializer here
from listings.serializers import ListingSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            address = data.get('address')
            city_town = data.get('city_town')
            username = data.get('username')
            agreed_to_terms = data.get('agreed_to_terms')
            agreed_to_privacy_policy = data.get('agreed_to_privacy_policy')

            # Check if the required fields are provided
            if not (first_name and last_name and email and password and address and city_town and username):
                return JsonResponse(
                    {'status': 'bad_request', 'message': 'Missing required fields'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'username': username,
                'address': address,
                'city_town': city_town,
                'agreed_to_terms': agreed_to_terms,
                'agreed_to_privacy_policy': agreed_to_privacy_policy,
            }

            print("User Data: ", user_data)  # Debugging line

            try:
                print("Before Serializer")
                serializer = CustomUserSerializer(data=user_data)
                print("After Serializer")
                if serializer.is_valid():
                    print("Serializer is valid")
                    serializer.save()
                    print("Serializer saved")
                    return JsonResponse({'status': 'success', 'message': 'User created successfully', 'redirect': 'homepage'}, status=201)

                else:
                    print("Serializer is not valid")
                    print("Serializer errors:", serializer.errors)
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except json.JSONDecodeError as e:
                print("JSONDecodeError: ", e)
                return JsonResponse({'status': 'bad_request', 'message': 'Invalid JSON data'}, status=400)
            except ValueError as e:
                print("ValueError: ", e)
                return JsonResponse({'status': 'bad_request', 'message': str(e)}, status=400)
            except Exception as e:
                print("General Exception: ", e)
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            else:
                print("No exceptions, but fell through to 'else'")
                return JsonResponse({'status': 'bad_request'}, status=400)
                
        except Exception as e:
            print("Outer Exception: ", e)
            return JsonResponse({'status': 'error', 'message': 'An error occurred'}, status=500)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not (username and password):
            return Response(
                {'status': 'bad_request', 'message': 'Missing required fields'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(
                {'status': 'success', 'message': 'Logged in successfully'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'status': 'failed', 'message': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

    return Response({'status': 'bad_request'}, status=status.HTTP_400_BAD_REQUEST)


# class RegisterUserView(APIView):

#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)

#         if serializer.is_valid():
#             new_user = serializer.save()

#             # Generate and return Token
#             token, created = Token.objects.get_or_create(user=new_user)

#             # Send verification or welcome email
#             send_mail(
#                 'Welcome to My App',
#                 'Here is your verification code.',
#                 'from@example.com',
#                 [new_user.email],
#                 fail_silently=False,
#             )

#             # Redirect to homepage
#             return HttpResponseRedirect('/')

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
