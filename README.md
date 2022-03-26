# RozhkovPetProject

<h3>Launch</h3>

* Configure virtual environment:
1) sudo apt-get install python3-pip
2) sudo pip3 install virtualenv
3) python3 -m virtualenv ~/Venv/pet_project
4) source ~/Venv/pet_project/bin/activate
5) pip3 install -r requirements.txt
* When cloning project to PyCharm select python configuration from this venv
* git clone https://github.com/anatolyRozhkov/RozhkovPetProject.git
* Configure chromedriver:
1) sudo apt-get install chromium-chromedriver (choose version compatable with your chrome browser)
2) export PATH=$PATH:/path/to/driver/chrome-driver
* Run tests:
1) pytest -m form_page -s -v --env dev
2) pytest -m special -s -v --env dev

<h3>Configuration and rules</h3>

* module tests contains test scripts and page object elements
* name test directories as pages you want to test (ex: login_page)
* each test dir has test scripts (ex: test_login_page.py) and page objects (ex: login_page_elements.py)
* base dir contains file base_elements.py that holds actions to be performed on page objects (ex: login_page.submit_button.perform_click() ) 
* and base_page.py that holds actions to be performed on page itself (ex: login_page.refresh() )
* the root dir has config.py that holds configurations (ex: url and port to be used for testing)
* and conftest.py that holds fixtures for browser setup and parameters (ex: --env)
* pytest.ini contains info needed for PyTest to find files, classes, and functions as well as pytest.mark descriptions
