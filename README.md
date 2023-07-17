# File Upload and Download App using FastAPI and React

This repository contains a simple web application built using FastAPI and React for uploading and downloading files to/from a MongoDB database using GridFS. The application allows users to upload files, view the list of uploaded files, and download files from the cloud storage.

# Features

 - Upload files to the cloud storage (MongoDB GridFS) using FastAPI.
 - View the list of uploaded files.
 - Download files from the cloud storage.

# Technologies Used

 - FastAPI: A modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints.
 - React: A JavaScript library for building user interfaces.
 - MongoDB: A NoSQL database used for storing uploaded files.
 - GridFS: A specification within MongoDB for storing and retrieving large files, such as images, videos, and audio.

# Backend Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Install Python dependencies:
   ```bash
   cd your-repo-name
   pip install -r requirements.txt

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

The FastAPI server will start running at http://localhost:8000.

# Frontend Setup

1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install

2. Run the React development server:
   ```bash
   npm start

The React development server will start running at http://localhost:3000.

# Usage

1. Open your browser and go to http://localhost:3000.
2. Upload a file by clicking the "Choose File" button and selecting a file from your local machine. Then click the "Subir Archivo" button to upload the selected file to the cloud storage.
3. Once the file is uploaded, it will appear in the list of files. You can click on the file name to download the file from the cloud storage.

# CORS Configuration

The backend server is configured to allow requests from the following origin:
 - http://localhost:5173
   
Please update the origins list in the main.py file if you want to allow requests from other origins:
 - Example:
   ```python
   origins = [
       "http://localhost:5173",  # Add more origins here if needed
   ]

# Note
 - This application is a basic example of how to upload and download files using FastAPI and React. In a real-world application, you may need to implement authentication and authorization mechanisms to secure the file uploads and downloads.

 - Make sure you have MongoDB installed and running locally on the default port 27017 before starting the FastAPI server.

 - The MongoDB connection URL is set to 'mongodb://localhost:27017' in the main.py file. Modify this URL if your MongoDB server is running on a different host or port.

 - The React frontend uses the Sonner library for displaying toasts. You can customize the toast messages by updating the frontend code in frontend/src/App.js and frontend/src/components/ListFiles.js.

