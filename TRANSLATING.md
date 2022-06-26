Tlumaczenie strony
==================

- Inslatacja *gettext* - https://www.gnu.org/software/gettext/
- W głównym katalogu i każdym podkatalogu (np. delta, core, polls) tworzymy katalog "locale"
- `python manage.py makemessages -l pl`
- W szablonach:
  - Dodajemy `{% load i18n %}` na samej górze (ale po `extends`)
    - Bez tego będziemy dostawać błędy np. "Invalid block tag on line 7: 'translate', expected 'endblock'. Did you forget to register or load this tag?"
  - Używamy np. `{% translate "Welcome on Polls page" %}`
- W modelach i widokach:
  - ...
- Uzupełniamy pliki `django.po`
- `python manage.py compilemessages`
  - Powstanie plik `django.mo
- W `settings.py`, w `MIDDLEWARE`, po `SessionMiddleware` dodajemy:
  `'django.middleware.locale.LocaleMiddleware',`