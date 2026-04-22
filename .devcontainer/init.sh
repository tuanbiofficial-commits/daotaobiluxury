#!/bin/bash
set -e

export PATH="${NVM_DIR}/versions/node/v${NODE_VERSION_DEVELOP}/bin/:${PATH}"

cd /home/frappe

if [ -d "/home/frappe/frappe-bench/apps/frappe" ]; then
    echo "==> Bench already exists, starting server..."
    cd frappe-bench
    exec bench start
fi

echo "==> First-time setup: initializing bench (this takes ~5-10 minutes)..."

bench init --skip-redis-config-generation frappe-bench

cd frappe-bench

bench set-mariadb-host mariadb
bench set-redis-cache-host redis://redis:6379
bench set-redis-queue-host redis://redis:6379
bench set-redis-socketio-host redis://redis:6379

sed -i '/redis/d' ./Procfile
sed -i '/watch/d' ./Procfile

echo "==> Installing payments app..."
bench get-app payments

echo "==> Installing LMS app from mounted workspace (your fork)..."
bench get-app /workspace

echo "==> Creating site lms.localhost..."
bench new-site lms.localhost \
  --force \
  --mariadb-root-password 123 \
  --admin-password admin \
  --no-mariadb-socket

bench --site lms.localhost install-app payments
bench --site lms.localhost install-app lms
bench --site lms.localhost set-config developer_mode 1
bench --site lms.localhost set-config allow_tests 1
bench --site lms.localhost clear-cache
bench use lms.localhost

echo ""
echo "===================================================="
echo "  Setup done! Login: Administrator / admin"
echo "  URL: http://localhost:8000"
echo "===================================================="
echo ""

exec bench start
