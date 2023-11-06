# Django-Todo-App
This project is used for DevOps Practice - Dockerize and deploy using Jenkins pipeline 
## Installation
1. Clone the repository
```
git clone git@github.com:siddhantbhattarai/Django-Todo-App.git
```

2. Build the app
```
docker build -t todo-app .
```

3. Run the app
```
docker run -d -p 8000:8000 todo-app:latest
```
