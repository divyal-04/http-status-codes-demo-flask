# HTTP Status Codes Demo Server (Flask)

A simple Flask-based server to **demonstrate all major HTTP status code families** (2xx, 3xx, 4xx, 5xx) for learning, testing, and API experimentation.  
Perfect for beginners, students, and anyone looking to understand **how APIs respond in real-world scenarios**.

---

## 🔹 Features

- **2xx Success:** `200 OK`, `201 Created`, `204 No Content`  
- **3xx Redirection:** `301 Moved Permanently`  
- **4xx Client Errors:** `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `405 Method Not Allowed`, `408 Request Timeout`, `429 Too Many Requests`  
- **5xx Server Errors:** `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`  

> Each endpoint demonstrates realistic scenarios using query parameters, headers, request bodies, and client behaviors.

---

## 🔹 Demo Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/user` | GET | Get user info (404 if not found) |
| `/user` | POST | Create a user (201 Created) |
| `/user` | DELETE | Delete a user (204 No Content) |
| `/redirect-old` | GET | Redirect to `/redirect-new` (301) |
| `/bad-request` | POST | Send JSON body, else 400 |
| `/protected` | GET | Requires header `Authorization: demo_token` |
| `/forbidden` | GET | Access based on user role |
| `/only-post` | POST | Only POST allowed, else 405 |
| `/timeout` | GET | Simulate slow server (client-side 408) |
| `/rate-limit` | GET | Limits requests, 429 if exceeded |
| `/server-error` | GET | Simulates 500 Internal Server Error |

---

## 🔹 Setup & Run Demo Server

Follow these steps to run the HTTP Status Codes Demo Server locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/divyal-04/http-status-codes-demo-flask.git
cd http-status-codes-demo-flask

# 2️⃣ Create a virtual environment
# Windows
python -m venv venv
# Linux / Mac
python3 -m venv venv

# 3️⃣ Activate the virtual environment
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Run the server
python run.py

# ✅ Server will start at http://localhost:5000/
# You can now test endpoints using Postman, Thunder Client, or a browser.

