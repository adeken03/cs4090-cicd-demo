# cicd_demo

Small Python demo used for the CS4090 CI/CD exercise. It implements helpers in `src/cs4090_cicd_demo/app.py` and validates them with `pytest` in `tests/test_app.py`.

## Run locally
```
python -m venv .venv
.\.venv\Scripts\activate   # on macOS/Linux use: source .venv/bin/activate
pip install -r requirements.txt
pytest -q --cov=. --cov-report=term --cov-report=xml --cov-report=html
```

## CI/CD workflow
Workflows are split per the quiz:
- `.github/workflows/ci.yml` runs only on pushes/PRs to `development` (CI).
- `.github/workflows/cd.yml` runs only when a PR from `development` into `main`/`master` is merged, then publishes coverage reports to GitHub Pages (CD).
