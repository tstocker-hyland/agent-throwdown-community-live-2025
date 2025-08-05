# cin-agent-throwdown-community-live-2025
Agent Throwdown for Community Live 2025

# Google Colab

https://colab.research.google.com/github/tstocker-hyland/agent-throwdown-community-live-2025/blob/main/notebooks/rag_request.ipynb

# 📓 Jupyter Notebook with Virtual Environment

This project uses a Python virtual environment to manage dependencies and run Jupyter notebooks in a clean, reproducible way.

---

## ✅ Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

This will create a `.venv` folder in your project directory containing an isolated Python environment.

---

### 2. Activate the Virtual Environment

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

**On Windows:**

```bash
.venv\Scripts\activate
```

---

### 3. Install Jupyter and Kernel Support

Install Jupyter and the IPython kernel in the virtual environment:

```bash
pip install notebook ipykernel
```

---

### 4. Register the Virtual Environment as a Jupyter Kernel

```bash
python -m ipykernel install --user --name=venv --display-name "Python (.venv)"
```

This registers your environment so you can select it from within Jupyter notebooks.

---

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open your notebook and switch the kernel to **"Python (.venv)"** using the top-right dropdown menu.

---

## 🧠 Tips

- Always activate the virtual environment before launching Jupyter.

---

Happy Notebooks! 🚀