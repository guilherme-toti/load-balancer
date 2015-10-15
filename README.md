# Simple Load Balancer
This is a very simple load balancer with Vagrant + NGINX + Tornado + MySQL + REDIS

# How to use
1. Clone this repository into some folder
2. Open console, go to this folder and type `vagrant up`

# What will `vagrant up` do?
After you write `vagrant up` you will have **5** virtual machines:
#####- Name: vm_master | IP: 192.168.50.5
The Master VM, who is going to do the load balance
This vm will do:
- Update apt cache
- Install and Configure NGINX

#####- Name: vm_1 | IP: 192.168.50.10
This vms will do:
- Update apt cache
- Install and Configure NGINX
- Install PIP and the project dependences
- Install VirtualEnv and create a new VirtualEnv called `venv` into `/vagrant`
- Install and Configure Supervisor

#####- Name: vm_2 | IP: 192.168.50.20
This vms will do:
- Update apt cache
- Install and Configure NGINX
- Install PIP and the project dependences
- Install VirtualEnv and create a new VirtualEnv called `venv` into `/vagrant`
    - Install and Configure Supervisor

#####- Name: vm_3 | IP: 192.168.50.30
This vms will do:
- Update apt cache
- Install and Configure NGINX
- Install PIP and the project dependences
- Install VirtualEnv and create a new VirtualEnv called `venv` into `/vagrant`
- Install and Configure Supervisor

#####- Name: vm_mysql | IP: 192.168.50.100
This vm will do:
- Update apt cache
- Install PIP
- Install MySQL
    - Create the database: `app_db`
    - Create the user: `remoto` with password: `123`
    - Grant all permissions to user `remoto` to the database `app_db`

#####- Name: vm_redis | IP: 192.168.50.200
This vm will do:
- Update apt cache
- Install REDIS

# Load Balancer
The machine responsible for the load balancer is serving on ip `192.168.50.5`.
After the `vagrant up` you can access to `http://192.168.50.5` and see the magic ;)

# MySQL
The MySQL machine is serving on ip `192.168.50.100` with one database called `app_db`, user `remoto` and password `123`.

# REDIS
The REDIS machine is serving on ip `192.168.50.200` in default port: `6379`

# To-do's
1. ~~Create another vm for REDIS~~
2. ~~Install `supervisor` in vms~~
3. ~~Configure supervisor in all vms~~
4. Develop the API
5. Develop the application
