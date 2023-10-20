echo "Building the Project..."
python3.9 -m pip install -r requirements.txt

echo "Make Migrations..."
python3.9 -m manage.py makemigrations --noinput
python3.9 -m manage.py migrate --noinput

echo "Collect Static..."
python3.9 -m manage.py collectstatic --noinput --clear
