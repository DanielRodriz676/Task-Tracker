# 🧠 Backend Project — Task Tracker CLI

Project based on roadmap.sh:
🔗 **Task Tracker**
[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

---

## ⚙️ Requirements

To run this project, you need **Python 3.13** or you can use **uv**.

* Option 1: Install Python 3.13 normally
* Option 2 (recommended): Use **uv** to manage the virtual environment and dependencies

> ⚠️ Make sure Python has access to the standard libraries.

---

## 📦 Local Installation with `uv`

### 1️⃣ Inside the project directory

```bash
uv venv
```

---

### 2️⃣ Activate the virtual environment

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

---

### 3️⃣ Install the project in editable mode

```bash
uv pip install -e .
```

This allows code changes to be reflected immediately in the CLI.

---

## 🖥️ CLI Usage

### ➕ Add a task

```bash
todo add "task"
```

---

### ✏️ Update a task

```bash
todo update 1 "task update"
```

---

### 📋 List all tasks

```bash
todo list-task
```

---

### ❌ Remove a task

```bash
todo remove 1
```

---

### 🔄 Update task status

```bash
todo mark 1 "progress"
todo mark 1 "done"
```

---

### 📂 Filter tasks by status

#### ✅ Completed tasks

```bash
todo list-done
```

#### ❌ Not completed tasks

```bash
todo list-not-done
```

#### 🔄 Tasks in progress

```bash
todo list-progress
```
