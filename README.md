# Mode Deployment


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


