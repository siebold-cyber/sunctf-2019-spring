FROM php:7.3-apache

COPY ./php.ini $PHP_INI_DIR/php.ini
COPY ./public_html /var/www/html
RUN docker-php-ext-install pdo_mysql mysqli mbstring

EXPOSE 8080
