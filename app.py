from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from database import init_db, get_session, close_session
from models import Receipt, User

# Initialize the Flask app
app = Flask(__name__)

# Initialize database on first run
with app.app_context():
    init_db()

# Define the upload folder
upload_folder = 'uploads'
os.makedirs(upload_folder, exist_ok=True)
app.config['UPLOAD_FOLDER'] = upload_folder

#Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

# Define the allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    #Check if the file part exists in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    #Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # add Logic to process the file here (OCR,etc.)
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'file_path': file_path
            }), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Close database session after each request."""
    close_session()

if __name__ == '__main__':
    app.run(debug=True)