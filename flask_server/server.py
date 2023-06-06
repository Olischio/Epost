from flask import Flask, send_file, render_template
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)

@app.route('/somepicture.jpeg')
def serve_image():
    # Perform any desired function here
    # For example, print a message when the image is served
    print("Image served!")

    # Get the current timestamp
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # Open the file in append mode and write the content
    with open('myfile.txt', 'a') as file:
        file.write(f"{current_time} - Someone downloaded somepicture.png.\n")

    print("Ferdig med å skrive til fil!")

    #.jpeg er viktig at samsvarer med filnavnet
    # Return the image file to be served
    return send_file('image.jpeg', mimetype='image/png')

@app.route('/log')
def show_log():
    with open('myfile.txt', 'r') as file:
        log_content = file.read()
    return render_template('log.html', log_content=log_content)

@app.route('/send_email')
def send_email():
    # Email configuration
    sender_email = 'oliver.schiott@outlook.com'
    receiver_email = 'oliver.schiott@outlook.com'
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_username = 'oliver.schiott@outlook.com'
    smtp_password = os.environ.get('SMTP_PASSWORD')

    # Create a multi-part email message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'HTML Email Example'
    message['From'] = sender_email
    message['To'] = receiver_email

    # HTML content of the email
    html_content = '''
    <html>
    <body>
        <h1>Hello,</h1>
        <p>This is an example of sending an HTML email using Flask.</p>
        
        <p>This is the tracking image:</p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOuu3daYO60-FJuk8cTU1aSZCa9EvggUjzbQ&usqp=CAU">
        
    </body>
    </html>
    '''

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







