# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "fedora/26-cloud-base"

  # Forward traffic on the host to the development server on the guest
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  if Vagrant.has_plugin?("vagrant-hostmanager")
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
  end

  # Vagrant can share the source directory using rsync, NFS, or SSHFS (with the
  # vagrant-sshfs plugin). By default, it rsyncs the current directory to
  # /vagrant. We disable this in favor of SSHFS.
  #
  # If you would to use NGS to share the directory, uncomment this and
  # configure NFS.
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/srv/pycon", type: "sshfs", sshfs_opts_append: "-o nonempty"

  config.vm.provision "shell", inline: "sudo dnf upgrade -y"

  # Install packages required for Ansible and configure everything with ansible
  config.vm.provision "shell", inline: "sudo dnf -y install python2-dnf libselinux-python"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbooks/production.yml"
  end

 # Create the "pycon" box
 config.vm.define "pycon" do |pycon|
    pycon.vm.host_name = "pyconpune.example.com"

    pycon.vm.provider :libvirt do |domain|
        # Season to taste
        domain.cpus = 4
        domain.graphics_type = "spice"
        domain.memory = 2048
        domain.video_type = "qxl"

        # Uncomment the following line if you would like to enable libvirt's unsafe cache
        # mode. It is called unsafe for a reason, as it causes the virtual host to ignore all
        # fsync() calls from the guest. Only do this if you are comfortable with the possibility of
        # your development guest becoming corrupted (in which case you should only need to do a
        # vagrant destroy and vagrant up to get a new one).
        #
        #domain.volume_cache = "unsafe"
    end
  end
end
