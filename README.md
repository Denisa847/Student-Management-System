# 🎓 Student Management System

A Python console application for managing **students, disciplines, and grades**, featuring **data persistence, statistical reports, and undo/redo functionality**.

The project was developed during my first year of studying Computer Science while learning Python. Its goal was to practice fundamental software development concepts such as **object-oriented design, layered architecture, repository abstraction, data persistence**, and implementing **undo/redo functionality using the Command pattern**.

---

# ✨ Features

## 👨‍🎓 Student Management
- Add a student
- Remove a student
- Update student information
- Search students by **ID or name**
- Automatically remove associated grades when a student is deleted

---

## 📚 Discipline Management
- Add disciplines
- Remove disciplines
- Update discipline information
- Search disciplines by **ID or name**
- Automatically remove grades when a discipline is deleted

---

## 📝 Grade Management
- Assign grades to students
- View all grades
- Remove grades by student
- Remove grades by discipline

---

## 📊 Statistics
The system provides several academic reports:

- Students **failing at least one discipline**
- Students ranked by **best academic situation**
- Disciplines ranked by **average grade**

---

## ↩️ Undo / Redo Support

The application supports **undo and redo operations** using the **Command Pattern**.

Supported undo/redo operations:

- Add student
- Remove student
- Update student
- Add discipline
- Remove discipline
- Update discipline
- Add grade

---

# 🏗 Architecture

The project follows a **layered architecture**:
