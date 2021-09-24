BUILD_TS := $(shell date -u +'%Y-%m-%d%T%H:%M:%SZ')
APP_VERSION := $(shell poetry run python -c "from kbfs_upload import __version__; print(__version__)")
GIT_REF := $(shell git log --pretty='format:%h' -n 1)

build: SHELL:=/bin/bash
build:
	docker build \
	--build-arg BUILD_TS="$(BUILD_TS)" \
	--build-arg APP_VERSION="$(APP_VERSION)" \
	--build-arg GIT_REF="$(GIT_REF)" \
	--no-cache=true \
	-t dakotakae/kbfs_upload:latest .