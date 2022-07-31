.PHONY: env
env:
	virtualenv .venv -p /usr/bin/python3
	. .venv/bin/activate && python -m pip install -r requirements.txt

.PHONY: test
runtest:
	echo "To be implemented"

.PHONY: run
run:
	. .venv/bin/activate && python kanban-warrior.py