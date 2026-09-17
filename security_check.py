from pathlib import Path
import sys

code = Path("app/app.py").read_text(encoding="utf-8")

if "debug=True" in code.replace(" ", ""):
    print("Falha SAST: Flask executado com debug=True.")
    sys.exit(1)

print("Relatorio SAST validado: debug=True nao encontrado.")
