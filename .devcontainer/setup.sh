#!/bin/bash
set -e

export PATH="${NVM_DIR}/versions/node/v${NODE_VERSION_DEVELOP}/bin/:${PATH}"

cd /home/frappe

if [ -d "/home/frappe/frappe-bench/apps/frappe" ]; then
    echo "==> Bench already exists, skipping setup."
    exit 0
fi

echo "==> First-time setup — this takes 5-10 minutes..."

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

echo "==> Linking LMS app from mounted fork..."
rm -rf apps/lms
ln -sfn /workspace apps/lms
./env/bin/pip install -e apps/lms
if ! grep -qx "lms" sites/apps.txt 2>/dev/null; then
    echo "lms" >> sites/apps.txt
fi

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
echo "  Setup done! Restart the codespace or run:"
echo "  bash /workspace/.devcontainer/start.sh"
echo "  Login: Administrator / admin"
echo "===================================================="
