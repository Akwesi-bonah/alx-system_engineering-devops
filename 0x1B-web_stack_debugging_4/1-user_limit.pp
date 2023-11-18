# Second task
exec { 'update permissions':
  command  => 'sudo sed -i \'s/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { 'give permissions':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,
}