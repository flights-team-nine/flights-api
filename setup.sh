export DATABASE_USER="root"
export DATABASE_PASS="BoltBolt6126"
export DATABASE_HOST="127.0.0.1"
export DATABASE_PORT="3306"
export DATABASE="honor_flight"
export ADMIN_USERNAME="admin"
export ADMIN_PASSWORD="BoltBolt6126"
export JWT_SECRET="abcde"

gunicorn -w 4 src.main:app