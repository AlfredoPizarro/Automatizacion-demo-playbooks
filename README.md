# Automation and Management
Playbooks usados como demo  en presentación Management and Automation de Red Hat Chile 


# deploy-vm-rhv-multiple
Playbook que permite generar varias vm de forma simultanea, customizando las variables contenidas en el archivo var.yaml. El playbook realiza las siguientes tareas:

- Crear una vm desde template. 
- Envía los parámetros de cloud-init para customización indicando ip, hostname, password, dns y gateway. 
- Registra la vm hacia Red Hat Satellite.

Infraestructura utilizada:
 RHV 4.2
 Red Hat Satellite 6.4
 Template de rhel7 con cloud-init instalado. 


La definición de las nuevas vms se declara como un diccionario dentro del archivo vars.yaml. 
Ej:

```
servers:
  srv1:
   srvname:  ansible-demo1.rhlabs.local
   shortname: ansible-demo1
   memoria: 2GiB
   cpu: 2
   ip_address: 172.20.1.111
   ip_net: 255.255.255.0
   ip_gateway: 172.20.1.1
   ip_nic: eth0
   temp_user: root
   temp_pass: redhat2019
   dns: 172.20.1.83
  srv2:
   srvname: ansible-demo2.rhlabs.local
   shortname: ansible-demo2
   memoria: 2GiB
   cpu: 2
   ip_address: 172.20.1.112
   ip_net: 255.255.255.0
   ip_gateway: 172.20.1.1
   ip_nic: eth0
   temp_user: root
   temp_pass: redhat01
   dns: 172.20.1.83
```

# deploy-vm-rhv-single
Playbook que permite la creación de una vm única. Este playbook es el que integramos con Red Hat Cloudforms y Ansible Tower, el que permite realizar las mismas acciones del playbook anterior pero además permite inyectar la rsa-key de Ansible Tower a la nueva vm.
Infraestructura utilizada:
 RHV 4.2
 Red Hat Satellite 6.4
 Template de rhel7 con cloud-init instalado. 
 Ansible Tower 3.4
 Red Hat Cloudforms 4.6
 

# host-preparation
Playbook que demuestra algunas acciones que normalmente se realizan en un ambiente de operaciones a nuevas vms. Este playbook permite:

- Agregar nuevos usuarios.
- Agregar parámetros de kernel a sysctl.
- Habilitar reglas de firewall vía firewalld.
- En base a un disco adicional, generar un nuevo vg, 3 lvs y realizar el formateo, montaje y modificaciones necesarias a fstab.

Los usuarios, reglas, parámetros y particiones se parametrizan en el archivo vars.yaml:

```
---
#Identifica a los usuarios a crear 
users:
  - appuser
  - operator
  - thanos
#Reglas de firewall que se deben aplicar
rules:
  - http
  - https
  - nfs
  - ldap
#Parametros de kernel especificados en un diccionario
kernel:
   param1:
     nombre: net.ipv4.conf.all.send_redirects
     valor: 0
   param2:
     nombre: net.ipv4.conf.all.log_martians
     valor: 1
   param3:
     nombre: net.ipv4.conf.all.rp_filter
     valor: 1
#Discos adicional para aplicaciones (sin /dev)
disco: sdb
#Memoria minima en MB para aplicar el playbook, si la memoria es menor, no ejecuta  el resto de los pasos
min_memory: 1024
#Tamaño de cada una de las 3 particiones de aplicación en Gigas
lv_data1_size: 1g
lv_data2_size: 1g
lv_data3_size: 1g


