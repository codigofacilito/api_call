# Setup
python3 -m venv env 

source env/bin/activate (Unix)
Source venv/Scripts/activate (Windows)

pip install -r requirements.txt 

# Run Migrations

cd MainProject
python mananage.py migrate

cd..

cd CourseProject
python mananage.py migrate

# Run projects

make run
