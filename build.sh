echo "Building the Project..."
python3.9 -m pip install -r requirements.txt

echo "Make Migrations..."
python3.9 -m manage makemigrations --noinput
python3.9 -m manage migrate --noinput

echo "Collect Static..."
python3.9 -m manage collectstatic --noinput --clear