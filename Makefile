NAME := sre-joe-bot
REPO := quay.io/app-sre/$(NAME)
TAG := $(shell git rev-parse --short HEAD)

ifneq (,$(wildcard $(CURDIR)/.docker))
	DOCKER_CONF := $(CURDIR)/.docker
else
	DOCKER_CONF := $(HOME)/.docker
endif

all:
	@echo
	@echo "Targets:"
	@echo "venv:          Create local venv and install dependencies"
	@echo "check:         Check for flake8 and pylint errors"
	@echo "image:         Build container image"
	@echo "image-push:    Push container image"
	@echo

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python -mvenv venv
	. venv/bin/activate; pip install -r requirements.txt
	touch venv/bin/activate

venv-test: venv-test/bin/activate

venv-test/bin/activate: requirements-test.txt
	test -d venv-test || python -mvenv venv-test
	. venv-test/bin/activate; pip install -r requirements-test.txt
	touch venv-test/bin/activate

run: venv
	. venv/bin/activate; errbot

clean:
	rm -rf venv
	git clean -Xfd

check: venv-test
	. venv-test/bin/activate; flake8 plugins
	. venv-test/bin/activate; pylint plugins

image: build
	docker build -t $(REPO):$(TAG) Dockerfile .

image-push:
	docker tag $(REPO):$(TAG) $(REPO):latest
	docker --config=$(DOCKER_CONF) push $(REPO):$(TAG)
	docker --config=$(DOCKER_CONF) push $(REPO):latest
