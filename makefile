build:
	docker build \
	--build-arg BUILD_TS=$(date -u + '%Y-%m-%d%T%H:%M:%SZ') \
	--build-arg APP_VERSION=$(poetry run python -c "from kbfs_upload import __version__; print(__version__)") \
	--build-arg GIT_REF=$(git log --pretty-format:'%h' -n 1)
	--no-cache=true \
	-t dakotakae/kbfs_upload:latest .