from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def show_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    
    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results

    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id Where dojos.id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        
        dojo = cls(results[0])

        if results[0]['ninjas.id'] != None:

            for row in results:
                ninja_data ={
                    "id" : row['ninjas.id'],
                    "first_name" : row['first_name'],
                    "last_name" : row['last_name'],
                    "age" : row['age'],
                    "dojo_id" : row['dojo_id'],
                    "created_at" : row['ninjas.created_at'],
                    "updated_at" : row['ninjas.updated_at'],
                    }

                dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo
