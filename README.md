# Food Forge

Food Forge is a Flask-based web application designed to process uploaded images and PDF files to extract recipes and catalog them. This project is in its early stages of development.

---

## Folder Structure

```
FoodForge/
├── uploads/                # Directory for storing uploaded files (auto-created)
├── templates/
│   └── index.html         # Frontend HTML file
├── static/
│   ├── style.css          # CSS file for styling (if applicable)
│   └── index.js           # JavaScript file for interactivity (if applicable)
├── app.py                 # Flask backend file
└── README.md              # Project documentation
```

---

## How to Run the Program

### Prerequisites

1. Python 3.7 or higher installed on your system.
2. `pip` package manager installed.

### Steps to Set Up and Run

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd FoodForge
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv foodforge
   source foodforge/bin/activate   # On Windows: foodforge\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install flask
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open your web browser and navigate to: [http://localhost:5000](http://localhost:5000)

---

## Features

- Upload images (`.png`, `.jpg`, `.jpeg`) or PDF files (`.pdf`).
- Basic Flask backend to handle file uploads.
- Simple frontend for file selection and submission.

---

## Future Enhancements

- Add OCR functionality to extract text from images and PDFs.
- Improve frontend UI and design.
- Store and catalog extracted recipes in a database.
- Implement user authentication and sharing features.

---

## Issues and Contributions

Feel free to submit issues or contribute to the project by opening a pull request.
