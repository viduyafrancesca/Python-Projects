from flask import Flask, request, render_template, redirect, url_for
import smtplib, openai
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ics import Calendar, Event
from datetime import datetime

app = Flask(__name__)
# Organizer details
ORGANIZER_NAME = '<ORGANIZER NAME>'

# Initialize OpenAI API key
openai.api_key = 'sk-'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        to = request.form['to']
        cc = request.form.get('cc', '')  # Default to empty string if not provided
        subject = request.form['subject']
        body = request.form['body']

        # Extract date and time using ChatGPT
        event_datetime, end_hour = extract_datetime_from_body(body)
        print(event_datetime, end_hour)
        if event_datetime:
            # Generate calendar invite
            calendar_attachment = generate_ics_event(subject, body, event_datetime, end_hour)
            # Send the email with calendar invite
            send_email(to, cc, subject, body, calendar_attachment)
            return redirect(url_for('success'))
        else:
            return "Could not extract date/time from the body."

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')
    
def extract_datetime_from_body(body):
    prompt = f"Extract the date and time from the following text:\n\n{body}\n\nPlease respond with the date-time in a format like '2024-08-16 09:00' and the end hour in an integer value with no newline."
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Parse the response
        output = response.choices[0].message.content
        
        # Assuming the response is structured with date-time and end hour, split it accordingly
        
        date_time_str = output[:-2].strip()
        end_hour = output[17:]
        
        # print(date_time_str, type(int(end_hour)), len(end_hour))
        event_datetime = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        return event_datetime, int(end_hour)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None

def generate_ics_event(subject, body, event_datetime, end_hour):
    # Extract date and time from email body
    event_datetime, end_hour = extract_datetime_from_body(body)

    if event_datetime:
        # Set event end time (using the extracted end hour)
        event_end_time = event_datetime.replace(hour=end_hour)
    else:
        # Default to current time plus 1 hour if no date is found
        event_datetime = datetime.now()
        event_end_time = event_datetime.replace(hour=(event_datetime.hour + 1))

    # Step 1: Create ICS Calendar Event
    c = Calendar()
    e = Event()
    e.name = subject
    e.description = body
    e.begin = event_datetime  # Set event start time based on the extracted date/time
    e.end = event_end_time  # Set event end time based on the extracted end hour
    e.organizer = ORGANIZER_NAME
    c.events.add(e)

    # Save the ICS file temporarily
    ics_filename = 'invite.ics'
    with open(ics_filename, 'w') as f:
        f.writelines(c)
    
    return ics_filename


def send_email(to, cc, subject, body, attachment):
    from_email = 'your.email@email.com'
    password = 'password'
    event_datetime, end_hour = extract_datetime_from_body(body)

    ics_filename = generate_ics_event(subject, body, event_datetime, end_hour)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Cc'] = cc
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach ICS file
    with open(ics_filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {ics_filename}',
        )
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, [to] + [cc], msg.as_string())
    except Exception as e:
        print(f'Error sending email: {e}')

if __name__ == '__main__':
    app.run(debug=True)