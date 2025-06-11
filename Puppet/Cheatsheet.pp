#Basic Puppet Syntax
# Declaring a class
class example_class {
  file { '/tmp/example.txt':
    ensure  => present,
    content => "Hello, Puppet!",
  }
}

# Applying a class
include example_class

#Resource Types
# File resource
file { '/etc/example.conf':
  ensure  => file,
  source  => 'puppet:///modules/example/example.conf',
}

# Package resource
package { 'nginx':
  ensure   => installed,
  provider => apt,
}

# Service resource
service { 'nginx':
  ensure => running,
  enable => true,
}

#Variables and Facts
$os_name = $facts['os']['name']
notify { "Operating System: ${os_name}": }

#Conditionals
if $facts['os']['name'] == 'Ubuntu' {
  notify { 'This is an Ubuntu system': }
} else {
  notify { 'This is not Ubuntu': }
}

#Loops
# Iterating over an array
$packages = ['nginx', 'curl', 'vim']
package { $packages:
  ensure => installed,
}

#Templates
# Using an ERB template
file { '/etc/example.conf':
  ensure  => file,
  content => template('example/example.conf.erb'),
}
#
#Here’s a Puppet cheat sheet in table format for quick reference:
#| Category | Syntax Example | Description |
#| Class Definition | class example {} | Defines a reusable class in Puppet. |
#| Including a Class | include example | Applies a class to a node. |
#| File Resource | file { '/etc/example.conf': ensure => file, source => 'puppet:///modules/example/example.conf', } | Manages files on a system. |
#| Package Resource | package { 'nginx': ensure => installed, provider => apt, } | Installs or manages software packages. |
#| Service Resource | service { 'nginx': ensure => running, enable => true, } | Ensures a service is running and enabled. |
#| Variables | $os_name = $facts['os']['name'] | Stores values dynamically. |
#| Conditionals | if $facts['os']['name'] == 'Ubuntu' { notify { 'Ubuntu detected': } } | Executes logic based on conditions. |
#| Loops | $packages = ['nginx', 'curl', 'vim'] package { $packages: ensure => installed, } | Iterates over a list of items. |
#| Templates | file { '/etc/example.conf': content => template('example/example.conf.erb'), } | Uses ERB templates for dynamic content. |
#| Custom Facts | Facter.add(:custom_fact) do setcode { 'value' } end | Defines custom system facts. |

