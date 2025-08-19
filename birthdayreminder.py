import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage

GMAIL_USER = 'your_email@gmail.com'
GMAIL_PASS = 'your_password'

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = GMAIL_USER
    msg['To'] = recipient
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(GMAIL_USER, GMAIL_PASS)
        smtp.send_message(msg)
    print(f"Email sent to {recipient}")

def send_birthday_wishes(filepath):
    df = pd.read_excel(filepath)
    today_str = datetime.now().strftime('%m-%d')
    current_year = datetime.now().year
    updated = False

    for i, row in df.iterrows():
        bday_str = row['Birthday'].strftime('%m-%d')
        last_sent = str(row.get('Last Sent', ''))
        if bday_str == today_str and str(current_year) not in last_sent:
            body = f"Happy Birthday, {row['Name']}!"
            send_email(row['Email'], "Happy Birthday!", body)
            df.at[i, 'Last Sent'] = current_year
            updated = True

    if updated:
        df.to_excel(filepath, index=False)
        print("Updated Last Sent dates.")

if __name__ == "__main__":
    path = input("Enter the Excel file path: ")
    send_birthday_wishes(path)
