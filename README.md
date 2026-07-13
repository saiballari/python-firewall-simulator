<div align="center">

# 🚀 TaskFlow

### A Modern Full Stack Task Management Application Built with the MERN Stack

TaskFlow is a secure, scalable, and responsive task management application designed to help users organize, prioritize, and track their daily work efficiently. Built using the MERN Stack, it demonstrates modern full-stack development practices including authentication, RESTful APIs, database integration, and cloud deployment.

[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://react.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-Express-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)](https://jwt.io/)
[![Vercel](https://img.shields.io/badge/Frontend-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com/)
[![Render](https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge&logo=render)](https://render.com/)

</div>

---

# 🌐 Live Application

### 🔗 Frontend

https://YOUR-VERCEL-URL.vercel.app

### 🔗 Backend API

https://taskflow-2-u9nr.onrender.com

> Experience the complete application with secure authentication, task management, analytics, search, filtering, and responsive design.

---

# 📖 Overview

TaskFlow provides a centralized platform where users can securely manage their daily tasks through a modern dashboard.

The application follows a complete MERN architecture with JWT-based authentication, REST APIs, MongoDB Atlas integration, and production deployment using Vercel and Render.

The project was developed to demonstrate production-ready full-stack development practices including secure authentication, CRUD operations, responsive UI, and cloud deployment.

---

# ✨ Key Features

### 🔐 Authentication

- Secure User Registration
- User Login
- JWT Authentication
- Protected Routes
- Password Hashing using bcrypt

### 📋 Task Management

- Create Tasks
- Update Tasks
- Delete Tasks
- View Personal Tasks
- Persistent Data Storage

### 🎯 Productivity

- Priority Management
  - 🔴 High
  - 🟡 Medium
  - 🟢 Low

- Due Date Support

- Pending & Completed Status

### 🔍 Search & Filtering

- Search by Title
- Search by Description
- Filter by Status
- Filter by Priority
- Automatic Due Date Sorting

### 📊 Dashboard Analytics

- Total Tasks
- Pending Tasks
- Completed Tasks
- Interactive Pie Chart
- Live Dashboard Statistics

### 🎨 User Interface

- Responsive Design
- Modern Dashboard
- Toast Notifications
- Mobile Friendly
- Clean User Experience

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Frontend | React.js, Vite, Axios, React Router DOM |
| Backend | Node.js, Express.js |
| Database | MongoDB Atlas |
| Authentication | JWT, bcryptjs |
| Charts | Recharts |
| Notifications | React Toastify |
| Deployment | Vercel, Render |
| Version Control | Git & GitHub |

---

# 🏗 System Architecture

```
                    React Frontend
                           │
                           │
                    Axios HTTP Requests
                           │
                           ▼
                 Express REST API Server
                           │
                 JWT Authentication
                           │
                           ▼
                    MongoDB Atlas
```

---

# 📂 Project Structure

```
TaskFlow
│
├── client
│   ├── src
│   │
│   ├── components
│   ├── pages
│   ├── services
│   ├── assets
│   └── main.jsx
│
├── server
│   ├── config
│   ├── controllers
│   ├── middleware
│   ├── models
│   ├── routes
│   ├── server.js
│   └── package.json
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/saiballari/taskflow.git
```

---

## Backend

```bash
cd server

npm install

npm start
```

---

## Frontend

```bash
cd client

npm install

npm run dev
```

---

# 🔑 Environment Variables

## Backend

```env
PORT=5000

MONGODB_URI=YOUR_MONGODB_URI

JWT_SECRET=YOUR_SECRET_KEY
```

---

## Frontend

```env
VITE_API_URL=https://taskflow-2-u9nr.onrender.com/api
```

---

# 📡 REST API

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/auth/register | Register User |
| POST | /api/auth/login | Login User |

---

## Tasks

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/tasks | Get All Tasks |
| POST | /api/tasks | Create Task |
| PUT | /api/tasks/:id | Update Task |
| DELETE | /api/tasks/:id | Delete Task |

---

# 🚀 Production Deployment

| Service | Platform |
|----------|----------|
| Frontend | Vercel |
| Backend | Render |
| Database | MongoDB Atlas |

---

# 🎯 Project Highlights

- Production-ready MERN Stack Application
- Secure JWT Authentication
- RESTful API Architecture
- MongoDB Atlas Integration
- Cloud Deployment
- Interactive Dashboard
- Task Analytics
- Search & Advanced Filtering
- Responsive User Interface
- Clean & Scalable Folder Structure

---

# 📚 What I Learned

Through this project, I strengthened my understanding of:

- Full Stack MERN Development
- REST API Design
- JWT Authentication
- MongoDB Atlas Integration
- Express Middleware
- React State Management
- Axios API Communication
- Cloud Deployment
- Git & GitHub Workflow
- Production Environment Configuration

---

# 🚀 Future Enhancements

- Calendar View
- Kanban Board
- Dark Mode
- Team Collaboration
- Email Notifications
- File Attachments
- AI Task Suggestions
- Activity History

---

# 👨‍💻 Developer

## Sai Ballari

**Full Stack Developer | Java Programmer | Cybersecurity Enthusiast**

### GitHub

https://github.com/saiballari

### Portfolio

https://portfoilo-website-green.vercel.app/

### LinkedIn

(Add your LinkedIn profile URL)

---

# ⭐ Support

If you found this project interesting or useful, consider giving this repository a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

<div align="center">

### Thank you for visiting the repository!

Built with ❤️ using the MERN Stack by **Sai Ballari**

</div>
