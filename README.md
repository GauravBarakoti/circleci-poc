
# CircleCI Documentation

https://circleci.com/docs/configuration-reference/

This documentation will help you understand CircleCI and will also help in deploying your application with approximately no downtime on a server using the CircleCI pipeline.

We'll start from the very basics.

Take any server in our case I'm proceeding with an ubuntu server on AWS.

I have a sample FLASK application.

Now, we require Apache and Docker.

# Apache and Docker Installation Documentation

This documentation provides step-by-step instructions for installing Apache web server and Docker on your server. Additionally, it includes guidance on hosting a Python Flask application inside a Docker container, where Apache will act as a load balancer to ensure zero downtime during code updates triggered through CircleCI pipeline.

## Table of Contents
1. [Apache Installation](#apache-installation)

2. [Docker Installation](#docker-installation)
3. [Hosting Python Flask Application in Docker with Apache Load Balancer](#hosting-python-flask-application-in-docker-with-apache-load-balancer)
4. [CircleCI pipeline to Automate Deployment of New versions](#CircleCI-pipeline-to-Automate-Deployment-of-New-versions)
---

## 1. Apache Installation

Apache is a widely-used web server software. Follow these steps to install Apache:

You can refer to this document or copy these commands:

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

```bash
# Update package lists
sudo apt-get update
```
```bash
# Install Apache
sudo apt-get install apache2
```
```bash
# Start Apache
sudo systemctl start apache2
```
```bash
# Check Apache Status
sudo systemctl status apache2
```

To test if Apache is running, open a web browser and enter your server's IP address. You should see the default Apache page.

---

## 2. Docker Installation 

Docker is a platform for developing, shipping, and running applications. Docker containers offer perfect host for small independent applications. 

Document for docker installation:
https://docs.docker.com/engine/install/ubuntu/

To install Docker, follow these steps:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

To install the latest version, run:
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Test Docker installation by running:

```bash
sudo docker --version
```

---

## 3. Hosting Python Flask Application in Docker with Apache Load Balancer 

Now, let's host your Python Flask application inside a Docker container and configure Apache as a load balancer.

1. **Build Docker Image**: Create a Dockerfile for your Flask app and build the Docker image.


   Build the image:

   ```bash
   sudo docker build -t flask-app .
   ```

2. **Run Docker Container**: Run the Docker container and map the necessary ports:

    e.g.

   ```bash
   docker run -d -p 8081:5000 flask-app
   ```

   This will start your Flask app inside a Docker container, exposed on port 8080.

3. **Configure Apache Load Balancer**: Install and configure Apache as a reverse proxy and load balancer. Create an Apache configuration file for your Flask app (e.g., `myapp.conf`) in `/etc/apache2/sites-available/`:

    Install Required Apache modules:
    
    ```bash
    sudo a2enmod proxy
    ```
    mod_proxy is the main proxy module that redirects requests and allows Apache to act as gateway to backend servers.
    ```bash
    sudo a2enmod proxy_http
    ```
    mod_proxy_http allows support for proxying HTTP requests.
    ```bash
    sudo a2enmod proxy_balancer
    ```
    ```bash
    sudo a2enmod lbmethod_byrequests
    ```
    mod_proxy_balancer and mod_lbmethod_byrequests add load balancing capabilities to Apache web server.

    changes in apache 000-default.conf
    ```bash
    cd /etc/apache2/sites-available/ 
    ```
    ```bash
    sudo vi 000-default.conf
    ```

   ```apache
   <VirtualHost *:80>
        #...
        <Proxy "balancer://mycluster">
                BalancerMember "http://localhost:8081"
                BalancerMember "http://localhost:8082"
        </Proxy>
        ProxyPreserveHost On
        # ProxyPreserveHost causes Apache to preserve original host header and pass it to back-end servers.
        ProxyPass "/" "balancer://mycluster/"
        ProxyPassReverse "/" "balancer://mycluster/"
        # We list our backend servers in Proxy tag named balancer://mycluster . You can change it to anything else.
        #...
   </VirtualHost>
   ```

   Enable the new configuration and reload Apache:

   ```bash
   sudo systemctl reload apache2
   ```

Now, your Flask application should be accessible via Apache on port 80. Apache will act as a load balancer, providing zero downtime when you push new code versions through your CircleCI pipeline.

# 4. CircleCI pipeline to Automate Deployment of New versions

![App Screenshot](https://circleci.com/docs/assets/img/docs/arch.png)


You can follow the official documentation

https://circleci.com/docs/first-steps/

Or follow these steps ->

Go to: https://circleci.com/signup/  -> Sign Up  -> Provide Email and Password

On the Welcome page provide the necessary details.

Now, Connect to your code using GitHub, GitLab.com, Bitbucket.

For now, I'm proceeding with GitHub.

Firstly you will not have any projects which CircleCI follows.

Go to Projects and Follow the repository which you want CircleCI to follow.







Feel free to adapt this documentation to your specific requirements and Flask application configuration.

