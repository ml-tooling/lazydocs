FROM ubuntu:20.04

# Fix for pipe operations: https://github.com/hadolint/hadolint/wiki/DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Generate and Set locals
# https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-debian-ubuntu-docker-container#38553499
RUN apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LC_ALL="en_US.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US:en" \
    TZ="Europe/Berlin" \
    DEBIAN_FRONTEND="noninteractive" \
    RESOURCES_PATH="/resources"

# Create resources folder
RUN mkdir $RESOURCES_PATH && chmod a+rwx $RESOURCES_PATH

# Install basics
# hadolint ignore=DL3005
RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y upgrade \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        wget \
        gnupg2 \
        git \
        jq \
        software-properties-common \
        # Required by Pyenv
        make \
        build-essential \
        libbz2-dev \
        libssl-dev \
        libreadline-dev \
        libsqlite3-dev \
        libffi-dev \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.19.0/tini -O /tini && \
    chmod +x /tini

# Install Docker in Container
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable" \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends docker-ce=5:19.03.13~3-0~ubuntu-focal \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        gcc \
        python3-dev \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && pip install \
        setuptools==50.* \
        wheel==0.* \
        flake8==3.* \
        pytest==6.* \
        twine==3.* \
        mypy==0.* \
        pytest-cov==2.* \
        black==20.8b1 \
        pydocstyle==5.* \
        isort==5.* \
        docker==4.* \
        nox==2020.8.* \
        pipenv==2020.11.* \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pyenv to allow dynamic creation of python versions
RUN git clone https://github.com/pyenv/pyenv.git $RESOURCES_PATH/.pyenv
# Add pyenv to path
ENV PATH=$RESOURCES_PATH/.pyenv/shims:$RESOURCES_PATH/.pyenv/bin:$PATH \
    PYENV_ROOT=$RESOURCES_PATH/.pyenv

# Install web development tools
RUN apt-get update \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g yarn@1 \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install markdown lint tool
RUN npm install -g markdownlint@^0.21.1 markdownlint-cli@^0.24.0

# Workaround to get ssh working in act and github actions
RUN mkdir -p /github/home/.ssh/ \
    # create empty config file if not exists
    && touch /github/home/.ssh/config \
    && chown -R root:root /github/home/.ssh \
    && chmod 700 /github/home/.ssh \
    && ln -s /github/home/.ssh /root/.ssh

# Settings and configurations
ENV \
    # Flush log message immediately to stdout
    PYTHONUNBUFFERED=true \
    # Use local folder as pipenv virtualenv
    PIPENV_VENV_IN_PROJECT=true

# Install Universal-Build
# hadolint ignore=DL3013
RUN pip install git+https://github.com/ml-tooling/universal-build.git

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/tini", "-g", "--", "/entrypoint.sh"]
