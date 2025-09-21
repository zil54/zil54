#1. Define Environments in puppet.conf
#Modify /etc/puppetlabs/puppet/puppet.conf to specify environments:

[main]
environment = production

[dev]
manifest = /etc/puppetlabs/code/environments/dev/manifests/site.pp
modulepath = /etc/puppetlabs/code/environments/dev/modules

[uat]
manifest = /etc/puppetlabs/code/environments/uat/manifests/site.pp
modulepath = /etc/puppetlabs/code/environments/uat/modules

[prodfix]
manifest = /etc/puppetlabs/code/environments/prodfix/manifests/site.pp
modulepath = /etc/puppetlabs/code/environments/prodfix/modules

[prod]
manifest = /etc/puppetlabs/code/environments/prod/manifests/site.pp
modulepath = /etc/puppetlabs/code/environments/prod/modules

#2  Define Node-Specific Configurations in site.pp
#Inside /etc/puppetlabs/code/environments/dev/manifests/site.pp, define node-specific rules:
node /^dev-.*/ {
  include postgres_setup
}
#3 node /^dev-.*/ {
[agent]
environment = dev

#4 Apply the configuration
puppet agent --test

#This will apply the postgres_setup class only to Dev nodes.
