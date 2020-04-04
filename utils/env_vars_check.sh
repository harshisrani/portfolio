
# Sensitive variables to be defined on local host, eg. ~/.bash_profile
# and in the Travis CI Configuration Build

if [[ -z $DOCKER_PASSWORD ]]; then
    echo "DOCKER_PASSWORD environment variable required to run"
    exit 1
fi
if [[ -z $AWS_ACCESS_KEY ]]; then
    echo "AWS_ACCESS_KEY environment variable required to run"
    exit 1
fi
if [[ -z $AWS_SECRET_KEY ]]; then
    echo "AWS_SECRET_KEY environment variable required to run"
    exit 1
fi
if [[ -z $ANSIBLE_VAULT_PASSWORD ]]; then
    echo "ANSIBLE_VAULT_PASSWORD environment variable required to run"
    exit 1
fi
if [[ -z $ANSIBLE_SSH_PASSWORD ]]; then
    echo "ANSIBLE_SSH_PASSWORD environment variable required to run"
    exit 1
fi
if [[ -z $ANSIBLE_NOTIFICATION_EMAIL_PASSWORD ]]; then
    echo "ANSIBLE_NOTIFICATION_EMAIL_PASSWORD environment variable required to run"
    exit 1
fi