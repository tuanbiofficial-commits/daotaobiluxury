#!/bin/bash
export PATH="${NVM_DIR}/versions/node/v${NODE_VERSION_DEVELOP}/bin/:${PATH}"

if [ ! -d "/home/frappe/frappe-bench/apps/frappe" ]; then
    echo "==> Bench not ready yet. Setup still running or failed."
    echo "    Check: bash /workspace/.devcontainer/setup.sh"
    exit 0
fi

cd /home/frappe/frappe-bench

if pgrep -f "bench start" > /dev/null; then
    echo "==> Bench already running. Logs: tail -f /tmp/bench.log"
    exit 0
fi

echo "==> Starting bench in background..."
nohup bench start > /tmp/bench.log 2>&1 &
sleep 3
echo "==> Bench started. Wait ~30s for the server to be ready on port 8000."
echo "    Logs: tail -f /tmp/bench.log"
echo "    Login: Administrator / admin"
