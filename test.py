from flask import Flask,render_template ,  redirect, request, flash,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/refister')

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        pass
    return render_template("register.html")