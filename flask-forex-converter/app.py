from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from helper import valid_curr_code, valid_amount, convert_currency, get_target_currency_symbol

app = Flask(__name__)
app.config['SECRET_KEY'] = "shh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.get('/')
def index():
    """Show currency converter on homepage"""

    return render_template('index.html')


@app.post('/results')
def results():
    """Convert currency"""

    conv_from = request.form["conv-from"].upper()
    conv_to = request.form["conv-to"].upper()
    starting_amount = request.form["amount"]

    # Check validity of all form fields
    error = False
    if not valid_curr_code(conv_from):
        error = True
        flash(f"Starting currency not valid: {conv_from}")

    if not valid_curr_code(conv_to):
        error = True
        flash(f"Target currency not valid: {conv_to}")

    if not valid_amount(starting_amount):
        error = True
        flash("Not a valid amount.")

    # Return home with error message(s) if found
    if error:
        return redirect('/')
    # Otherwise, convert currency and show results on results page
    else:
        converted_amount = convert_currency(
            conv_from,
            conv_to,
            starting_amount
        )
        symbol = get_target_currency_symbol(conv_to)

        return render_template(
            'results.html',
            converted_amount=converted_amount,
            symbol=symbol
        )
