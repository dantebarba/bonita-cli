#!/bin/sh
set -e

# Prepend "bonita" if the first argument is not an executable
if ! type -- "$1" &> /dev/null; then
	set -- bonita "$@"
fi

exec "$@"
