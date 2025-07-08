# 🐳 Flask Docker App

This is a simple Python Flask application containerized using Docker. It returns a "Hello from Flask in Docker!" message when accessed through the browser or an API client.

---

## 📁 Project Structure

```

flask-docker-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── Dockerfile          # Docker image instructions

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-docker-app.git
cd flask-docker-app
````

### 2. Build the Docker Image

```bash
docker build -t flask-docker-app .
```

### 3. Run the Docker Container

```bash
docker run -d -p 5000:5000 flask-docker-app
```

Now open your browser and go to:
👉 [http://localhost:5000](http://localhost:5000)

You should see:

```
Hello from Flask in Docker!
```

---

## 🧠 CI/CD Concept Overview

This project can be used as a base for building a CI/CD pipeline.

### CI (Continuous Integration)

* Run tests (if any)
* Lint Python code
* Build Docker image on every push

### CD (Continuous Deployment)

* Push Docker image to Docker Hub or GitHub Container Registry
* Deploy container to a cloud server or Kubernetes

---

## 🐍 Tech Stack

* Python 3.9 (slim image)
* Flask
* Docker

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Author

Made with ❤️ by [Your Name](https://github.com/yourusername)

