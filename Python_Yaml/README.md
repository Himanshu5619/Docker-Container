# 🎓 Python YAML Use Case - Student Management System

## 📌 Overview
Welcome to the **Student Management System**, a simple yet powerful Python application that reads and processes student data from a YAML file. This script allows users to view and filter student records based on their GPA, making it an excellent example of handling structured data in Python.

## 🚀 Features
✅ Reads student data from a YAML file 📂
✅ Displays all students with their details 👨‍🎓👩‍🎓
✅ Filters students based on a minimum GPA 📊
✅ User-friendly terminal-based interaction 🖥️

## 🛠️ Prerequisites
Make sure you have the following installed before running the application:
- **Python** (>=3.6) 🐍
- **PyYAML** library 📜

## ⚙️ Installation
To install the required dependencies, open your terminal and run:
```sh
pip install pyyaml
```

## 📄 Creating the YAML File
Before running the application, create a file named **`students.yaml`** and structure it as follows:

```yaml
students:
  - name: Alice
    age: 21
    major: Computer Science
    gpa: 3.8
  - name: Bob
    age: 22
    major: Mathematics
    gpa: 3.5
  - name: Charlie
    age: 20
    major: Physics
    gpa: 3.9
  - name: David
    age: 23
    major: Chemistry
    gpa: 3.2
  - name: Eva
    age: 21
    major: Computer Science
    gpa: 3.7
```

## 🏗️ Running the Application
1️⃣ Ensure `students.yaml` and `app.py` are in the same directory.
2️⃣ Run the script using:
```sh
python app.py
```
3️⃣ Follow the on-screen instructions to filter students by GPA.

## 🖥️ Expected Output
Upon running the script, you should see output similar to:
```
All Students:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Bob, Age: 22, Major: Mathematics, GPA: 3.5
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9
Name: David, Age: 23, Major: Chemistry, GPA: 3.2
Name: Eva, Age: 21, Major: Computer Science, GPA: 3.7

Enter minimum GPA to filter students: 3.6
Students with GPA >= 3.6:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9
Name: Eva, Age: 21, Major: Computer Science, GPA: 3.7
```

## 🎯 Customization Options
🔹 Modify `students.yaml` to add or remove student details.
🔹 Extend `app.py` to include sorting features.
🔹 Implement CRUD operations to manage students dynamically.

## 📜 License
This project is **open-source** and can be modified or distributed freely.

---


