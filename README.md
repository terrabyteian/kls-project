# kls-project


### Install Steps

Steps to install:

1. Download this project's .zip on a Linux machine
2. With docker installed, `cd <project_dir>/dockerbuild/`
3. `docker build --no-cache -t driversiti-project:latest .` (This will build an image for this project)
4. `docker run -p 5000:5000 -i -t driversiti-project`

This docker image contains the following:

* The programming assignments under <project_dir>/programming
* The database assignments under <project_dir>/database
* an instance of mongo
* a supervisord conf file that runs mongo

To be able to fully use the assignments, wherever you see a requirements.txt file, you should run `virtualenv virtualenv`,`source virtualenv/bin/activate`,`pip install -r requirements.txt`. 

For the web application, run app.py after setting up your virtualenv. If you navigate that tree you will see the sample files as well as the python script that can randomly generate the files.
