from config import mysql


class DepartmentModel(object):

    @staticmethod
    def get_all_departments() -> list:
        dep_list = []
        # здесь будет извлечение данных и заполнения dep_list
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM departments order by id')
        for row in cursor.fetchall():
            dep_list.append({
                'id': row[0], 'name': row[1]
            })
        return dep_list

    @staticmethod
    def get_depname_by_id() -> str:
        #здесь будет сценарий извлечения имени департамента по его id
        return ''
