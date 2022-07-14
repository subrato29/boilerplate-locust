Author: Subrata Sarkar
------------------------------

```
Locust is a performance testing tool

boilerplate-locust

````

Running the tests with webUI:
-------------------
```
locust -f <FILENAME>.py

```

Running the tests by command prompt:
-------------------
```
mkdir <CREATING_LOG_DIR> && locust -f <DIR_OF_.py_file> -u 1 -r 1 -t 10s --headless --print-stats --csv log/Run1.csv --csv-full-history

e.g.
mkdir log && locust -f startstop/startstop_user.py -u 1 -r 1 -t 10s --headless --print-stats --csv log/Run1.csv --csv-full-history

```