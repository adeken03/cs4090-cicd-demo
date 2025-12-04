# cicd_demo

Small Python demo used for the CS4090 CI/CD exercise. It implements helpers in `src/app.py` and validates them with `pytest` in `tests/test_app.py`.

## Run locally
```
python -m venv .venv
.\.venv\Scripts\activate   # on macOS/Linux use: source .venv/bin/activate
pip install -r requirements.txt
pytest --cov=src --cov-report=term --cov-report=html --html=report.html --self-contained-html
```

## CI/CD workflow
GitHub Actions workflow `.github/workflows/ci.yml:
- triggers on pushes/PRs to `master` or `main`
- installs dependencies on Python 3.10, runs pytest plus coverage
- packages reports into `site/` on pushes, deploys them to GitHub Pages

