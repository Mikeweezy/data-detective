# Data Detective 🔍

A Python project for exploring and analyzing datasets — loading data, profiling it, detecting issues, and generating reports.

## Project Structure

```
data-detective/
├── data/
│   └── sample/          # Sample datasets for exploration
├── reports/             # Generated analysis reports
├── src/
│   └── data_detective/  # Main source package
├── tests/               # Unit and integration tests
├── README.md
├── requirements.txt
├── .gitignore
└── main.py              # Entry point
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mikeweezy/data-detective.git
cd data-detective
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

## Usage

Place your sample datasets in `data/sample/`, then run `main.py` to start
an analysis. Results and generated reports are written to `reports/`.

## Development

- Source code lives in `src/data_detective/`.
- Add tests to `tests/` and run them with:

```bash
python -m pytest tests/
```

## License

TBD
