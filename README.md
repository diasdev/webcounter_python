# Example Application


## Setup

### Clone this repo

### Import the code into Bunnyshell

### Attach the Terraform Modules

make sure the regions are correct for the subnets

### Configure AWS Credentials

* Ask for an AWS IAM user
* Install the AWS CLI
```
brew install awscli
```
* configure the credentials
* test 
```
aws s3 ls
```

### Install the bunnyshell CLI

Download the correct binary for your system. In this case I saved it to my home directory and created a link to it so it would be globally available. 

```
sudo ln -s ~/bunnyshell /usr/local/bin/bunnyshell-cli
```

### Cluster Access

aws eks get-token --cluster-name aws-cluster-demo-2