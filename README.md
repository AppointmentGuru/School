# School

![logo](https://raw.githubusercontent.com/AppointmentGuru/School/master/logo.png)

> It's what you call a swarm in the sea

**NB:** This is a work in progress.

# Setup:

Create the following docker compose:


# Usage and commands:

**Bootstrap your environment**

Will create all the things you need to get started using School

```
docker run --rm appointmentguru/school bootstrap
```

**Create a swarm:**

Will create a swarm in DigitalOcean

```
docker run --rm appointmentguru/school swarmup
```

**Setup a service (Django + Django Rest Framework):**

Creates a standardized RESTful service with Django and Django Rest Framework. This service is immediately deployable to your School.

```
mkdir MyAwesomeMicroService && cd MyAwesomeMicroService
docker run --rm appointmentguru/school serviceprepare
```

**Create a release:**

This will create a release in Github and (optionally) also push a tag to your Docker registry

```
# MyAwesomeMicroService
docker run --rm appointmentguru/school release
```

**Deploy your service:**

Will take your service to School :).

```
# MyAwesomeMicroService
docker run --rm appointmentguru/school deploy
```

## Recommended services:

School works great with these services:

* DigitalOcean
* Docker Cloud
* Kong
* CloudFlare
* Slack
* StatusCake

## Convention:

Given the following variables: 

* organization: **acme**
* canonical_tld: **acme.com**
* service: **UserService**
* entity_name: **user**

**We expect the following to be true:**

> **Note:** You can override any of these configurations. But these are the expectations:

* Github Repo: `acme/UserService`
* Docker Repo: `acme/userservice`

The following will be made for you: 

* Subdomain setup on CloudFlare: userservice.acme.com
* Postgres db + access will be setup:
  * name: `acme_userservice`
  * user: `acme_userservice`
* Deployed to swarm with service named: `userservice`
* Proxied via Kong @: userservice.acme.com -> userservice:80 (internal network)
* StatusCake test: 
  * name: UserService
  * tags: [userservice]
  * url: userservice.acme.com

For more details on configuration, please reference the individual roles.

## Microservices that work:

**Requirements**

* Available on a url 
* Deployed to a swarm - Zero downtime deploys
* Healthcheck 
* Images verified (tested) at build time 
* Deployment commands are grouped in a `run.sh` script
* Deployed by release number 
* Centralized logs 
* Proxied via API gateway
* Connected to database server (if necessary)
  * Data is backed up, replicated, safe and secure
* Required infrastructure contained in compose file (e.g.: workers, brokers etc) 
* ...

**Nice to have**

* Code coverage + code quality metrics over time (Codacy) 
* ..

