
# CircleCI Documentation

https://circleci.com/docs/configuration-reference/

This documentation will help you understand CircleCI and will also help in deploying your application with approximately no downtime on a server using the CircleCI pipeline.

We'll start from the very basics.

Take

# Apache and Docker Installation Documentation

This documentation provides step-by-step instructions for installing Apache web server and Docker on your server. Additionally, it includes guidance on hosting a Python Flask application inside a Docker container, where Apache will act as a load balancer to ensure zero downtime during code updates triggered through CircleCI pipeline.

## Table of Contents
1. [Apache Installation](#apache-installation)
2. [Docker Installation](#docker-installation)
3. [Hosting Python Flask Application in Docker with Apache Load Balancer](#hosting-python-flask-application-in-docker-with-apache-load-balancer)

---

## 1. Apache Installation <a name="apache-installation"></a>

Apache is a widely-used web server software. Follow these steps to install Apache:

```bash
# Update package lists
sudo apt-get update

# Install Apache
sudo apt-get install apache2

# Start Apache
sudo systemctl start apache2

# Enable Apache to start on boot
sudo systemctl enable apache2
```

To test if Apache is running, open a web browser and enter your server's IP address. You should see the default Apache page.

---

## 2. Docker Installation <a name="docker-installation"></a>

Docker is a platform for developing, shipping, and running applications. To install Docker, follow these steps:

```bash
# Update package lists
sudo apt-get update

# Install required dependencies
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update package lists (again)
sudo apt-get update

# Install Docker
sudo apt-get install docker-ce

# Start Docker
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker
```

Test Docker installation by running:

```bash
sudo docker --version
```

---

## 3. Hosting Python Flask Application in Docker with Apache Load Balancer <a name="hosting-python-flask-application-in-docker-with-apache-load-balancer"></a>

Now, let's host your Python Flask application inside a Docker container and configure Apache as a load balancer.

1. **Build Docker Image**: Create a Dockerfile for your Flask app and build the Docker image.

   ```Dockerfile
   FROM python:3.8

   WORKDIR /app

   COPY requirements.txt requirements.txt

   RUN pip install -r requirements.txt

   COPY . .

   CMD ["python", "app.py"]
   ```

   Build the image:

   ```bash
   docker build -t flask-app .
   ```

2. **Run Docker Container**: Run the Docker container and map the necessary ports:

   ```bash
   docker run -d -p 8080:8080 flask-app
   ```

   This will start your Flask app inside a Docker container, exposed on port 8080.

3. **Configure Apache Load Balancer**: Install and configure Apache as a reverse proxy and load balancer. Create an Apache configuration file for your Flask app (e.g., `myapp.conf`) in `/etc/apache2/sites-available/`:

   ```apache
   <VirtualHost *:80>
       ProxyPass / http://localhost:8080/
       ProxyPassReverse / http://localhost:8080/
   </VirtualHost>
   ```

   Enable the new configuration and reload Apache:

   ```bash
   sudo a2ensite myapp.conf
   sudo systemctl reload apache2
   ```

Now, your Flask application should be accessible via Apache on port 80. Apache will act as a load balancer, providing zero downtime when you push new code versions through your CircleCI pipeline.

Feel free to adapt this documentation to your specific requirements and Flask application configuration.

