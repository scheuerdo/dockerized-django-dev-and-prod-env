FROM python:3.10 as base

# Adding a non-root user to run the application
RUN addgroup --system web \
    && adduser --system --ingroup web web

# Cleaning up the image
RUN apt-get update \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


USER web

WORKDIR /home/web/exampleDjangoProject/

# Copying the requirements file and installing the dependencies
COPY --chown=web:web ./requirements.txt requirements.txt
USER root
RUN pip install --no-cache-dir -r requirements.txt
USER web

COPY --chown=web:web ./docker/exampleDjangoProject/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Setting the entrypoint script
ENTRYPOINT ["entrypoint.sh"]


################################ Development stage ###################################################
FROM base as dev

# Copying scripts that starts the development application server (Django runserver command)
COPY --chown=web:web ./docker/exampleDjangoProject/start-dev-server.sh /usr/local/bin/start-dev-server.sh
RUN chmod +x /usr/local/bin/start-dev-server.sh

# Running the development server start up script
CMD ["start-dev-server.sh"]



################################ Production/Deployment stage #########################################
FROM base as prod

# Copying the production requirements file and installing the production dependencies
COPY --chown=web:web ./requirements.prod.txt requirements.prod.txt
USER root
RUN pip install --no-cache-dir -r requirements.prod.txt
USER web

# Copying the application code
COPY --chown=web:web . ./

# Copying scripts that starts the production application server (gunicorn)
USER root
COPY --chown=web:web ./docker/exampleDjangoProject/start-prod-server.sh /usr/local/bin/start-prod-server.sh
RUN chmod +x /usr/local/bin/start-prod-server.sh


# Running the production server start up script
CMD ["start-prod-server.sh"]