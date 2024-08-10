from flask import Flask, render_template, request, redirect, url_for, flash
import pywhatkit
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        message = request.form['message']
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])

        if mobile_number and message:
            try:
                # Send WhatsApp message using pywhatkit
                pywhatkit.sendwhatmsg(mobile_number, message, hour, minute)
                flash('Message successfully sent!', 'success')
            except Exception as e:
                flash(f'An unexpected error occurred: {e}', 'danger')
        else:
            flash('Please enter both a mobile number and a message.', 'warning')

        return redirect(url_for('send_message'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    