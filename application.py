import os
from flask import Flask, render_template, request, flash, redirect, url_for
import stripe

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']


app = Flask(__name__)
app.secret_key = 'ZLO\x8c#5\x9eb\xc2\x88B(\x84R\xc6(e2c\x17"\x8co\xa2'


@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    amount = 500
 
    customer = stripe.Customer.create(
        email='',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Paying Bill'
    )

    #return render_template('charge.html', amount=amount)
    flash('Thanks for the payment, you are a champ')
    return redirect(url_for('index'))
    return render_template('index.html', amount=amount)

if __name__ == "__main__":
    app.run(debug=True)
