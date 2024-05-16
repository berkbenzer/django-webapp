from django.shortcuts import render, HttpResponse
from .practice_verbs import GermanPractice



def home_view(request):
    return render(request, "home.html", {})

def homepage_view(request):
    return render(request, "home.html", {})

def artickle_view(request):
    return render(request, "artikles.html", {})

def verbs_view(request):
    return render(request, "verbs.html", {})

def translation_view(request):
    return render(request, "translation.html", {})

def jenkins_view(request):
    return render(request, "jenkins.html", {})

def aws_view(request):
    return render(request, "aws.html", {})


def terraform_view(request):
    return render(request, "terraform.html", {})

def kubernetes_view(request):
    return render(request, "kubernetes.html", {})


def index_view(request):
    return render(request, "techindex.html", {})

def verbs_view(request):
    practice = GermanPractice()
    if request.method == 'POST':
        if 'practice_verbs' in request.POST:
            # Get user input from form
            user_input = request.POST.get('user_input', '').strip().lower()
            # Retrieve stored verb details from session
            stored_verb, stored_item, stored_form = request.session.get('current_verb'), request.session.get('current_item'), request.session.get('correct_form')

            if user_input == stored_form:
                message = "Correct! Try another one."
            else:
                message = f"Incorrect! The correct form for '{stored_verb}' in '{stored_item}' is '{stored_form}'. Try this one."

            # Fetch a new verb after checking the answer
            chosen_verb, chosen_item, correct_form = practice.practice_verbs()
            # Store new verb details in session
            request.session['current_verb'], request.session['current_item'], request.session['correct_form'] = chosen_verb, chosen_item, correct_form
            # Render response with feedback and new verb
            return render(request, 'verbs.html', {'message': message, 'chosen_verb': chosen_verb, 'chosen_item': chosen_item, 'correct_form': None})

        elif 'quit' in request.POST:
            # Handle quit action
            return HttpResponse('Take care!')

    else:
        # Handle initial loading and verb generation for GET request
        chosen_verb, chosen_item, correct_form = practice.practice_verbs()
        # Store the initial verb details in the session
        request.session['current_verb'], request.session['current_item'], request.session['correct_form'] = chosen_verb, chosen_item, correct_form
        # Render the initial form without user input
        return render(request, 'verbs.html', {'chosen_verb': chosen_verb, 'chosen_item': chosen_item, 'correct_form': None})

    # Default return in case none of the conditions above are met
    return render(request, 'verbs.html')