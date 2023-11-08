# automatically fix word press on apache server runing on 5000 error


exec { 'Fix server error':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
