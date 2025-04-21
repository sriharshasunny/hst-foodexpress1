# Food Express Web Application

A modern food delivery web application with user authentication, order management, and payment processing.

## Features

- User authentication (login/signup)
- Profile management
- Order tracking
- Payment processing
- Modern UI with animations
- Responsive design

## Local Development Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python database.py
```

6. Run the application:
```bash
python app.py
```

7. Open your browser and visit:
```
http://localhost:5000
```

## Deployment to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variables:
     - `PYTHON_VERSION`: `3.9.0`
     - `FLASK_ENV`: `production`

4. Deploy the application

## Project Structure

```
├── app.py              # Flask application
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── Procfile           # Render deployment configuration
├── README.md          # Project documentation
└── templates/         # HTML templates
    ├── index1.html    # Main application page
    ├── login.html     # Login page
    ├── signup.html    # Signup page
    └── intro_1.html   # Introduction page
```

## Technologies Used

- Flask (Python web framework)
- SQLite (Database)
- HTML/CSS/JavaScript (Frontend)
- Bootstrap (UI framework)
- Gunicorn (Production server) 