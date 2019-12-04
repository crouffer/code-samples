# AWS CloudFormation Examples

Here are some CFN examples to demonstrate the following:

## Create a VCP with Multiple Subnets and NAT Gateway

### Features

- 2 Public Subnets
- 3 Private Subnets
- Routing Rules
- NAT Gateway
- Tagging built into template

<u>**Template:**</u> vpc.yml



## Add a Bastion Server (aka Jump Box) to the VPC

### Features

- Select instance type
- Tagging built into template

<u>**Template:**</u> bastion_ec2_instance.yml

## Create an ECS Cluster of Spot Instances in the VPC

### Features

- Ability to specify the number of cores needed in the cluster
- Configure the spot-bid per instance type
- Tagging built into template
- ecs-userdata.sh script can be customized to add startup configuration to the cluster instances

<u>**Template:**</u> ecs_spot_fleet_cluster.yml

## Add an ECS Service to the Spot Fleet Cluster

### Features

- Ability add database connection info to the service
- Tagging built into template

<u>**Template:**</u> service.yml

## Create an Aurora RDS Instance in the VPC

### Features

- Select the instance type
- Cross-subdomain (availability group) mirroring
- Tagging built into template

<u>**Template:**</u> aurora_database.yml









