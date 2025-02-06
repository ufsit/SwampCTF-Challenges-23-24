#!/bin/bash
set -e

unset ENV

set -r

env() {
	[ "$___var" ] || echo "We take our security seriously. Employee records are not accessible." >&2
	___var=1
	kill -9 $$
}

unset() {
	[ "$___var" ] || echo "We take our security seriously." >&2
	___var=1
	kill -9 $$
}

cat <<EOF
/-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\\
|                                       |
|  SwampCo Employee Evaluation Script™  |
|                                       |
|  Using a new, robust, and blazingly   |
|  fast BASH workflow, lookup of your   |
|  best employee score is easier than   |
|  ever--all from the safe comfort of   |
|     a familiar shell environment      |
|                                       |
\\-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-/

EOF

echo "To start, enter the employee's name..."
read -r name
eval "
if [ -n \"\${employee_${name}_score}\" ]; then
	echo \"Employee "'${name}'" score: \$employee_${name}_score\"
else
	echo \"Employee not found. Please consult your records.\"
fi
"
