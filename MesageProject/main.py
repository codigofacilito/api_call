from flask import Flask

app = Flask(__name__)

@app.route('/notifications')
def notifications():
    for x in range(0, 100):
        print("Sending email to user...")
    return 'Emails sent'

if __name__ == '__main__':
    app.run(debug=True, port=8002)