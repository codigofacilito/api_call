python3 -m venv env 

source env/bin/activate (Unix)
Source venv/Scripts/activate (Windows)

pip install -r requirements.txt 


cd MainProject
python mananage.py migrate

cd..

cd CourseProject
python mananage.py migrate