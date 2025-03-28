from django.shortcuts import render,redirect
from django.contrib import messages
from userapp.models import *
from django.utils.datastructures import MultiValueDictKeyError
from nltk.stem import WordNetLemmatizer
import pickle    
import re
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
from adminapp.models import * 
from sklearn.model_selection import train_test_split
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.


def admin_dashboard(request):
    user_id = request.session["user_id_after_login"]
    user = User.objects.get(pk = user_id)
    context = {
        'la' : user,
    }
    return render(request, "admin_dashboard.html",context)





import nltk
nltk.download('wordnet')  # Ensure WordNet is downloaded

from nltk.stem import WordNetLemmatizer
wo = WordNetLemmatizer()



wo = WordNetLemmatizer()

def preprocess(data):
    # Preprocess
    a = re.sub('[^a-zA-Z]', ' ', data)
    a = a.lower()
    a = a.split()
    a = [wo.lemmatize(word) for word in a]
    a = ' '.join(a)
    return a

tfidf_vectorizer = pickle.load(open('userapp/models/vectorizer.pkl', 'rb'))
model = pickle.load(open('userapp/models/prediction.pkl', 'rb'))

from django.http import JsonResponse
from django.core.mail import send_mail


def predict(request):
    user_id = request.session.get('user_id_after_login')
    print("User ID from session:", user_id)
    if not user_id:
        return JsonResponse({'error': 'User not logged in'}, status=400)
    
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        msg = request.POST.get('mood_pred', '')
        if msg:
            a = preprocess(msg)
            pred = model.predict(tfidf_vectorizer.transform([a]))[0]
            
            if pred == 0:
                final_result = "No Mental Health Detected"
                quote = "Be Happy, Be Bright, Be You"
            elif pred == 1:
                final_result = "Mental Health Detected"
                quote = "Consult Your Doctor"

            # Store prediction in database
            PredictionHistory.objects.create(
                user=user,
                input_text=msg,
                prediction_result=final_result
            )

            # Send email to the user
            subject = 'Mental Health Status Prediction Result'
            message = f"Dear {user.full_name},\n\nYour mental health status has been evaluated. Here are the results:\n\nPrediction: {final_result}\n\nQuote: {quote}\n\nBest regards,\nYour Mental Health Companion"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]

            send_mail(subject, message, from_email, recipient_list)

            return JsonResponse({'final_result': final_result})  

    return JsonResponse({'error': 'Invalid request'}, status=400)




def detection(request):
    
    return render(request, "detection.html")




import json, re, requests
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from .models import PredictionHistory



@csrf_exempt
def select_therapy(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prediction_id = data.get('prediction_id')
        therapy_type = data.get('therapy_type') 
        
        try:
            prediction = PredictionHistory.objects.get(pk=prediction_id)
        except PredictionHistory.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid prediction ID'})
        
        user_input = prediction.input_text
        
        # Perplexity API setup
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        if therapy_type == 'music':
            system_message = (
                "You are a creative AI that generates a list of exactly 5 YouTube video links for music therapy. "
                "Based on the following user input, provide exactly 5 valid YouTube video links separated by commas. "
                "Return only the links with no extra text."
            )
        elif therapy_type == 'workout':
            system_message = (
                "You are a professional fitness trainer. Based on the following user input, generate a concise guided workout plan. "
                "Provide only the essential steps in plain text (limit the answer to 5 lines maximum). "
                "Do not include extra explanations or markdown formatting."
            )
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid therapy type'})
        
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ]
        
        payload = {"model": "sonar", "messages": messages}
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            try:
                bot_response = response.json()['choices'][0]['message']['content']
                # Remove markdown formatting and reference numbers
                bot_response = re.sub(r'(\*\*|__|\*|_)', '', bot_response)
                bot_response = re.sub(r'\[\d+\]', '', bot_response)
                # Decode any unicode escape sequences (e.g. \u0027 -> ')
                bot_response = bot_response.encode('utf-8').decode('unicode_escape')
                
                if therapy_type == 'music':
                    # Expect a comma-separated list of links
                    links = [link.strip() for link in bot_response.split(',') if link.strip()]
                    if len(links) >= 5:
                        links = links[:5]
                    prediction.music_therapy_links = links
                    prediction.save()
                    message = "Music Therapy links updated!"
                else:  # therapy_type == 'workout'
                    # Split the response into lines and keep at most 5 lines
                    lines = bot_response.splitlines()
                    short_plan = "\n".join(lines[:5])
                    if len(lines) > 5:
                        short_plan += "\n..."
                    prediction.guided_workout_plan = short_plan
                    prediction.save()
                    message = "Guided Workout plan updated!"
                    
                return JsonResponse({'status': 'success', 'message': message})
            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error', 'message': 'Error processing API response'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to get response from API'}, status=response.status_code)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)




