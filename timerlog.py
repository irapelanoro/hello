from flask import Flask, render_template
import time
from collections import Counter

app = Flask(__name__,template_folder = 'templatesTP')

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def count_with_dict(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def count_with_counter(text):
    words = text.split()
    return Counter(words)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/question1')
def question1():
    file_path = 't8.shakespeare.txt'
    text = read_file(file_path)
    count_dict = count_with_dict(text)
    return f"Count with Dictionary: {count_dict}"

@app.route('/question2')
def question2():
    file_path = 't8.shakespeare.txt'
    text = read_file(file_path)
    count_counter = count_with_counter(text)
    return f"Count with Counter: {count_counter}"

if __name__ == '__main__':
    app.run(debug=True)
