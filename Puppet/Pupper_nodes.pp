#In Puppet, a node refers to any system or machine that is managed by Puppet. Nodes can be physical servers, virtual machines,
#or cloud instances, and they receive configurations from a Puppet primary server (formerly called the master).
#Key Aspects of a Node in Puppet
#- Identified by a certname (usually its fully qualified domain name).
#- Receives a catalog from the Puppet primary server, which defines its desired state.
#- Can be classified using node definitions in site.pp or an External Node Classifier (ENC).
#- Uses Facter to provide system details that help tailor configurations

node 'webserver.example.com' {
  include apache
}

#This ensures that only webserver.example.com gets the apache class applied.

