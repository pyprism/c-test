# c-test

#### Run locally
```
docker-compose up
```

#### Run test
```
docker-compose exec web python manage.py test
```

### Work flow
  - At first copy config.json and create a new file named config.local.json. Put appropriate values .
  - Create superuser from terminal `docker-compose exec web python manage.py createsuperuser`
  - Go to `http://127.0.0.1:8000/v1/api/account/` and login, after login superuser can see list of accounts, also can create a normal user account.
  - Go to `http://127.0.0.1:8000/v1/api/city_name/` for CRUD operation of city name
  - After creating a city, user can see current weather from `http://127.0.0.1:8000/v1/api/city_name/{pk}/get_current_weather/`
  - User can search by city name from `http://127.0.0.1:8000/v1/api/city_name/search_city/?city_name={name of the city}`

### Things I focused on:
  - CRUD
  - Cached api results
  - Search/Filtering with pagination
  - Unit Tests
  - Easy setup/deployment
