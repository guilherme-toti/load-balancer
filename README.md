# Simple Load Balancer
This is a very simple load balancer with Vagrant + NGINX + Tornado + MySQL

# How to use
1. Clone this repository into some folder
2. Open console, go to this folder and type `vagrant up`

After that you need to SSH every machine and:

1. In console: `cd /vagrant`
2. Then run `python main.py` to start the tornado server
3. Type `exit` to leave SSH


So you can access from `192.168.50.5` and the load balancer will be working! ;)
The machines balanced is on ip range `192.168.50.{1,3}0`.

# MySQL
The MySQL machine is serving on ip `192.168.50.100` with one database called `app_db`, user `remoto` and password `123`.

# To-do's
1. Create another vm for REDIS
2. Install `supervisor` in vms
3. Configure supervisor in all vms
4. Develop the API
5. Develop the application
