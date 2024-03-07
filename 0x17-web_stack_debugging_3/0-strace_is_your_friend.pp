# Fixes `phpp` to o `php` in `wp-settings.php`.

exec { 'wordpress-fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
