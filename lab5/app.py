from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Fake in-memory user "database"
USERS = {
    "ola": {
        "name": "Ola",
        "age": 25,
        "bio": "Uwielbia Pythona i kolorowanki dla dorosłych."
    },
    "toffi": {
        "name": "Toffi",
        "age": 8,
        "bio": "Kochający spacery włochaty rudzielec."
    },
    "gaja": {
        "name": "Gaja",
        "age": 0.5,
        "bio": "Mały demon, żarłok i poszukiwacz przygód."
    },
    "ninja": {
        "name": "Ninja",
        "age": 16,
        "bio": "Koci senior, dostojny i niezależny."
    }
}

# --- Static routes ----------------------------------------------------------


@app.route("/")
def home():
    """Static route: portal home page"""
    page = '''
    <!doctype html>
    <title>MiniPortal</title>
    <p>Witaj<a href="/profiles">Zobacz profile</a></p>
    '''
    return page


@app.route("/about")
def about():
    """Static route: about page"""
    page = '''
    <!doctype html>
    <title>O projekcie</title>
    <h1>O projekcie</h1>
    <p>Ta aplikacja demonstruje podstawy <code>Flask</code>:
       routing statyczny i dynamiczny, szablony Jinja i obsługę błędów.</p>
    '''
    return page


# --- Dynamic routes ---------------------------------------------------------


@app.route("/profiles")
def list_profiles():
    """Static URL, dynamic content: list of users"""
    template = '''
    <!doctype html>
    <title>Profile</title>
    <h1>Profile użytkowników</h1>
    <ul>
      {% for username, user in users.items() %}
        <li><a href="{{ url_for('show_profile', username=username) }}">{{ user.name }}</a></li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('home') }}">⟵ powrót</a></p>
    '''
    return render_template_string(template, users=USERS)


@app.route("/profiles/<username>")
def show_profile(username):
    """Dynamic route: single user profile"""
    user = USERS.get(username)
    if user is None:
        abort(404)
    template = '''
    <!doctype html>
    <title>Profil {{ user.name }}</title>
    <h1>Profil: {{ user.name }}</h1>
    <ul>
      <li>Wiek: {{ user.age }} lat</li>
      <li>Opis: {{ user.bio }}</li>
    </ul>
    <p><a href="{{ url_for('list_profiles') }}">⟵ wszystkie profile</a></p>
    '''
    return render_template_string(template, user=user)


# --- Error handlers ---------------------------------------------------------


@app.errorhandler(404)
def not_found(error):
    return "<h1>404 –Nie znaleziono</h1>", 404


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # debug=True = szybkie prototypowanie (auto reload, traceback w przeglądarce)
    app.run(debug=True)
