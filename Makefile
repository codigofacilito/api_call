run:
	cd MainProject && python manage.py runserver 8000 &
	cd CourseProject && python manage.py runserver 8001 &
	wait