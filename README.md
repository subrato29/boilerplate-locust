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
----------------------------
```
rm -rf <LOG_DIR> mkdir <CREATING_LOG_DIR> && locust -f <DIR_OF_.py_file> -u 1 -r 1 -t 10s --headless --print-stats --csv log/Run1.csv --csv-full-history

e.g.
rm -rf log && mkdir log && locust -f startstop/startstop_user.py -u 1 -r 1 -t 10s --headless --print-stats --csv log/Run1.csv --csv-full-history

e.g.
rm -rf log && mkdir log && locust -f httpuser/httpuser.py -u 1 -r 1 -t 10s --headless --print-stats --csv log/Run1.csv --csv-full-history -L DEBUG --logfile log/app_log.log --html log/html_report.html

e.g.
locust -f httpuser/httpuser.py --show-task-ratio

Show all user class in your locust script
e.g.
locust -f httpuser/httpuser.py --l
```