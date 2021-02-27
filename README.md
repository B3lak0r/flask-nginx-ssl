FLASK-NGINX-SSL (BITWALA CHALLENGE)

Flask "Hello World" nginx self signed ssl docker repo.

Dockerfile based on tiangolo/uwsgi-nginx:python3.8-alpine image, main changes / modifications:

1.- Added openssl for self signed certs
2.- A nginx.conf file for https redirection pointing to uwsgi socket.
3.- Modified entripoint.sh including self signed cert generation steps.

