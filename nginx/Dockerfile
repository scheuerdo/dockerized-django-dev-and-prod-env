FROM nginx:1.25

# Install vim and systemd for debugging purposes on the production web server
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y systemd

# Replace the default Nginx configuration file with the custom nginx.conf file
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d