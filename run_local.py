import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
PYTHON = VENV / "Scripts" / "python.exe"


def run(cmd, cwd=ROOT):
    print(f"\n> {' '.join(cmd)}")
    return subprocess.Popen(cmd, cwd=str(cwd), shell=True)


def ensure_venv():
    if not PYTHON.exists():
        print("Virtual environment not found. Create one first: python -m venv .venv")
        raise SystemExit(1)


def install_deps():
    print("Installing project dependencies...")
    subprocess.run(
        [str(PYTHON), "-m", "pip", "install", "-r", "requirements.txt"],
        check=False,
    )


def start_backend():
    return run(f'"{PYTHON}" -m uvicorn backend:app --host 127.0.0.1 --port 8001')


def start_frontend():
    return run(f'"{VENV / "Scripts" / "streamlit.exe"}" run app.py --server.address 127.0.0.1 --server.port 8502')


if __name__ == "__main__":
    ensure_venv()
    install_deps()
    backend = start_backend()
    time.sleep(3)
    frontend = start_frontend()
    print("\nThermoMind is starting...")
    print("Backend: http://127.0.0.1:8001")
    print("Frontend: http://127.0.0.1:8502")
    print("\nPress Ctrl+C in this terminal to stop both services.")
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\nShutting down ThermoMind services...")
        backend.terminate()
        frontend.terminate()
        backend.wait()
        frontend.wait()
