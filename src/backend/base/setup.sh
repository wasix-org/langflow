#!/bin/sh
set -ex

export BACKEND_DIR="$(pwd)"

cd ../../frontend
npm install
npm run build

cd "$BACKEND_DIR"
uvx pip install -r wasmer-requirements.txt --target wasix-site-packages --platform wasix_wasm32 --only-binary=:all: --python-version=3.13 --no-deps
cp ../../lfx/src/lfx wasix-site-packages/lfx -rT

echo 'Now you can execute "wasmer-dev run --net ."'
