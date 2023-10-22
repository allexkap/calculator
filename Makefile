PYTHON=$(VENV)/bin/python3
CC=gcc

.PHONY: all clean


all: calc.c
	$(CC) -o calc calc.c

calc.c: codegen.py
	$(PYTHON) codegen.py

clean:
	rm -f calc calc.c
