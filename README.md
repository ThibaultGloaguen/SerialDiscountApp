# Serial to Discount registry

This application allows the user to exchange his serial number for a discount code throught a web application.
The backend is written in python 3.7 with the Flask framework and the frontend is written in javascript with the vuejs framework.

The backend API:

| Method | Path | README |
| ------ | ------ | ------ |
| GET | /discount | get a discount code ( please provide mandatory parameter serial_number ) |



# Installation

This application requires Docker to run.
By default, the Docker will expose port 5000. To change this configuration, you can modify the docker-compose.yml to choose another port.
To install and run the server application:
```sh
$ docker-compose build
```

# Run
```sh
$ docker-compose up application
```
The server should now run on http://0.0.0.0:5000

### Tests

This solution is provided with tests.
To run those tests:
```sh
$ docker-compose up test
```

### Explanation

This application is provided with two separate database. One key value database with all the serial numbers
provided in the sample and one other database with a list with all the discount codes.

When a user send a request to get a discount code, the server checks if the serial number exists. if not it throws a 404.
If the serial number exists, it checks if there is already a discount code paired to this serial.
If not, the server gets the list of discount available and pop the first one of the list and pair it to the current serial number.

The discount code list database is updated with one less discount code and the serial number database is updated so the new serial / discount pair is saved.



### Edge case

In the case where there is more serial numbers than discount codes, once the discount code list is empty. the server throws a 410 error and informs to the user that there is no more discount code available.

In the case where there is more discount code than serial numbers, no problem because everyone can get his serial numbers ;).






## Thanks for reading ;)