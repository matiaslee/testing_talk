run_unit_tests:
	pytest -m "not integration_test and not end2end_test"


run_integration_tests:
	export ENVIROMENT=test
	python tests/populate_test_db.py
	pytest -m integration_test -vv
	rm database_test.sqlite
	unset ENVIROMENT


run_end2end_tests:
	export ENVIROMENT=test
	python tests/populate_test_db.py
	pytest -m end2end_test -vv
	rm database_test.sqlite
	unset ENVIROMENT
