#!/bin/bash

ENV_NAME=""

if [ -z "$BUNNYSHELL_API_TOKEN" ]
then
    echo -e "Please set the BUNNYSHELL_API_TOKEN"
    exit 1;
fi

if [ -z "$ENV_NAME" ]
then
    read -p $'\033[0;33mEnvironment name: \033[00m' ENV_NAME;
fi

  echo -e "creating environment: $ENV_NAME"

aws rds create-db-instance \
    # --engine sqlserver-se \
    # --engine sqlserver-se \
    # --engine mysql \
    --engine postgres
    --db-instance-identifier bunny-demo-db \
    --allocated-storage 10 \
    --db-instance-class db.t2.micro \
    --vpc-security-group-ids bunny-demo-sg \
    --db-subnet-group bunny-demo-sn \
    --master-username bunny-demo-username \
    --master-user-password bunny-demo-password \
    --backup-retention-period 1