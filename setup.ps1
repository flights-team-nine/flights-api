$env:DATABASE_USER = "root"
$env:DATABASE_PASS = "BoltBolt6126"
$env:DATABASE_HOST = "127.0.0.1"
$env:DATABASE_PORT = "3306"
$env:DATABASE = "honor_flight"
$env:ADMIN_USERNAME = "admin"
$env:ADMIN_PASSWORD = "BoltBolt6126"
$env:ADMIN_SALT = "generic_salt"
$env:JWT_SECRET = "abcde"

waitress-serve --port=8000 src.main:app