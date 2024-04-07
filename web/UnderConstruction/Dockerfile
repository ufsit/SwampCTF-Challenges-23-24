# Use an official PHP runtime as a parent image
FROM php:7.4-apache

# Install system dependencies for MySQL and PHP extensions
RUN apt-get update && apt-get install -y \
    mariadb-server \
    mariadb-client \
    && docker-php-ext-install mysqli pdo pdo_mysql

# Copy the current directory contents into the container at /var/www/html
COPY ./www /var/www/html

# Copy your SQL file into the container
COPY ./init_db.sql /tmp/init_db.sql

# Use the default development configuration
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"

# Create a startup script that will start MariaDB, Apache and populate the database
RUN echo '#!/bin/bash\n\
service mariadb start\n\
# Wait for MariaDB to fully start. Adjust the sleep time as necessary.\n\
sleep 10\n\
# Initialize the database with the SQL file\n\
mysql < /tmp/init_db.sql\n\
# Start Apache in foreground\n\
apache2-foreground' > /entrypoint.sh \
    && chmod +x /entrypoint.sh

# Expose port 80
EXPOSE 80

# Use the custom script as the entrypoint
CMD ["/entrypoint.sh"]
