FROM keybaseio/client:nightly-python

LABEL maintainer="Dakota Brown <dakota.kae.brown@gmail.com>"

ARG BUILD_TS
ARG GIT_REF
ARG APP_VERSION

LABEL org.lavel-schema.schema-version="1.0"
LABEL org.label-schema.build-date=${BUILD_TS}
LABEL org.label-schema.name="dakotakae/kbfs_upload"
LABEL org.label-schema.description="A simple API to accept uploads to a KBFS directory."
LABEL org.lable-schema.vcs-url="https://www.github.com/da-code-a/kbfs-upload-api"
LABEL org.label-schema.vcs-ref=${GIT_REF}
LABEL org.label-schema.version=${APP_VERSION}
LABEL org.label-schema.docker.cmd="docker run dakotakae/kbfs_upload -p 5000:5000 -d"

ENV KEYBASE_ALLOW_ROOT=1
ENV KEYBASE_SERVICE=1
ENV KEYBASE_KBFS_ARGS="-debug -mount-type=force"

EXPOSE 5000

WORKDIR /code
COPY . /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD kbfsu