from flask import Flask, request, render_template, redirect, url_for
import smtplib, re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ics import Calendar, Event
from ics.grammar.parse import ContentLine  # Import to handle custom ICS lines like organizer
from datetime import datetime, timedelta
# import re

app = Flask(__name__)

# Organizer details
ORGANIZER_EMAIL = 'slackycode@gmail.com'  # Organizer email
ORGANIZER_NAME = 'Chesca Viduya'         # Organizer name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        to = request.form['to']
        cc = request.form.get('cc', '')  # Default to empty string if not provided
        subject = request.form['subject']
        body = request.form['body']

        # Generate calendar invite
        # extract_datetime_from_body = 
        calendar_attachment = generate_ics_event(subject, body)

        # Send the email with calendar invite
        send_email(to, cc, subject, body, calendar_attachment)

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

def extract_datetime_from_body(body):
    # Regular expression to detect date and time in the format: "Aug 16, 2024 9-10am"
    date_time_pattern = r'((?:[A-Za-z]{3})|(?:January|February|March|April|May|June|July|August|September|October|November|December)) (\d{1,2})(?:, (\d{4}))? (\d{1,2})-(\d{1,2})(am|pm)'
    
    match = re.search(date_time_pattern, body)
    if match:
        # Extract matched groups (Month, Day, Year, Start Hour, End Hour, AM/PM)
        month_str = match.group(1)
        day = match.group(2)
        year = match.group(3)
        start_hour = match.group(4)
        end_hour = match.group(5)
        am_pm = match.group(6)
        if year is None:
            year = datetime.now().year
            event_datetime_str = f"{month_str} {day}, {year} {start_hour}{am_pm}"
        else:
            # Convert the extracted values to a proper datetime format
            event_datetime_str = f"{month_str} {day}, {year} {start_hour}{am_pm}"

        event_datetime = datetime.strptime(event_datetime_str, '%B %d, %Y %I%p') if len(month_str) > 3 else datetime.strptime(event_datetime_str, '%b %d, %Y %I%p')
        
        return event_datetime, int(end_hour)
    else:
        return None, None

def generate_ics_event(subject, body):
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
    from_email = 'your.email@gmail.com'
    password = 'your_app_password'
    ics_filename = generate_ics_event(subject, body)

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


