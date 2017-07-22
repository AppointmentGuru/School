# School

![logo](https://raw.githubusercontent.com/AppointmentGuru/School/master/logo.png)

> It's what you call a swarm in the sea

**NB:** This is a work in progress.

# Setup:

# Usage and commands:

**Bootstrap your environment**

Will create all the things you need to get started using School

```
mkdir -p MyProject/configs && cd MyProject
docker run -it -v $(pwd)/configs:/code/configs --rm appointmentguru/school:baseline python scripts/bootstrap.py
```

This will create some files at: `./configs/`. Have a look at these and fill out what you can.

You _must_ provide:

* `api_token` in digital_ocean.ini
* at least one `digital_ocean_ssh_key_ids` in secrets.yml
* `digital_ocean_token` in secrets.yml
* `ansible_user` in secrets.yml (this will be your user on your computer (e.g.: `whoami`))

**Create a swarm:**

Will create a swarm in DigitalOcean

```
docker run --rm -it \
	-v ~/.ssh:/root/.ssh \
	-v $(pwd)/configs/settings.yml:/code/ansible/group_vars/all/settings.yml \
	-v $(pwd)/configs/secrets.yml:/code/ansible/group_vars/all/secrets.yml \
	-v $(pwd)/configs/digital_ocean.ini:/etc/ansible/inventory/digital_ocean.ini \
	-e "ANSIBLE_HOST_KEY_CHECKING=False" \
	-e "ANSIBLE_LIBRARY=/etc/ansible/library" \
	appointmentguru/\school:baseline \
	ansible-playbook ansible/provision.swarm.yml -i /etc/ansible/inventory/digital_ocean.py
```

Set up a MicroService infrastructure:

(currently only Nginx -> Kong is supported)

```
docker run --rm -it \
	-v ~/.ssh:/root/.ssh \
	-v $(pwd)/configs/settings.yml:/code/ansible/group_vars/all/settings.yml \
	-v $(pwd)/configs/secrets.yml:/code/ansible/group_vars/all/secrets.yml \
	-v $(pwd)/configs/digital_ocean.ini:/etc/ansible/inventory/digital_ocean.ini \
	-e "ANSIBLE_HOST_KEY_CHECKING=False" \
	-e "ANSIBLE_LIBRARY=/etc/ansible/library" \
	appointmentguru/\school:baseline \
	ansible-playbook ansible/infrastructure.swarm.yml -i /etc/ansible/inventory/digital_ocean.py
```

**Deploy some services:**

The following services are deployable via school:

* logdna
* vizualizer

todo:

* authservice for kong

```
docker run --rm -it \
	-v ~/.ssh:/root/.ssh \
	-v $(pwd)/configs/settings.yml:/code/ansible/group_vars/all/settings.yml \
	-v $(pwd)/configs/secrets.yml:/code/ansible/group_vars/all/secrets.yml \
	-v $(pwd)/configs/digital_ocean.ini:/etc/ansible/inventory/digital_ocean.ini \
	-e "ANSIBLE_HOST_KEY_CHECKING=False" \
	-e "ANSIBLE_LIBRARY=/etc/ansible/library" \
	appointmentguru/\school:baseline \
	ansible-playbook ansible/deploy.service.yml -i /etc/ansible/inventory/digital_ocean.py -e'service=vizualizer'
```

Replace `-e service=..` to deploy different services


**Tools**

**Kong dashboard for Kong is cool:**

```
docker run -d -p 8080:8080 pgbi/kong-dashboard:v2
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

**Current setup required:**

* Create a run script (run.sh)
* Create a school play (school.play.yml)
* Wire together with compose (docker-compose.school.yml)

**Manual steps:**

* Create docker cloud setup


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

