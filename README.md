# Test Example for CAS598 Fundamentals of Research Software Engineering Class

There is one function in `temps.py`, which has tests in `temps_test.py`. Tests can be run with:
```
python -m unittest temps_test.p
```

# Coverage

If *Coverage* is installed, coverage report can be created with:
```
coverage run -m unittest temps_test.py
coverage report -m
```
or by running the script `run_coverage.sh`:
```
./run_coverage.sh
```

# Virtual Environment

It's recommended to use a virtual environment. You can create one with:
```
python3 -m venv venv
```
and then activate it with
```
source venv/bin/activate
```

After that the requirements can be installed with:
```
pip install -r requirements.txt
```
