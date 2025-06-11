#1. Install the Puppet PostgreSQL Module
#The puppetlabs/postgresql module simplifies PostgreSQL management. You can install it using:
puppet module install puppetlabs-postgresql


#2 Define a Puppet Manifest for PostgreSQL
#Create a Puppet manifest (postgresql.pp) to install, configure, and manage PostgreSQL:

class { 'postgresql::server':
  ensure => present,
}

postgresql::server::db { 'my_database':
  user     => 'db_user',
  password => 'securepassword',
}

#3. Automate Upgrades
#To always keep PostgreSQL updated, modify the package resource:
package { 'postgresql-server':
  ensure   => latest,
  provider => 'yum',  # Change based on OS
}

#4. Manage Configuration Files
#Use Puppet to enforce PostgreSQL settings:
file { '/var/lib/pgsql/data/postgresql.conf':
  ensure  => file,
  source  => 'puppet:///modules/postgres/postgresql.conf',
  require => Package['postgresql-server'],
}

#5. High Availability & Failover Strategies
#Overview:
#High availability (HA) means ensuring that your PostgreSQL server remains online even when individual nodes fail.
#With Puppet, you can integrate HA tools (e.g., Patroni) that manage streaming replication, automatic failover, and workload balancing.
#These modules typically allow you to designate a primary server and one or more replicas, and they help manage the necessary configuration
#and dependencies between them.

# Define a role for primary PostgreSQL server with HA configuration
node 'primary.example.com' {
  class { 'postgresql::server':
    ensure         => present,
    config_settings => {
      'wal_level'            => 'replica',
      'max_wal_senders'      => '5',
      'synchronous_commit'   => 'on',
    },
  }

  # Assuming a Patroni-based module is available
  include patroni::primary
}

# Define a role for replica PostgreSQL servers
node /replica\d+\.example\.com/ {
  class { 'postgresql::server':
    ensure         => present,
    config_settings => {
      'wal_level'            => 'replica',
      'max_wal_senders'      => '5',
      'hot_standby'          => 'on',
    },
  }

  include patroni::replica
}

#6. Let's expand on our PostgreSQL deployment management with Puppet by diving into three aspects:

1. High Availability & Failover Strategies
Overview:
High availability (HA) means ensuring that your PostgreSQL server remains online even when individual nodes fail. With Puppet, you can integrate HA tools (e.g., Patroni) that manage streaming replication, automatic failover, and workload balancing. These modules typically allow you to designate a primary server and one or more replicas, and they help manage the necessary configuration and dependencies between them.
Example Manifest:
You might structure your manifests like this, dividing configurations for primary and replica nodes:
# Define a role for primary PostgreSQL server with HA configuration
node 'primary.example.com' {
  class { 'postgresql::server':
    ensure         => present,
    config_settings => {
      'wal_level'            => 'replica',
      'max_wal_senders'      => '5',
      'synchronous_commit'   => 'on',
    },
  }

  # Assuming a Patroni-based module is available
  include patroni::primary
}

# Define a role for replica PostgreSQL servers
node /replica\d+\.example\.com/ {
  class { 'postgresql::server':
    ensure         => present,
    config_settings => {
      'wal_level'            => 'replica',
      'max_wal_senders'      => '5',
      'hot_standby'          => 'on',
    },
  }

  include patroni::replica
}

#In this approach, Puppet assigns different configurations based on the node's
#role while the HA module (like Puppet’s Patroni module) orchestrates cluster replication and synchronized failover.

#6. Backup Automation
#Overview: Automating backups is key to data integrity. You can schedule PostgreSQL backups using Puppet,
#often with modules like deric/pgprobackup. This module leverages tools such as pg_probackup to create consistent,
#scheduled backups and even manage off-site backup locations.

class postgres_backup {
  # Including the pgprobackup module
  include pgprobackup

  # Define backup instance and schedule
  pgprobackup::instance { 'main_instance':
    ensure           => present,
    backup_schedule  => {
      'FULL'  => {
        hour    => '3',
        minute  => '15',
        weekday => ['0'],  # Sundays, for example
      },
      'DELTA' => {
        weekday => ['1-6'],  # All other days for incremental backups
      },
    },
  }

  # Optionally, manage related cron jobs for triggering backups
  pgprobackup::manage_cron { 'backup_cron_job':
    ensure => present,
  }
}

include postgres_backup

#7  Performance Tuning & Monitoring
#Keeping PostgreSQL performant is an ongoing task. You can use Puppet to manage tuning parameters in configuration files, automate adjustments based
#on load and integrate monitoring solutions. For example, you might use the puppetlabs/postgresql module to manage and update settings in postgresql.conf
#based on recommendations (e.g., from tools like PgTune) or observed workload metrics.

class postgres_performance {
  # Ensure the PostgreSQL server is installed with the latest version
  package { 'postgresql-server':
    ensure   => latest,
  }

  # Manage the main configuration file with performance-tuned settings
  file { '/var/lib/pgsql/data/postgresql.conf':
    ensure  => file,
    source  => 'puppet:///modules/postgres/performance.conf',
    notify  => Service['postgresql'],
  }

  # Make sure the PostgreSQL service reloads the new configuration
  service { 'postgresql':
    ensure => running,
    enable => true,
    subscribe => File['/var/lib/pgsql/data/postgresql.conf'],
  }

  # (Optional) Include custom facts or external modules to collect performance metrics
  # that feed into automated tuning processes.
}

include postgres_performance
