# --- Docker build ---
# docker build -t cookiecutter-mymcpserver:latest .
# --- Docker run ---
# docker run -it --rm -v /Users/sanhehu/Documents/GitHub/cookiecutter_mymcpserver-project:/usr/src/app cookiecutter-mymcpserver:latest
# ECR Gallery https://gallery.ecr.aws/docker/library/python
# --- stage 1 ---
# we install dependencies and run unit test
FROM public.ecr.aws/docker/library/python:3.11-slim AS build
# We need these two environment variables to run unit test
# you can always override it in Batch job definition or in submit job API
ARG USER_ENV_NAME=""
ARG PARAMETER_NAME=""
# if "run unit test" is part of the docker build process, we may need to give
# the container AWS credential. these env vars are only required in stage 1
# we will not include them in stage 2
ARG AWS_REGION=""
ARG AWS_ACCESS_KEY_ID=""
ARG AWS_SECRET_ACCESS_KEY=""
ARG AWS_SESSION_TOKEN=""
# !! don't leave it uncommented in CI, this is for local debug, use it with caution
# RUN env
# this is the working directory in the container
# it should have the same folder structure of your git repo
WORKDIR /usr/src/app
# copy the following file to working directory
# these file are not changing frequently, so it should go to the top of Dockerfile as a layer cache
COPY pyproject.toml \
    poetry.toml \
    poetry.lock \
    requirements.txt \
    requirements-dev.txt \
    requirements-test.txt \
    requirements-poetry.txt \
    README.rst \
    ./
# install virtualenv, then create virtualenv, install main and test dependencies
# since we are using Poetry to resolve the deterministic dependency,
# this layer is not chaging frequently as before
RUN pip install virtualenv && \
    pip install -r requirements-poetry.txt && \
    virtualenv .venv && \
    poetry install --no-root --extras mcp
# copy the source code and test cases to the working directory
# these two folder are chaging frequently
COPY cookiecutter_mymcpserver/ ./cookiecutter_mymcpserver
# install the source package itself and run unit test
# after that, destroy the virtualenv. because this virtualenv has lots of unnecessary dependencies
# we should create a clean virtualenv that include necessary dependencies.
# we also clean up the wheel, setuptools, pip as well
# finally we display the total size of the virtualenv
RUN poetry install && \
    ls -la /usr/src/app/.venv/bin/ >&2 && \
    du /usr/src/app/.venv/ -H
ENTRYPOINT ["/usr/src/app/.venv/bin/python", "-m", "cookiecutter_mymcpserver.app"]
CMD ["--config", "/usr/src/app/config.json"]


# --- stage 2 ---
# we only copy the tested, built virtualenv to the final image
FROM public.ecr.aws/docker/library/python:3.11-slim
WORKDIR /usr/src/app
# the final docker image is environment (sbx, tst, prd) awared, we need these two
# environment variables to tell the image which environment it at
ARG USER_ENV_NAME
ARG PARAMETER_NAME
# !! don't leave it uncommented in CI, this is for local debug, use it with caution
# RUN env
COPY --from=build /usr/src/app/.venv ./.venv
COPY --from=build /usr/src/app/cookiecutter_mymcpserver ./cookiecutter_mymcpserver
ENTRYPOINT ["/usr/src/app/.venv/bin/python", "-m", "cookiecutter_mymcpserver.app"]
CMD ["--config", "/usr/src/app/config.json"]
