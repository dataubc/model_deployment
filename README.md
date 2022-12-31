# Mode Deployment

- Using Flask to deploy ML models. We will gradually learn how to use html form and a pre-saved pickle model to pass the user's input to the model, run the prediction process and print back the output of the model.
- To deploy the model using docker

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

Part of my teaching at Concordia Data Science Bootcamp*

