"""Создание HTML-документации для учебного калькулятора."""

from pathlib import Path


HTML = """<!doctype html>
<html lang="ru">
<head><meta charset="utf-8"><title>Документация калькулятора</title></head>
<body>
  <h1>Учебный калькулятор</h1>
  <p>Модуль <code>calculator.py</code> содержит операции:</p>
  <ul>
    <li><code>add(a, b)</code> — сложение;</li>
    <li><code>subtract(a, b)</code> — вычитание;</li>
    <li><code>multiply(a, b)</code> — умножение;</li>
    <li><code>divide(a, b)</code> — деление;</li>
    <li><code>power(a, b)</code> — возведение в степень.</li>
  </ul>
</body>
</html>
"""


Path("docs").mkdir(exist_ok=True)
Path("docs/calculator.html").write_text(HTML, encoding="utf-8")
print("HTML-документация создана: docs/calculator.html")
