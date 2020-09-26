set -a
source ./resources/defineColors.sh
set +a

sed_script=$(awk 'BEGIN {FS=","} (NR!=1){ printf("/%s/s/^/%s%s/ ; /%s/s/$/%s/ ; ", $1, ENVIRON[$4"_BACKGROUND"], ENVIRON[$3"_FONT"], $1, ENVIRON["RESET_ALL"]) } ' $2)

sed "$sed_script" $1