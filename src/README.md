# Running this app

First, you have to create a venv and install the requirements. 

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Move to the right folder and  export the configuration variables. 
You have to do this for two variables `ENVIRONMENT` and `PYTHONPATH`. 
Then you can start the app. For example:

```
$ cd src
.../src$ export ENVIRONMENT="production"
.../src$ export PYTHONPATH="/home/lee/projects/testing_talk/src/"
.../src$ uvicorn app:app --reload
```

Possible values of ENVIRONMENT are `production`, `test` or `development`.
For each value a new database is created.

## Testing

You have a beatiful Makefile to run the tests of this app.
To run unitest run:

```
$ make run_unit_tests
```

To run integration tests:

```
$ make run_integration_tests
```

To run end to end test, first you have to up the app with `ENVIRONMENT="test"
and then run (internet connection is needed to run these tests):

```
$ make run_end2end_tests
```

