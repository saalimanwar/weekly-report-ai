# AI Weekly Status Report Generator

### Submitted By:
Salim Anwar
--------------------------------------------------------------------------------------------------------------------------------------------------------------

### Problem:
Writing weekly summaries manually is slow, repetitive, and inconsistent across teams.

### Solution:
A web-based AI assistant that:
- Takes a CSV of weekly tasks
- Uses OpenAI GPT to generate a professional summary
- Saves time, improves clarity, and removes manual effort

###  Impact:
- Saves ~60 minutes per user per week
- Works for any team with a simple CSV format
- Scalable, efficient, and easy to use

###  Files Included:
- `app.py` – Main Streamlit app
- `sample_tasks.csv` – Example input
- `requirements.txt` – Required libraries

###  How to Run:
```bash
pip install -r requirements.txt
streamlit run app.py
