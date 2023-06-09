from flask import Flask, request, send_file, render_template, url_for
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)

#nytt
@app.route('/')
def home():
    return render_template('index.html')

#Dette er en mega giga ultratest
@app.route('/send-email')
def form():
    return render_template('send-email.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    subject = request.form['subject']

    result = send_email(email, subject)

    return f'Email: {email}, Subject: {subject} {result}'

@app.route('/somepicture.jpeg')
def serve_image():

    # Perform any desired function here
    # For example, print a message when the image is served
    print("Image served!")

    # Her definerer jeg query argumenter fra linken
    email = request.args.get("email",'')
    subject = request.args.get("subject",'')

    # Get the current timestamp
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # Ny logg melding basert på input 
    # log_message = f"{current_time}|email={email}|subject={subject}\n"

    # Open the file in append mode and write the content
    with open('myfile.txt', 'a') as file:
        # file.write(f"{current_time} - Someone downloaded somepicture..\n")
        file.write(f"{current_time}|{email}|{subject} \n")

    print("Ferdig med å skrive til fil!")

    # Return the image file to be served
    return send_file('image.jpeg', mimetype='image/jpeg')

@app.route('/log')
def show_log():
    # log_entries = []
    with open('myfile.txt', 'r') as file:
        log_content = file.readlines()
        # for line in lines:
        #     log_entries.append(line.strip().split('|')) 
    return render_template('log.html', log_content=log_content)
        
    #     # readlines
    #     log_content = file.read()
    # return render_template('log.html', log_content=log_content)


def send_email(receiver_email, subject):
    # Email configuration
    sender_email = 'oliver.schiott@outlook.com'
    # receiver_email = 'oliver.schiott@outlook.com'
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_username = 'oliver.schiott@outlook.com'
    smtp_password = os.environ.get('SMTP_PASSWORD')

    # Create a multi-part email message
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    image_url = url_for('serve_image', _external=True)

    # image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOuu3daYO60-FJuk8cTU1aSZCa9EvggUjzbQ&usqp=CAU"

    # HTML content of the email
    html_content = '''
    <html>
    <body>
        <h1>Hello,</h1>
        <p>This is an example of sending an HTML email using Flask.</p>
        
        <p>This is the tracking image:</p>
        <img src="{0}">
        <p>This email includes tracking technology to gather statistical data on delivery and open rates. By opening this email, you consent to the collection and analysis of your interaction with the message. We use this information to enhance our communication and provide you with tailored content.

        If you wish to opt out of tracking, you can unsubscribe here. Disabling the loading of external images in your email client settings will also prevent tracking.</p>
    </body>
    </html>
    '''

    html_content=html_content.format(image_url)

    # Attach HTML content to the email message
    message.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'
    

if __name__ == '__main__':
    app.run()

