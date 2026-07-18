#!/bin/bash

echo "📥 pushing latest code ..."
git add .
git commit -m "update"
git push

echo "✅ push complete"
sleep 4