def result(request):
    user_id = request.session.get('user_id_after_login')
    if not user_id:
        return render(request, "results.html", {'predictions': []})

    user = User.objects.get(pk=user_id)
    predictions = PredictionHistory.objects.filter(user=user).order_by('-timestamp')

    return render(request, "results.html", {'predictions': predictions})





import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from userapp.models import User
from .models import PredictionHistory





def download_specific_report(request, prediction_id):
    # Get the user id from the session
    user_id = request.session.get('user_id_after_login')
    if not user_id:
        return HttpResponse("User not logged in", status=403)
    
    # Get the specific prediction object
    prediction = get_object_or_404(PredictionHistory, id=prediction_id, user_id=user_id)
    
    # Create a CSV file in memory
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="prediction_{prediction.id}_report.csv"'
    
    writer = csv.writer(response)
    # Write CSV header
    writer.writerow(['Input Text', 'Prediction Result', 'Timestamp', 'Music Therapy Links', 'Guided Workout Plan'])
    
    # Write the specific prediction's data
    writer.writerow([
        prediction.input_text,
        prediction.prediction_result,
        prediction.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        ", ".join(prediction.music_therapy_links) if prediction.music_therapy_links else "",
        prediction.guided_workout_plan
    ])
    
    return response

def download_report(request):
    # Get the user id from the session
    user_id = request.session.get('user_id_after_login')
    if not user_id:
        return HttpResponse("User not logged in", status=403)
    
    user = get_object_or_404(User, pk=user_id)
    predictions = PredictionHistory.objects.filter(user=user).order_by('-timestamp')
    
    # Create a CSV file in memory
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prediction_report.csv"'
    
    writer = csv.writer(response)
    # Write CSV header
    writer.writerow(['Input Text', 'Prediction Result', 'Timestamp', 'Music Therapy Links', 'Guided Workout Plan'])
    
    # Write each prediction's data
    for pred in predictions:
        writer.writerow([
            pred.input_text,
            pred.prediction_result,
            pred.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            ", ".join(pred.music_therapy_links) if pred.music_therapy_links else "",
            pred.guided_workout_plan
        ])
    
    return response




