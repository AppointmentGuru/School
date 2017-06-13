# School

![logo](https://raw.githubusercontent.com/AppointmentGuru/School/master/logo.png)

> It's what you call a swarm in the sea

**NB:** This is a work in progress.

# Getting started

**Create a swarm in Digital Ocean:**

```
docker-compose run --rm school python school.py
```

**Deploy a service**

```
ansible-playbook deploy.service.yml -i inventory/digital_ocean.py --limit={manager-node} -e'service=.. version=.. expose_ports=..'
```
