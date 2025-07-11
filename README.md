# 🛠️ Python Tools

A collection of simple and useful Python scripts — built for learning, experimenting, and automation. Each tool is beginner-friendly, well-documented, and runs from the terminal.

---

## 📦 Included Tools

### 1. 🔍 File Scanner & Hasher (`scanner.py`)
- Recursively scans directories for selected file extensions (`.exe`, `.bat`, etc.)
- Computes SHA-256 hashes to verify file integrity
- Simple command-line interface with real-time output

### 2. 📊 Authentication Log Analyzer (`authentication-log-analyzer.py`)
- Parses `auth.log` (Unix systems)
- Summarizes successful and failed login attempts
- Helpful for basic system monitoring and log inspection

### 3. 🌐 TCP Socket Server & Client (`tcp-socket-server-client.py`)
- Demonstrates basic client-server communication over sockets
- One script acts as the server, another as the client
- Great for learning Python’s `socket` module and networking fundamentals

### 4. 👀 File Watcher
- Watches a folder for changes (create, delete, modify)
- Prints alerts or logs changes in real time
- Ideal for monitoring or basic automation tasks

### 5. OpenCTI Artifacts
🔎 Python script that connects to OpenCTI's public demo API to fetch the 100 most recent malware-related file artifacts using GraphQL.
- Utilizes the OpenCTI GraphQL endpoint and parses results in JSON
- Extracts hash types, MIME types, and timestamps from artifact observables
- Built for cybersecurity automation and CTI enrichment
- Requires: `requests` (`pip install requests`)


---

## ▶️ Usage

Run any tool with:

```bash
python scanner.py
python authentication-log-analyzer.py
python tcp-socket-server-client.py
python file-watcher.py
