FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN <<EOT
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"
sudo apt update

sudo apt-get update && apt-get upgrade -y
sudo apt-get -y install --no-install-recommends postgresql-client-18
sudo apt-get clean -y && rm -rf /var/lib/apt/lists/*
EOT
