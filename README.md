# Test Sample Web App

Testing over a single web app. It's just a web app to expose how to test it.

This web app depends on the ``Test sample server``.
- Server source: https://github.com/fmihaich/test_sample_server

## Pre-requisites

As it was said, this web app needs ``test sample server`` to correctly work (and to execute system tests).

Then, it is necessary to have a local image of the test sample server:

```bash
git clone https://github.com/fmihaich/test_sample_server.git
cd test_sample_server
docker build -f Dockerfile -t test_sample_test_runner:local .
```

## Web app image

In order to build the web app image execute the following command:
```bash
docker build -f Dockerfile -t test_sample_web_app:local .
```

In order to delete the server image execute the following command:
```bash
docker rmi test_sample_web_app:local
```

## Run the web app

In order to run the web app, start the ``system.yml`` docker-compose environment by running:

```bash
docker-compose -f system.yml up
```

Open any browser and go to **``http://localhost:5000/``**. You will see the entire ``sample project`` running.

After finishing using the web app, to down de docker-compose environment execute:

```bash
docker-compose -f system.yml down
```
