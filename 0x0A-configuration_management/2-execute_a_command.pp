# killmenow.pp

exec { 'killmenow_process':
  command     => 'pkill killmenow',
}
