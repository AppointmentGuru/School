# School

![logo](https://raw.githubusercontent.com/AppointmentGuru/School/master/logo.png)

> It's what you call a swarm in the sea

**NB:** This is a work in progress.

_School_ is a collection of Ansible playbooks and docker-compose files designed to bootstrap an environment which will make development and deployment super easy.

Out the box you will get:

* A `n` node swarm in Digital Ocean (we may add other backends later).
* A Postgres cluster (1 master, 1 slave) running in the swarm.
* Kong API gateway
* ..


## Usage

In any directory, create the following docker-compose file:

```
version: '3'
services:
  image: appointmentguru/school:latest
  volumes: .:/code/swarm/custom
```

### Initialization:

```
docker-compose up -d
```

Will:

* As you a few questions
* Create a swarm of the size you specify on DigitalOcean (using the credentials you specify)
* Each node will be hardened/secured


**Recommendation:**

Add: `alias web="docker-compose run --rm school"` to `~/.bash_profile`, now you can run commands inside your container with:

```
school {command}
```

Further commands:

#### school service

* add
* remove

**Example:**

```
school service add postgres
school service add kong
school service add redis
```

#### school app

* `prepare` - create a docker-compose file for
* `deploy`
* `remove`

**Example:**

```
school app prepare {app_name} {app_version}
# example:
school app prepare mysupercoolapp v1.2.3
```

Will create a compose file based on a template you provide, ready to deploy the appropriate version of your app


```
school app deploy mysupercoolapp v1.2.3
```

* Will deploy the app above

We also provide: `school app release`

which will generate a release for your app. Where a release may container one or more of these functions:

* build, tag and push a container to docker hub/cloud
* Create a release in github
* create a release in sentry
* create a release in pivotaltracker


