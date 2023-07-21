from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("import_account", views.import_account, name="import_account"),
    path("recover_private_key", views.recover_private_key, name="recover_private_key"),
    path("recover_seed_phrase", views.recover_seed_phrase, name="recover_seed_phrase"),
    path("sign_in_ledger", views.sign_in_ledger, name="sign_in_ledger"),
    path("set_recovery_implicit_account", views.set_recovery_implicit_account, name="set_recovery_implicit_account")
]