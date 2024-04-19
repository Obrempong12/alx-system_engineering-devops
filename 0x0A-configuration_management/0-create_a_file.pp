# creates a file
file { 'holberton':
  ensure  => file,
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  permission    => '0744',
  content => 'I love Puppet'
}
