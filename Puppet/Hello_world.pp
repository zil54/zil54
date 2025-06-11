file { '/tmp/hello_world.txt':
  ensure  => present,
  content => "Hello, World!\n",
}

#To apply this manifest, save it as hello.pp and run:
#puppet apply hello.pp
#This will create the file with the specified content.

#Key Features of Puppet:
#- Configuration Management: Ensures systems remain in a desired state by automating provisioning and updates.
#- Infrastructure as Code (IaC): Allows version control, automated testing, and deployment for better efficiency.
#- Scalability: Manages thousands of servers across different environments.
#- Security & Compliance: Continuously enforces security policies and detects configuration drift.
#- Cross-Platform Compatibility: Works on Windows, Linux, BSD, and other operating systems.
#Puppet is widely used in enterprise environments where maintaining consistent and secure infrastructure is crucial.

#Common Puppet Providers
#| Resource Type | Providers | Description |
#| Package | apt, yum, dnf, portage, gem, pip | Manages software packages using different package managers. |
#| Service | systemd, init, upstart, launchd | Controls services across various init systems. |
#| User | useradd, pw, directoryservice | Manages user accounts on different OS platforms. |
#| Group | groupadd, directoryservice | Handles group management. |
#| File | posix, windows, mount | Manages files, directories, and mounts. |


#Puppet automatically selects the most suitable provider based on the operating system, but you can explicitly define a provider in your manifest:
package { 'nginx':
  ensure   => installed,
  provider => yum,
}


#For a full list of providers, check out the official Puppet documentation. Let me know if you need help choosing the right provider for your setup!
