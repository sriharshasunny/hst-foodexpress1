from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from database import create_user, verify_user, get_user_by_id, update_user_profile
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def intro():
    return render_template('intro_1.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect(url_for('index1'))
    return render_template('login.html')

@app.route('/signup')
def signup():
    if 'user_id' in session:
        return redirect(url_for('index1'))
    return render_template('signup.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    user_id = verify_user(username, password)
    if user_id:
        session['user_id'] = user_id
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('fullName')
    phone = data.get('phone')
    address = data.get('address')
    
    if not all([username, email, password]):
        return jsonify({'error': 'Required fields are missing'}), 400
    
    if create_user(username, email, password, full_name, phone, address):
        return jsonify({'message': 'Account created successfully'}), 201
    else:
        return jsonify({'error': 'Username or email already exists'}), 400

@app.route('/api/profile', methods=['GET'])
def get_profile():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user = get_user_by_id(session['user_id'])
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/profile', methods=['PUT'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    full_name = data.get('fullName')
    phone = data.get('phone')
    address = data.get('address')
    
    if update_user_profile(session['user_id'], full_name, phone, address):
        return jsonify({'message': 'Profile updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update profile'}), 400

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/index1')
def index1():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True) 