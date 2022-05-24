from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re

class Recipe():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_mins = data['under_30_mins']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_recipe(data):

        is_Valid = True

        if len(data['name']) < 3:
            is_Valid = False
            flash("Name of recipe is too short")

        if len(data['description']) < 3:
            is_Valid = False
            flash("The description of recipe is too short")

        if len(data['instructions']) < 3:
            is_Valid = False
            flash("The instructions of recipe is too short")

        if len(data['created_at']) < 1:
            is_Valid = False
            flash("Date must be entered")

        return is_Valid

    @classmethod
    def all_recipes(cls):
        query = "SELECT * FROM recipes;"

        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        for recipe in results:
            recipes.append(Recipe(recipe))

        return recipes

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes(name, description, under_30_mins, instructions, created_at, user_id) VALUE(%(name)s, %(description)s, %(under_30_mins)s, %(instructions)s, %(created_at)s, %(user_id)s);"
        results = connectToMySQL('recipes').query_db(query, data)

        return results

    @classmethod
    def delete_recipe(cls, data):
        query = "Delete From recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return results

    @classmethod
    def view_recipe(cls, data):
        query = "Select * From recipes Where id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return results

    @classmethod
    def edit_recipe(clas, data):
        query = "UPDATE recipes SET name = %(name)s, description= %(description)s, under_30_mins = %(under_30_mins)s, instructions = %(instructions)s, created_at = %(created_at)s WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        return results

