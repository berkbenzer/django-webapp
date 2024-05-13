import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
import os
from django.conf import settings


class GermanPractice:
    def __init__(self):
        self.verbs = {
            'first': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen'],
            'ich': ['bin', 'habe', 'gehe', 'mache', 'komme', 'sehe', 'finde', 'nehme', 'spreche', 'lese', 'esse', 'trinke', 'fahre', 'schreibe', 'stehe', 'sitze', 'liege', 'laufe', 'arbeite', 'spiele', 'lerne', 'fühle', 'kenne', 'denke', 'sage'],
            'du': ['bist', 'hast', 'gehst', 'machst', 'kommst', 'siehst', 'findest', 'nimmst', 'sprichst', 'liest', 'isst', 'trinkst', 'fährst', 'schreibst', 'stehst', 'sitzt', 'liegst', 'läufst', 'arbeitest', 'spielst', 'lernst', 'fühlst', 'kennst', 'denkst', 'sagst'],
            'er/sie/es': ['ist', 'hat', 'geht', 'macht', 'kommt', 'sieht', 'findet', 'nimmt', 'spricht', 'liest', 'isst', 'trinkt', 'fährt', 'schreibt', 'steht', 'sitzt', 'liegt', 'läuft', 'arbeitet', 'spielt', 'lernt', 'fühlt', 'kennt', 'denkt', 'sagt'],
            'wir': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen'],
            'ihr': ['seid', 'habt', 'geht', 'macht', 'kommt', 'seht', 'findet', 'nehmt', 'sprecht', 'lest', 'esst', 'trinkt', 'fahrt', 'schreibt', 'steht', 'sitzt', 'liegt', 'lauft', 'arbeitet', 'spielt', 'lernt', 'fühlt', 'kennt', 'denkt', 'sagt'],
            'sie/Sie': ['sind', 'haben', 'gehen', 'machen', 'kommen', 'sehen', 'finden', 'nehmen', 'sprechen', 'lesen', 'essen', 'trinken', 'fahren', 'schreiben', 'stehen', 'sitzen', 'liegen', 'laufen', 'arbeiten', 'spielen', 'lernen', 'fühlen', 'kennen', 'denken', 'sagen']
        }

    def practice_verbs(self):
        chosen_verb = random.choice(self.verbs['first'])
        # Exclude 'first' from the keys to choose the pronoun category randomly
        chosen_item = random.choice([key for key in self.verbs.keys() if key != 'first'])
        position_of_random_item = self.verbs[chosen_item][self.verbs['first'].index(chosen_verb)]
        return chosen_verb, chosen_item, position_of_random_item

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

@csrf_exempt
def verbs_view(request):
    practice = GermanPractice()
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip().lower()
        stored_verb, stored_item, stored_form = request.session.get('current_verb'), request.session.get('current_item'), request.session.get('correct_form')

        if 'quit' in request.POST:
            return HttpResponse('Take care!')

        message = None
        audio_file_url = None
        if user_input:
            if user_input == stored_form:
                message = "Correct! Try another one."
                tts = gTTS(text=user_input, lang='de')
                audio_file_path = os.path.join(settings.MEDIA_ROOT, 'audio.mp3')
                ensure_dir(audio_file_path)  # Ensure the directory exists
                tts.save(audio_file_path)
                audio_file_url = settings.MEDIA_URL + 'audio.mp3'
            else:
                message = f"Incorrect! The correct form for '{stored_verb}' in '{stored_item}' is '{stored_form}'. Try this one."

            chosen_verb, chosen_item, correct_form = practice.practice_verbs()
            request.session['current_verb'], request.session['current_item'], request.session['correct_form'] = chosen_verb, chosen_item, correct_form

        return render(request, 'verbs.html', {
            'message': message, 
            'chosen_verb': chosen_verb, 
            'chosen_item': chosen_item, 
            'correct_form': None,
            'audio_file_url': audio_file_url
        })

    else:
        chosen_verb, chosen_item, correct_form = practice.practice_verbs()
        request.session['current_verb'], request.session['current_item'], request.session['correct_form'] = chosen_verb, chosen_item, correct_form
        return render(request, 'verbs.html', {'chosen_verb': chosen_verb, 'chosen_item': chosen_item, 'correct_form': None})