from flask import Flask, request, url_for, redirect, render_template

app = Flask (__name__)

# HOME
@app.route('/')
def index():
    return render_template("home.html")

# BOOKING PAGE
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        return redirect(url_for('confirmation'))
    else:
        return render_template("booking.html")

#CONFIRMATION PAGE
@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

#RUN
if __name__ == "__main__":
    app.run(debug=True)