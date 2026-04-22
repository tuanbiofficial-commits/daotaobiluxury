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

# Rewrite apps.txt cleanly — bench's appends don't always leave a trailing newline,
# which can merge app names into invalid module names like "paymentslms".
printf "frappe\npayments\nlms\n" > sites/apps.txt

echo "==> Creating site lms.localhost..."
bench new-site lms.localhost \
    --force \
    --mariadb-root-username root \
    --mariadb-root-password 123 \
    --admin-password admin \
    --mariadb-user-host-login-scope='%'

bench --site lms.localhost install-app payments
bench --site lms.localhost install-app lms
bench --site lms.localhost set-config developer_mode 1
bench --site lms.localhost set-config allow_tests 1
bench --site lms.localhost clear-cache
bench use lms.localhost

echo "==> Setting up /sites compatibility symlink for Vue frontend build..."
# The socket.js in frontend uses ../../../../sites/common_site_config.json which
# resolves to /sites when apps/lms is a symlink to /workspace — create that path.
sudo ln -sfn /home/frappe/frappe-bench/sites /sites || true

echo "==> Building Vue frontend (yarn install + build, ~3-5 min)..."
cd /workspace/frontend
yarn install
yarn build
cd /home/frappe/frappe-bench

echo ""
echo "===================================================="
echo "  Setup done! Restart the codespace or run:"
echo "  bash /workspace/.devcontainer/start.sh"
echo "  Login: Administrator / admin"
echo "===================================================="
