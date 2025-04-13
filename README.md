# FARM Full-Stack Web App

Welcome to the **FARM Full-Stack Web App** repository! This project is a web application built with a full-stack approach using FastAPI, React and MongoDB, along with Tailwind for front-end styling. 

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## About

The FARM Full-Stack Web App is designed as a robust and scalable full-stack web application. It combines a FastAPI-based backend with a React-powered frontend to deliver seamless functionality and user experience.

## Features

- **Backend**: RESTful API powered by FastAPI to handle business logic and data management.
- **Frontend**: Interactive and dynamic user interface built with ReactJS.

## Technologies Used

- **Backend**: FastAPI and MongoDB
- **Frontend**: React, Tailwind and Vite

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

Ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (Version 3.11.x or later)
- [Node.js](https://nodejs.org/) (Version 20.19.x or later)
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FreddyPinto/FARM-full-stack-web-app.git
   cd FARM-full-stack-web-app
   ```

2. Set up the Python backend:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the JavaScript frontend:

   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. Start the backend server:

   ```bash
   cd backend
   fastapi dev app/main.py
   ```

2. Start the frontend development server:

   ```bash
   cd ../frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173` to access the application.

## Contributing

We welcome contributions to improve this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).
