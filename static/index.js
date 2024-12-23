// Select elements
const fileInput = document.getElementById('file-input');
const uploadButton = document.getElementById('upload-button');
const statusDiv = document.getElementById('status');

// Handle form submission
document.getElementById('upload-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const file = fileInput.files[0];
    if (!file) {
        statusDiv.textContent = 'Please select a file to upload.';
        statusDiv.style.color = 'red';
        return;
    }

    if (!['image/png', 'image/jpeg', 'application/pdf'].includes(file.type)) {
        statusDiv.textContent = 'Invalid file type. Please upload an image or PDF.';
        statusDiv.style.color = 'red';
        return;
    }

    statusDiv.textContent = 'Uploading...';
    statusDiv.style.color = 'blue';

    // Simulate an upload for demo purposes
    setTimeout(() => {
        statusDiv.textContent = 'File uploaded successfully!';
        statusDiv.style.color = 'green';
    }, 2000);
});
