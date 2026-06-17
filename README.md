# Personal Kernel-Level Packet Interception Firewall

A custom Windows network layer security application built in Python that utilizes the Windows Filtering Platform (WFP) driver interface to capture, evaluate, and selectively drop outbound traffic.

## 🛠️ Core Technologies
* **Language:** Python (v3.14)
* **API/Driver Engine:** WinDivert User-Space Interception Architecture
* **Development Environment:** Visual Studio Code (Administrative Mode)

## 🚀 Key Features & Implementation
* **Low-Level Interception:** Monitors raw outbound IPv4, TCP, and UDP transport streams directly from the operating system network stack.
* **Threat Mitigation Rule Engine:** Implements dictionary-based rules to evaluate destination parameters against custom IP and Port threat list criteria.
* **Asynchronous Packet Drop Mechanism:** Successfully isolates and drops malicious traffic streams (e.g., testing via explicit mitigation of `8.8.8.8`) before it can clear the hardware layer.

## 📦 Run & Deployment Requirements
1. Place `WinDivert.dll` and `WinDivert64.sys` binaries into the local project directory.
2. Open your terminal workspace as an **Administrator**.
3. Initialize the firewall thread by executing:
   ```cmd
   python firewall.py
   ```
