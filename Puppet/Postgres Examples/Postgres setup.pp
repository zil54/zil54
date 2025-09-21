class postgres_setup {
  package { 'postgresql-server':
    ensure   => latest,  # Installs or upgrades to the latest version
    provider => 'yum',   # Change provider based on OS (e.g., 'apt' for Debian)
  }

  service { 'postgresql':
    ensure => running,
    enable => true,
    require => Package['postgresql-server'],
  }

  file { '/var/lib/pgsql/data/postgresql.conf':
    ensure  => file,
    source  => 'puppet:///modules/postgres/postgresql.conf',
    require => Package['postgresql-server'],
  }
}

include postgres_setup