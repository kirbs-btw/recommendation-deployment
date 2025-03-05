# recommendation-deployment
## general
This repo is for deploying a song recommendation logic with a docker container. 

## container setup
```sh
docker build -t recommendation-api . 
```

```sh
docker run -p 5000:5000 recommendation-api
```

## test
```sh
Invoke-WebRequest -Uri "http://127.0.0.1:5000/recommend/from_id" ` 
    -Method Post `
    -Headers @{"Content-Type"="application/json"} `
    -Body '{"id": "All Be Okay Lissie"}'
```