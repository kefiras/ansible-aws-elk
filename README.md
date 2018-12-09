Ansible-AWS-ELK
=========

Ansible role that spins up multiple instances of Elasticsearch, Logstash and Kibana. It build Elasticsearch cluster automatically based on EC2 tags. It spins up loadbalancers by default for each component and install Elasticsearch plugins: cerebro, head and kopf.

Requirements
------------

- boto library
- AWS secrets set in vars/credentials.yml as per below:
```
aws_access_key_id : "secret-key-id"
aws_secret_access_key : "secret-access-key"
```
- general variables set in defaults/main.yml
```
vpc_subnet_id: "subnet-XXXX"
ami_id: "ami-1e038d71"
region: "eu-central-1"
key_name: "aws-frankfurt"
key_file: "/PATH/TO/YOUR/KEY.pem"
ansible_ssh_private_key_file: "/PATH/TO/YOUR/KEY.pem"
ansible_user: centos
discovery_ec2_endpoint: "ec2.eu-central-1.amazonaws.com"
```


Role Variables
--------------

Main variables are set in defaults/main.yml. 

EC instances and loadbalancers details as per below:
```
# EC deployment stuff
deployment:
  - count: 2
    tag: 'elasticsearch'
    sg_name: 'sg_elasticsearch'
    sg_description: 'rule for ES'
    sg_proto: 'tcp'
    sg_ports: [22, 80, 9000, 9100, 9200, 9300]
    sg_cidr_ip: '0.0.0.0/0' 
  - count: 2
    tag: 'logstash'
    sg_name: 'sg_logstash'
    sg_description: 'rule for Logstash'
    sg_proto: 'tcp'
    sg_ports: [22, 9600, 5044]
    sg_cidr_ip: '0.0.0.0/0' 
  - count: 2
    tag: 'kibana'
    sg_name: 'sg_kibana'
    sg_description: 'rule for Kibana'
    sg_proto: 'tcp'
    sg_ports: [80, 22, 5601]
    sg_cidr_ip: '0.0.0.0/0'

# LB stuff
elasticsearch_lb:
  - protocol: 'http'
    load_balancer_port: 9200
    instance_port: 9200 
logstash_lb:
  - protocol: 'tcp'
    load_balancer_port: 5044
    instance_port: 5044 
kibana_lb:
  - protocol: 'http'
    load_balancer_port: 80
    instance_port: 5601
```

Dependencies
------------


Example Playbook
----------------

ansible-playbook -i localhost, main.yml --ask-vault

License
-------

BSD

Author Information
------------------

Wojciech Wojcik (wojciech.wojcik@cotton-networks.pl)
