# 🚀 Port Scanner

<p align="center">
Fast multithreaded TCP port scanner with interactive IP input
</p>

---

## ⚡ Features

- 🚀 Multithreaded scanning (fast)
- 🌍 Interactive IP input
- 🔍 Scan all ports (0–65535)
- 📊 Progress bar
- 💾 Saves open ports
- 📦 EXE version available

---

## 📥 Download

👉 Go to **Releases** and download:
```
port-scanner.exe
```

---

## ▶️ Usage

```bash
python code.py
```

---

## 📦 Build EXE

```bash
pyinstaller --onefile --add-data "all_ports_0-65535.txt;." code.py
```

---

## 📁 Output

- open_ports.txt → open ports list

---

## ⚙️ Requirements

```bash
pip install colorama tqdm
```

---

## 📜 License

MIT License
