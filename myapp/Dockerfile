FROM nginx:alpine

WORKDIR /var/www

RUN mkdir -p "/var/log/nginx"
RUN chmod -R a+w /var/log/nginx

RUN addgroup \
    --gid 1000 \
    docker

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup docker \
    --no-create-home \
    --uid 1000 \
    docker

RUN addgroup nginx docker


COPY nginx.conf /etc/nginx/nginx.conf
COPY empty /etc/nginx/conf.d/default.conf
COPY nginx-default.conf /etc/nginx/sites-available/default.conf
COPY index.html ./index.html
RUN chown -R docker:docker /var/www

CMD ["nginx"]
EXPOSE 80

