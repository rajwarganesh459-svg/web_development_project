#!/bin/bash

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Compiling C++ code..."

g++ matcher.cpp -o matcher

echo "Build completed!"