from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def Feedback(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        # print(review, rating)
        feed_id = request.session["user_id_after_login"]
        user_id = User.objects.get(pk = feed_id)
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(review)
        sentiment = None
        if score['compound'] >= 0.5:
            sentiment = 'Very Positive'
        elif score['compound'] >= 0:
            sentiment = 'Positive'
        elif score['compound'] >- 0.5:
            sentiment = 'Neutral' 
        elif score['compound'] >- 1:
            sentiment = 'Negative'
        else:
            sentiment = 'Very negative'
        FeedbackModel.objects.create(Rating = rating, Review = review, Sentiment = sentiment, user = user_id)
        # print(sentiment, rating)
        messages.success(request, 'Feedback was Submitted')
        return redirect("feedback")
    return render(request, 'feedback.html')




def user_profile(request):
    user_id = request.session.get('user_id_after_login')
    print(user_id)
    user = User.objects.get(pk=user_id)
    
    if request.method == "POST":
        # Get values from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('location')

        # Update only if the value is not empty
        if name:
            user.full_name = name
        if email:
            user.email = email
        if phone:
            user.phone_number = phone
        if password:
            user.password = password
        if location:
            user.address = location
        
        # Handle profile image upload (only update if a new image is provided)
        try:
            profile = request.FILES['profile']
            user.photo = profile
        except MultiValueDictKeyError:
            # If no new profile is provided, keep the existing one
            pass

        # Save the user object with the updated fields
        user.save()
        messages.success(request, 'Updated successfully!')
        return redirect('user_profile')

    return render(request, 'profile.html', {'user': user})






import time
def admin_logout(request):
    user_id = request.session["user_id_after_login"]
    user = User.objects.get(pk = user_id) 
    t = time.localtime()
    user.Last_Login_Time = t
    current_time = time.strftime('%H:%M:%S', t)
    user.Last_Login_Time = current_time
    current_date = time.strftime('%Y-%m-%d')
    user.Last_Login_Date = current_date
    user.save()
    request.session.flush() 
    messages.success(request, "Logged out successfully.")
    return redirect("login") 




import re
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Conversation
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def user_chatbot(request):
    # Retrieve the logged-in user from the session
    user_id = request.session.get('user_id_after_login')
    user = None
    if user_id:
        user = User.objects.filter(id=user_id).first()
    
    # Only show previous conversations for the logged-in user
    conversations = Conversation.objects.filter(user=user).order_by('created_at')
    
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()
        if user_message:
            # Build messages payload including conversation history
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a compassionate and knowledgeable mental health support chatbot. "
                        "Your sole purpose is to provide guidance, support, and self-care tips for mental health concerns. "
                        "Do not discuss topics unrelated to mental health, such as movies, sports, politics, or entertainment. "
                        "If a user asks about unrelated topics, politely steer the conversation back to mental health and well‑being. "
                        "You are a caring and empathetic mental health care doctor. Your tone should be supportive and friendly. "
                        "When a user sends a simple greeting or introduces themselves (for example, 'hi, I am Uppi'), reply with a warm, casual greeting that uses their name if provided (e.g., 'Hello Uppi, how are you today?'). "
                        "For more complex questions or mental health concerns, provide thoughtful and supportive guidance. "
                        "Always respond in plain text with no markdown formatting, no bold or italic symbols, and no reference numbers."
                        "you can give links to the videos like youtube, that need to be clickable so user can navigate"
                    )
                },
            ]
            
            # Append previous conversation history
            for conv in conversations:
                messages.append({
                    "role": "user",
                    "content": conv.user_message
                })
                messages.append({
                    "role": "assistant",
                    "content": conv.bot_response
                })
            
            # Append the current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            payload = {
                "model": "sonar",
                "messages": messages
            }
            
            headers = {
                "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(
                "https://api.perplexity.ai/chat/completions",
                json=payload,
                headers=headers
            )
            
            bot_response = "Error: Could not get response from AI"
            if response.status_code == 200:
                try:
                    bot_response = response.json()['choices'][0]['message']['content']
                    # Clean up response by removing markdown symbols and reference numbers
                    bot_response = re.sub(r'(\*\*|__|\*|_)', '', bot_response)
                    bot_response = re.sub(r'\[\d+\]', '', bot_response)
                except Exception as e:
                    print(e)
            
            # Save conversation with the associated user
            Conversation.objects.create(
                user=user,
                user_message=user_message,
                bot_response=bot_response
            )
            
            return redirect('user_chatbot')
    
    return render(request, 'chatwithbot.html', {'conversations': conversations})




def new_chat(request):
    user_id = request.session.get('user_id_after_login')
    if user_id:
        Conversation.objects.filter(user_id=user_id).delete()
    return redirect('user_chatbot')





def mood_assistance(request):
    return render(request, 'mood.html')



import random

def mood_response(request, mood):
    # Define a set of messages for each mood
    mood_messages = {
                'happy': [
                    "I am feeling great today.", 
                    "I am in a really good mood.",
                    "I feel positive and full of energy.", 
                    
                ],
                'calm': [
                    "I feel at peace today.", 
                    "I am calm and relaxed.", 
                    "I'm feeling neutral, not too high or too low.", 
                    "I feel calm and collected."
                ],
                'manic': [
                    "I feel anxious and restless.", 
                    "I am feeling agitated and on edge.", 
                    "I’m feeling like I can’t slow down.", 
                    "I feel like my mind is racing.", 
                    "I feel like I’m being pushed to the happy limit.", 
               

                ],
                'angry': [
                    "I am feeling frustrated and upset.", 
                    "I feel irritated and angry today.", 
                    
                    "I feel disappointed and upset.", 
                    "I’m angry about little things that shouldn’t bother me.", 
                 
                ],
                'sad': [
           
                    "I feel sad and discouraged.", 
     
                    "I feel sad and like I don’t have the energy to keep going.", 
                    
                ]
            }


    # Get a random message based on the selected mood
    selected_message = random.choice(mood_messages.get(mood, ["Stay positive!"]))

    return render(request, 'mood_response.html', {'mood': mood, 'message': selected_message})




def yoga_poster(request):
    return render(request, 'yoga.html')
