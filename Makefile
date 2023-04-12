.ONESHELL:
SHELL = /bin/bash

.PHONY : env 
## env: creates and configures the environment
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate ligo
	conda install ipykernel
	python -m ipykernel install --user --name ligo --display-name "IPython - ligo"

.PHONY : html 
## html: build the JupyterBook normally
html: 
	jupyter-book build . 

.PHONY : clean
## clean: clean up the figures, audio and _build folders
clean: 
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/*

.PHONY : help
## help: prints documentation
help : Makefile
	@sed -n '/^##/p' $<