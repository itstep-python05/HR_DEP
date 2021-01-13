from flask import render_template
from config import app
from models.department_model import DepartmentModel


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'departments': DepartmentModel.get_all_departments()
        })