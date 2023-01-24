# Mode Deployment Locally, Using Docker, Using K8s and AWS

1. Run Flask application locally :

```python
python app.py
```
- Using Flask to deploy ML models. We will gradually learn how to use html form and a pre-saved pickle model to pass the user's input to the model, run the prediction process and print back the output of the model.

2. To deploy the model using docker

 - First create the docker image using the following commands:
 
```bash
docker build -t my-app .
```
 - Then, runn then container

 ```bash
docker run -p 5000:5000 my-app
 ```
The appe will be running in the following port

```
http://localhost:5000/
```

3. To deploy the app to K8s:

Start your minkube cluster
```bash
minikube start
```
build the image in the cluster 
```bash
minikube image build -t my-app .
```
Now create deployment
```bash
cd kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
You should be able to see the app up and running

```bash
kubectl get pod
```
```bash
kubectl get svc
```

```bash
minikube service my-service
```

This should launch the app in the browser

4. Deployment to AWS ECS

First we need to tage the image and then push it to the AWS ECR

Since I am using the M1 chip, I will be using the `--platform=linux/amd64 .` to build the image of the app

```bash
docker build -t my-app --platform=linux/amd64 .
```

Now log in to your ECR using the following
```bash
aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin <account_id>.dkr.ecr.ca-central-1.amazonaws.com
```
You can also find the commands to sign in to the ECR in the image repo in the ECR

Next, you can now tag the image

```bash
docker tag my-app:latest <account_id>.dkr.ecr.ca-central-1.amazonaws.com/repo1:latest
```
and push it the ECR

```bash
docker push <account_id>.dkr.ecr.ca-central-1.amazonaws.com/repo1:latest
```

In the ECS AWS, we will need to create a cluster with a network and ECS instance. Once the cluster is created we will need to create a task in the task definition where we will have to define our container specificaitons. There we will need to provide the url for the image, and will do the port mapping, if you are using the flask then we need to use 5000 port.

Next, you will need to define a service that will be used to give access to the container, make sure to allow inbound and outbound traffic for the EC2 instance.






This should launch the app in the browser


