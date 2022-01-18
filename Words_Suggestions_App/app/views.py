from flask import Flask, render_template, url_for, request, flash
from app import app
from .find_similar_words import extract_synonym

app.secret_key = "secret key"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        word = request.form.get("title")
        similar_words = extract_synonym(word)
        print(word)
        
        print(similar_words)
        
        return render_template("index.html", similar_words = similar_words)
    
    else:
        flash('Please enter the word..')
        return render_template('index.html')