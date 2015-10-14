# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  (1..3).each do |i|
    config.vm.define "vm_#{i}" do |worker|
      worker.vm.box = "ubuntu/trusty64"

      # Synced Folders
      worker.vm.synced_folder "./app", "/vagrant"

      # Network Configs
      worker.vm.network "private_network", ip: "192.168.50.#{i}0"
    end
  end

  config.vm.define "vm_master" do |vm_master|
    vm_master.vm.box = "ubuntu/trusty64"

    # Network Configs
    vm_master.vm.network "private_network", ip: "192.168.50.5"
  end

  config.vm.define "vm_mysql" do |vm_mysql|
    vm_mysql.vm.box = "ubuntu/trusty64"

    # Network Configs
    vm_mysql.vm.network "private_network", ip: "192.168.50.100"
  end

  # Provisioning
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.groups = {
      "development" => ["vm_1", "vm_2", "vm_3"],
      "master" => ["vm_master"],
      "mysql" => ["vm_mysql"]
    }
  end
end
