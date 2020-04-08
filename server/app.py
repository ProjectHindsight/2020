from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from env_vars import firebase_service_account_path

# Use a service account
cred = credentials.Certificate(firebase_service_account_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# =================
# Route for Questions
# =================
@app.route('/questions', methods=['GET'])
def all_questions():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        question_list = []
        question_stream = db.collection(u'questions').stream()
        for question in question_stream:
            question_dict = question.to_dict()
            temp_question = {}
            temp_question['id'] = question.id
            temp_question['category'] = question_dict['category']
            temp_question['question'] = question_dict['question']
            temp_question['type'] = question_dict['type']

            question_list.append(temp_question)
        response_object['questions'] = question_list
    return jsonify(response_object)

# =================
# Route for User Entries
# =================
@app.route('/user_entry', methods=['POST'])
def add_user_entry():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        entry_dict = {
            'answer': post_data.get('answer'),
            'questionId': post_data.get('questionId'),
            'sentOn': post_data.get('sentOn'),
            'submittedOn': post_data.get('submittedOn'),
            'userId': post_data.get('userId')
        }
        db.collection(u'user_entry').add(entry_dict)
        response_object['message'] = 'Entry added!'
    return jsonify(response_object)

# =================
# Route for Books
# =================
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        book_dict = {
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        }
        db.collection(u'books').add(book_dict)
        response_object['message'] = 'Book added!'
    else:
        book_list = []
        book_stream = db.collection(u'books').stream()
        for book in book_stream:
            book_dict = book.to_dict()
            temp_book = {}
            temp_book['id'] = book.id
            temp_book['title'] = book_dict['title']
            temp_book['author'] = book_dict['author']
            temp_book['read'] = book_dict['read']

            book_list.append(temp_book)
        response_object['books'] = book_list
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        book_dict = {
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        }
        db.collection(u'books').document(book_id).set(book_dict)
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        db.collection(u'books').document(book_id).delete()
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()