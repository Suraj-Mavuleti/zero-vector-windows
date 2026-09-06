#!/bin/bash
# AUTO-UPDATER
cd /home/suraj/.gemini/antigravity/scratch/zero_suite/zero-vector-windows
git pull origin main --quiet
python3 zero_vector_gui.py
