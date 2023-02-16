import os
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from reportlab.pdfgen import canvas

# Watcher class to monitor the folder for changes
class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the created file is a JSON file
        if event.is_directory:
            return None
        elif event.event_type == 'created' and event.src_path.endswith('.json'):
            # Convert the JSON file to PDF
            json_file = open(event.src_path, 'r')
            data = json.load(json_file)
            pdf_file = os.path.splitext(event.src_path)[0] + '.pdf'
            c = canvas.Canvas(pdf_file)
            c.drawString(100, 750, data['name'])
            c.drawString(100, 700, data['email'])
            c.save()
            json_file.close()

            # Send the PDF file by email
            sender_email = 'sender@example.com'
            sender_password = 'password'
            recipient_email = 'recipient@example.com'
            subject = 'Converted JSON file'
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            with open(pdf_file, 'rb') as f:
                attach = MIMEApplication(f.read(),_subtype = 'pdf')
                attach.add_header('Content-Disposition','attachment',filename=str(pdf_file))
                message.attach(attach)
            msg = message.as_string()
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg)
            server.quit()
            print('Email sent')

if __name__ == "__main__":
    folder_path = '.'
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
