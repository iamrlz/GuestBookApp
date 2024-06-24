# GuestbookApp

**GuestbookApp** is a simple web application built using Flask and Docker, designed to allow users to leave messages in a virtual guestbook. The application provides a straightforward interface for submitting and displaying messages, making it ideal for personal or small-scale use cases where basic guestbook functionality is required.

## Features

- **Guestbook Functionality:** Users can submit messages that are stored and displayed in a guestbook format.
- **Minimalist UI:** The application offers a clean and intuitive user interface for interacting with the guestbook.
- **Dockerized Environment:** Docker is used for containerization, ensuring easy deployment and environment consistency across different systems.

## Technologies Used

- **Flask:** Python-based web framework used for developing the application.
- **Docker:** Containerization technology used to package the application and its dependencies into isolated containers.
- **Python 3.9:** Programming language used for backend logic and application development.

# Build and Run the Docker Image:

``` docker-compose up --build ```


### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/iamrlz/GuestBookApp.git
$ docker build -t iamrlz/GuestBookApp .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/lvthillo/python-flask-docker/).
```
docker pull iamrlz/GuestBookApp
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 iamrlz/GuestBookApp
```

Now visit http://localhost:8080
```
 The hostname  IP is 172.19.0.2/5050. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.19.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
3eefbfbad102
```


