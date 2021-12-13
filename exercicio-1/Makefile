.PHONY: help venv test
.DEFAULT: test

VENV?=venv
PYTHON=$(VENV)/bin/python3
PIP=$(PYTHON) -m pip
INSTALLED=$(VENV)/installed

test: venv
	$(PYTHON) -m pytest -q --tb=no --color=no

report: test_.py
	$(shell script -qefc make /dev/null > report)

help:
	@echo "uso: make [ venv | test | post | clean ]"

venv: $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --requirement requirements.txt
	touch $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	rm -rf dist
	rm -rf $(PACKAGE).egg-info
	rm -rf __pycache__
