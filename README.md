# GitHub Link QR Generator (Python)

This project contains simple Python scripts to generate QR codes for GitHub repository links.
Each QR code redirects to a GitHub repo when scanned.

The project is designed to help students easily create QR codes for events, LinkedIn posts, and project showcases.

---

## Files in This Project

### 1. `basic_qr_generator.py`
**Use this file for learning and quick usage**

- Generates QR codes in a loop
- File numbering starts from `0` every time the program is run
- Best for understanding:
  - `while` loops
  - Counters
  - User input

**Example output:**
```
project_qr_0.png
project_qr_1.png
```


⚠️ On re-running the file, numbering resets to `0`.

---

### 2. `persistent_qr_generator.py`
**Use this file for real-world usage**

- Remembers previously generated QR numbers
- Continues numbering even after restarting the program
- Uses a text file (`count.txt`) to store the last count
- Prevents file overwrite

**Example output across runs:**
```
Run 1 → project_qr_0.png, project_qr_1.png
Run 2 → project_qr_2.png, project_qr_3.png
```

This version is recommended for:
- College events
- Bulk student QR generation
- Professional usage

---

## Installation

Install the required library using:

```bash
pip install qrcode[pil]
```
# How to Run
```
python basic_qr_generator.py
```
## or

```
python persistent_qr_generator.py
```
# How to Stop the Program
```
type : done in input statement
```
# Output

> QR codes are saved as .png files in the same folder:
