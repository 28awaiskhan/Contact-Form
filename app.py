from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # ✅ Ye sabhi origins ke liye CORS allow karega

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data received'}), 400

        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        number = data.get('number', '')

        sender_email = 'asjd8037@gmail.com'
        receiver_email = 'asjd8037@gmail.com'
        password = 'clhh tnof krsp azfz'

        msg = MIMEText(f'Name: {name}\nEmail: {email}\nMessage: {message}\nNumber: {number}')
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        print(f"Sending email to {receiver_email} from {sender_email}")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        return jsonify({'message': 'Thank you! Your message has been sent.'}), 200
    except Exception as e:
        return jsonify({'message': 'Error sending email', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
