# recommendation-deployment
## general
This repo is for deploying a song recommendation logic with a docker container. 

## container setup
```sh
docker build -t recommendation-api . 
```

```sh
docker run -e API_KEY=thisistheapikey -p 5000:5000 recommendation-api
```

## test
```sh
curl -X POST http://127.0.0.1:5000/recommend/from_id ^
     -H "Content-Type: application/json" ^
     -d "{\"id\": \"All Be Okay Lissie\"}"
```