IP="$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')"
echo "Server will start at http://$IP:8000"
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
