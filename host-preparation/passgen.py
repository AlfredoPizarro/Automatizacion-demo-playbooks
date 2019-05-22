#from https://access.redhat.com/solutions/221403
#Permite generar un hash de una password para ser utilizado posteriormente
python -c 'import crypt,getpass; print crypt.crypt(getpass.getpass())'
