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


import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
import os
from django.conf import settings



words_data = {
    'der': {
        'Teppich': {'turkish_meaning': 'halı'},
        'Wein': {'turkish_meaning': 'şarap'},
        'Hund': {'turkish_meaning': 'köpek'},
        'Tisch': {'turkish_meaning': 'masa'},
        'Stuhl': {'turkish_meaning': 'sandalye'},
        'Mann': {'turkish_meaning': 'adam'},
        'Himmel': {'turkish_meaning': 'gökyüzü'},
        'Mond': {'turkish_meaning': 'ay'},
        'Wald': {'turkish_meaning': 'orman'},
        'Berg': {'turkish_meaning': 'dağ'},
        'Fluss': {'turkish_meaning': 'nehir'},
        'See': {'turkish_meaning': 'göl'},
        'Haus': {'turkish_meaning': 'ev'},
        'Fenster': {'turkish_meaning': 'pencere'},
        'Tür': {'turkish_meaning': 'kapı'},
        'Baum': {'turkish_meaning': 'ağaç'},
        'Stift': {'turkish_meaning': 'kalem'},
        'Zug': {'turkish_meaning': 'tren'},
        'Garten': {'turkish_meaning': 'bahçe'},
        'Vogel': {'turkish_meaning': 'kuş'},
        'Freund': {'turkish_meaning': 'arkadaş'},
        'Lehrer': {'turkish_meaning': 'öğretmen'},
        'Schuh': {'turkish_meaning': 'ayakkabı'},
        'Brief': {'turkish_meaning': 'mektup'},
        'Schlüssel': {'turkish_meaning': 'anahtar'},
        'Kopf': {'turkish_meaning': 'baş'},
        'Computer': {'turkish_meaning': 'bilgisayar'},
        'Bruder': {'turkish_meaning': 'erkek kardeş'},
        'Schrank': {'turkish_meaning': 'dolap'},
        'Fernsehen': {'turkish_meaning': 'televizyon'},
        'Kühlschrank': {'turkish_meaning': 'buzdolabı'}
        },
        'die': {
        'Dusche': {'turkish_meaning': 'duş'},
        'Brüder': {'turkish_meaning': 'erkek kardeşler'},
        'Apfel': {'turkish_meaning': 'elma'},
        'Frau': {'turkish_meaning': 'kadın'},
        'Katze': {'turkish_meaning': 'kedi'},
        'Blume': {'turkish_meaning': 'çiçek'},
        'Ente': {'turkish_meaning': 'ördek'},
        'Schule': {'turkish_meaning': 'okul'},
        'Sofas': {'turkish_meaning': 'koltuklar'},
        'Universität': {'turkish_meaning': 'üniversite'},
        'Stadt': {'turkish_meaning': 'şehir'},
        'Land': {'turkish_meaning': 'ülke'},
        'Sprache': {'turkish_meaning': 'dil'},
        'Musik': {'turkish_meaning': 'müzik'},
        'Blatt': {'turkish_meaning': 'yaprak'},
        'Straße': {'turkish_meaning': 'cadde'},
        'Zeitung': {'turkish_meaning': 'gazete'},
        'Zeitschrift': {'turkish_meaning': 'dergi'},
        'Tasche': {'turkish_meaning': 'çanta'},
        'Uhr': {'turkish_meaning': 'saat'},
        'Karte': {'turkish_meaning': 'harita'},
        'Maus': {'turkish_meaning': 'fare'},
        'Nacht': {'turkish_meaning': 'gece'},
        'Idee': {'turkish_meaning': 'fikir'},
        'Woche': {'turkish_meaning': 'hafta'},
        'Sonne': {'turkish_meaning': 'güneş'},
        'Arbeit': {'turkish_meaning': 'iş'},
        'Kuchen': {'turkish_meaning': 'kek'},
      'Stunde': {'turkish_meaning': 'saat'}
        },
        'das': {
        'Sofa': {'turkish_meaning': 'koltuk'},
        'Dunkel': {'turkish_meaning': 'karanlık'},
        'Regal': {'turkish_meaning': 'raf'},
        'Rot': {'turkish_meaning': 'kırmızı'},
        'Weiss': {'turkish_meaning': 'beyeaz'},
        'Buch': {'turkish_meaning': 'kitap'},
        'Haus': {'turkish_meaning': 'ev'},
        'Kind': {'turkish_meaning': 'çocuk'},
        'Auto': {'turkish_meaning': 'araba'},
        'Geld': {'turkish_meaning': 'para'},
        'Telefon': {'turkish_meaning': 'telefon'},
        'Fahrrad': {'turkish_meaning': 'bisiklet'},
        'Boot': {'turkish_meaning': 'tekne'},
        'Uhr': {'turkish_meaning': 'saat'},
        'Radio': {'turkish_meaning': 'radyo'},
        'Computer': {'turkish_meaning': 'bilgisayar'},
        'Hemd': {'turkish_meaning': 'gömlek'},
        'Mantel': {'turkish_meaning': 'palto'},
        'Kleid': {'turkish_meaning': 'elbise'},
        'Spiel': {'turkish_meaning': 'oyun'},
        'Bild': {'turkish_meaning': 'resim'},
        'Licht': {'turkish_meaning': 'ışık'},
        }
    }
     

    
def get_random_word():
    article = random.choice(list(words_data.keys()))
    german_word, word_data = random.choice(list(words_data[article].items()))
    turkish_meaning = word_data['turkish_meaning']
    return article, german_word, turkish_meaning

def practice_articles(request):
    if request.method == "POST":
        user_input = request.POST.get("article").strip().lower()
        correct_article = request.POST.get("correct_article")
        german_word = request.POST.get("german_word")
        turkish_meaning = request.POST.get("turkish_meaning")

        if user_input == correct_article:
            result = f"Correct! '{german_word}' means '{turkish_meaning}' in Turkish."
        else:
            result = f"Wrong! The correct article for '{german_word}' is '{correct_article}'. '{german_word}' means '{turkish_meaning}' in Turkish."

        article, german_word, turkish_meaning = get_random_word()
        return render(request, "articles.html", {
            "result": result,
            "german_word": german_word,
            "turkish_meaning": turkish_meaning,
            "correct_article": article
        })
    
    article, german_word, turkish_meaning = get_random_word()
    return render(request, "articles.html", {
        "german_word": german_word,
        "turkish_meaning": turkish_meaning,
        "correct_article": article
    })