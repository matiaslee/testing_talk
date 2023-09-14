# Running this app


Export configuration variables. You have to do this for two variables
`ENVIRONMENT` and `PYTHONPATH`. Then you can start the app. For example:

```
$ export ENVIRONMENT="production"
$ export PYTHONPATH="/home/lee/projects/testing_talk/src/"
$ uvicorn app:app --reload
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
and then run:

```
$ make run_end2end_tests
```

You need internet connection to run these tests.
