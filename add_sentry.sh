usage() { echo "Usage: $0 -i ilogin -f FirstName -l LastName " 1>&2; exit 1; }

while getopts ":i:f:l:" o; do
    case "${o}" in
        i)
            i=${OPTARG}
             ;;
        f)
            f=${OPTARG}
            ;;
        l)
            l=${OPTARG}
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${i}" ] || [ -z "${f}" ] || [ -z "${l}" ]; then
    usage
fi

echo "ilogin = ${i}"
echo "firstName = ${f}"
echo "lastName = ${l}"

sqlite3 DjangoPython/db_Dev.sqlite3 "insert into main_sentrymodel (login, first_name, last_name, feature, access_mode) values ('${i}','${f}','${l}','\ADMINISTRATOR','I')"

echo "Records in Sentry for ${i}"

sqlite3 DjangoPython/db_Dev.sqlite3 "select login, first_name, last_name, feature, access_mode from main_sentrymodel where login = '${i}'"

