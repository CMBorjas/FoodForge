// Select elements
const fileInput = document.getElementById('file-input');
const uploadButton = document.getElementById('upload-button');
const statusDiv = document.getElementById('status');
const form = document.getElementById('upload-form');

// Handle form submission
form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    const file = fileInput.files[0];

    // Check if a file is selected
    if (!file) {
        statusDiv.textContent = 'Please select a file to upload.';
        statusDiv.style.color = 'red';
        return;
    }

    // Check if the file type is valid
    if (!['image/png', 'image/jpeg', 'application/pdf'].includes(file.type)) {
        statusDiv.textContent = 'Invalid file type. Please upload an image or PDF.';
        statusDiv.style.color = 'red';
        return;
    }

    // Create a FormData object to send the file
    const formData = new FormData();
    formData.append('file', file);

    // Display upload progress
    statusDiv.textContent = 'Uploading...';
    statusDiv.style.color = 'blue';

    try {
        // Send the file to the Flask server
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        // Parse the response from the server
        const result = await response.json();

        if (response.ok) {
            statusDiv.textContent = `Success! ${result.message}`;
            statusDiv.style.color = 'green';
        } else {
            statusDiv.textContent = `Error: ${result.error || 'Unknown error occurred.'}`;
            statusDiv.style.color = 'red';
        }
    } catch (error) {
        // Handle network or other errors
        statusDiv.textContent = 'An error occurred during upload.';
        statusDiv.style.color = 'red';
        console.error('Upload error:', error);
    }
});