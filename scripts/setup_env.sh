#!/bin/bash

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this script as root"
  exit 1
fi

echo "Updating package lists..."
sudo apt update

echo "Installing required packages..."
sudo apt install -y \
  build-essential \
  libbz2-dev \
  libncurses5-dev \
  libncursesw5-dev \
  libssl-dev \
  libreadline-dev \
  libffi-dev \
  libsqlite3-dev \
  liblzma-dev \
  tk-dev \
  libgdbm-dev \
  libnss3-dev \
  libdb5.3-dev \
  libexpat1-dev \
  libpcap-dev \
  libmpdec-dev \
  libgmp-dev \
  libxext-dev \
  libgl-dev \
  libegl1-mesa-dev \
  libglu1-mesa-dev \
  libxi-dev \
  libxmu-dev \
  libxmu-headers \
  libgmp3-dev \
  bzip2 \
  python3-pip \
  python3-venv

echo "Setting up Python virtual environment..."
python3 -m venv chatbot_env

echo "Activating the virtual environment..."
source chatbot_env/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setup complete. To activate the virtual environment, run 'source chatbot_env/bin/activate'."
