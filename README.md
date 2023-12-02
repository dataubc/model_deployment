"""
# Model Deployment Strategies: Local, Docker, Kubernetes (K8s), and AWS

## 1. Running a Flask Application Locally
Deploy ML models using Flask by executing the application with the command:
```bash
python app.py
```
This process involves using an HTML form and a pickle file to run predictions and display outputs.

## 2. Deployment Using Docker
To containerize your application with Docker, follow these steps:

- Build the Docker image:
```bash
docker build -t my-app .
```
- Run the Docker container:
```bash
docker run -p 5000:5000 my-app
```
Access the app at http://localhost:5000/.

## 3. Deployment Using Kubernetes (K8s)
Deploy your app on Kubernetes with the following commands:

- Start Minikube:
```bash
minikube start
```
- Build the image within Minikube:
```bash
minikube image build -t my-app .
```
- Deploy the application:
```bash
cd kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
Check the deployment and service:
```bash
kubectl get pods
kubectl get svc
```
Launch the app in a browser:
```bash
minikube service my-service
```

## 4. Deployment on AWS ECS
For AWS ECS deployment, prepare your Docker image and push it to AWS ECR:

- Build the image (for M1 chip, use --platform=linux/amd64):
```bash
docker build -t my-app --platform=linux/amd64 .
```
- Authenticate with AWS ECR:
```bash
aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin <account_id>.dkr.ecr.ca-central-1.amazonaws.com
```
- Tag and push the Docker image:
```bash
docker tag my-app:latest <account_id>.dkr.ecr.ca-central-1.amazonaws.com/my-repo:latest
```
- Push the image to AWS ECR:
```bash
docker push <account_id>.dkr.ecr.ca-central-1.amazonaws.com/my-repo:latest
```

In AWS ECS, create a cluster and an instance with a network. Then create a task definition where you define the container specifications and provide the URL for the image. For Flask apps, use port 5000.

Define a service in ECS to access the container and ensure the EC2 instance allows inbound and outbound traffic.

## Cleanup:

- Delete the Kubernetes deployment:
```bash
kubectl delete service my-service
kubectl delete deployment model-deployment
```

- Stop Minikube:
```bash
minikube stop
```
