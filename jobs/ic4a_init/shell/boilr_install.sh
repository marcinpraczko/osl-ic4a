#!/bin/bash

# This is very basic installation of boilr, this script should be replaced
# with a bit of better solution. However is sufficient for start

# TODO: Add new header based on template
# TODO: Add option for verbose messages

set -e

SHELL="/bin/bash"
HOME_IC4A="${HOME}/.ic4a/download"
BOILR_INSTALL_URL="https://raw.githubusercontent.com/tmrts/boilr/master/install"
BOILR_LOCAL_BIN="${HOME_IC4A}/boilr_install.sh"

message() {
    msg="$1"

    echo ""
    echo "[*] ${msg}"
}

# --- MAIN CODE ---
message "Downloading installer from GitHub"
wget -c --show-progress -O ${BOILR_LOCAL_BIN} "${BOILR_INSTALL_URL}"

message "Running installer"
${SHELL} "${BOILR_LOCAL_BIN}"

message "Initialize boilr"
${HOME}/bin/boilr init

message "Boilr installed"
