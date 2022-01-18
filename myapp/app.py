from flask import Flask, request
from jinja2 import render_template

app = Flask (__name__)

@app.route('/')
def index():
    return """<h1>Welcome to SLICK RICK Salon!</h1>
            <p>We are open everyday from 10AM to 5PM.</p>
            <p>Our services include:</p>
            <ul>
                <li>Haircut</li>
                <li>Shampoo</li>
                <li>Blowdry</li>
            </ul>
            <p><a href="/book">Click here to book an appointment.</a><p>
            """

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'GET':
        return render_template(book.html)
    else:
        name = request.form ['name']
        time = request.form ['time']

        return "<h1>Hello, {} you have booked an appointment at {}.</h1>".format(name, time)


if __name__ == "__main__":
    app.run(debug=True)