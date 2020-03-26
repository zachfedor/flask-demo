from flask import Flask, render_template, request, redirect, url_for

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='asdf',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        if (request.method == 'POST'):
            # form was sent
            name = request.form['user_name']

            if name == "":
                return render_template('homepage.html', error="Sorry, but you didn't enter a name")
            elif 'E' in name:
                # this is bad, you can't have an 'E' in your name dingus!
                return redirect(url_for('greet', name="Dingus"))
            else:
                return render_template('homepage.html', name=name)
        else:
            # first view of page
            return render_template('homepage.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/greet/<name>')
    def greet(name):
        return render_template('greet.html', person=name)

    return app

