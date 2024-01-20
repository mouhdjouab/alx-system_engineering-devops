# killmenow.pp

exec { 'killmenow_process':
  command     => 'pkill -9 -f killmenow',
}
