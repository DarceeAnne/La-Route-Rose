# to run:
# python -m flask --app final_project_api run --port 8080
# link to docs:
# http://localhost:8080/docs

from flask import Flask, render_template
from flask_basicauth import BasicAuth
import pymysql
import os
from flask import abort
from flask import request
import json
import math

app = Flask(__name__)
app.config.from_file("final_project_api_config.json", load=json.load)

auth = BasicAuth(app)

from flask_swagger_ui import get_swaggerui_blueprint
from xlwings import App
swaggerui_blueprint = get_swaggerui_blueprint(
    base_url='/docs',
    api_url='/static/openapi.yaml',
)
app.register_blueprint(swaggerui_blueprint)

MAX_PAGE_SIZE = 100

@app.route("/accidents_velo_2019")
@auth.required
def accidents_2019():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)
    departments = request.args.get('departments')
    if departments:
        departments = tuple(map(int, departments.split(',')))
    else:
        departments = (75, 77, 78, 91, 92, 93, 94, 95)

    gender = request.args.get('gender')
    if gender == 'male':
        gender_filter = 1
    elif gender == 'female':
        gender_filter = 2
    else:
        gender_filter = None

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            sql_query = """
                        SELECT * 
                        FROM final_project_ironhack.caracteristiques_2019 c
                        JOIN final_project_ironhack.vehicles_2019 v ON c.Num_Acc = v.Num_Acc
                        JOIN final_project_ironhack.usagers_2019 u ON v.Num_Acc = u.Num_Acc
                        JOIN final_project_ironhack.lieux_2019 l ON l.Num_Acc = u.Num_Acc
                        WHERE catv = 1 AND dep IN %s
                        """
            if gender_filter is not None:
                sql_query += "AND u.sexe = %s "

            sql_query += "LIMIT %s OFFSET %s"

            cursor.execute(sql_query, (departments, gender_filter, page_size, (page-1) * page_size))
            accidents_velo_2019 = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            sql_count_query = "SELECT COUNT(*) AS total FROM accidents_velo_2019 WHERE dep IN %s"
            if gender_filter is not None:
                sql_count_query += "AND sexe = %s"

            cursor.execute(sql_count_query, (departments, gender_filter))
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'accidents': accidents_velo_2019,
        'last_page': f'/accidents_velo_2019?page={last_page}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',
        'next_page': f'/accidents_velo_2019?page={page+1}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',  
    }


@app.route("/accidents_velo_2020")
@auth.required
def accidents_2020():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)
    departments = request.args.get('departments')
    if departments:
        departments = tuple(map(int, departments.split(',')))
    else:
        departments = (75, 77, 78, 91, 92, 93, 94, 95)

    gender = request.args.get('gender')
    if gender == 'male':
        gender_filter = 1
    elif gender == 'female':
        gender_filter = 2
    else:
        gender_filter = None

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            sql_query = """
                        SELECT * 
                        FROM final_project_ironhack.caracteristiques_2020 c
                        JOIN final_project_ironhack.vehicles_2020 v ON c.Num_Acc = v.Num_Acc
                        JOIN final_project_ironhack.usagers_2020 u ON v.Num_Acc = u.Num_Acc
                        JOIN final_project_ironhack.lieux_2020 l ON l.Num_Acc = u.Num_Acc
                        WHERE catv = 1 AND dep IN %s
                        """
            if gender_filter is not None:
                sql_query += "AND u.sexe = %s "

            sql_query += "LIMIT %s OFFSET %s"

            cursor.execute(sql_query, (departments, gender_filter, page_size, (page-1) * page_size))
            accidents_velo_2020 = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            sql_count_query = "SELECT COUNT(*) AS total FROM accidents_velo_2020 WHERE dep IN %s"
            if gender_filter is not None:
                sql_count_query += "AND sexe = %s"

            cursor.execute(sql_count_query, (departments, gender_filter))
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'accidents': accidents_velo_2020,
        'last_page': f'/accidents_velo_2020?page={last_page}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',
        'next_page': f'/accidents_velo_2020?page={page+1}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',  
    }


@app.route("/accidents_velo_2021")
@auth.required
def accidents_2021():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)
    departments = request.args.get('departments')
    if departments:
        departments = tuple(map(int, departments.split(',')))
    else:
        departments = (75, 77, 78, 91, 92, 93, 94, 95)

    gender = request.args.get('gender')
    if gender == 'male':
        gender_filter = 1
    elif gender == 'female':
        gender_filter = 2
    else:
        gender_filter = None

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            sql_query = """
                        SELECT * 
                        FROM final_project_ironhack.caracteristiques_2021 c
                        JOIN final_project_ironhack.vehicles_2021 v ON c.Num_Acc = v.Num_Acc
                        JOIN final_project_ironhack.usagers_2021 u ON v.Num_Acc = u.Num_Acc
                        JOIN final_project_ironhack.lieux_2021 l ON l.Num_Acc = u.Num_Acc
                        WHERE catv = 1 AND dep IN %s
                        """
            if gender_filter is not None:
                sql_query += "AND u.sexe = %s "

            sql_query += "LIMIT %s OFFSET %s"

            cursor.execute(sql_query, (departments, gender_filter, page_size, (page-1) * page_size))
            accidents_velo_2021 = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            sql_count_query = "SELECT COUNT(*) AS total FROM accidents_velo_2021 WHERE dep IN %s"
            if gender_filter is not None:
                sql_count_query += "AND sexe = %s"

            cursor.execute(sql_count_query, (departments, gender_filter))
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'accidents': accidents_velo_2021,
        'last_page': f'/accidents_velo_2021?page={last_page}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',
        'next_page': f'/accidents_velo_2021?page={page+1}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',  
    }


@app.route("/accidents_velo_2022")
@auth.required
def accidents_2022():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)
    departments = request.args.get('departments')
    if departments:
        departments = tuple(map(int, departments.split(',')))
    else:
        departments = (75, 77, 78, 91, 92, 93, 94, 95)

    gender = request.args.get('gender')
    if gender == 'male':
        gender_filter = 1
    elif gender == 'female':
        gender_filter = 2
    else:
        gender_filter = None

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            sql_query = """
                        SELECT * 
                        FROM final_project_ironhack.caracteristiques_2022 c
                        JOIN final_project_ironhack.vehicles_2022 v ON c.Accident_Id = v.Num_Acc
                        JOIN final_project_ironhack.usagers_2022 u ON v.Num_Acc = u.Num_Acc
                        JOIN final_project_ironhack.lieux_2022 l ON l.Num_Acc = u.Num_Acc
                        WHERE catv = 1 AND dep IN %s
                        """
            if gender_filter is not None:
                sql_query += "AND u.sexe = %s "

            sql_query += "LIMIT %s OFFSET %s"

            cursor.execute(sql_query, (departments, gender_filter, page_size, (page-1) * page_size))
            accidents_velo_2022 = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            sql_count_query = "SELECT COUNT(*) AS total FROM accidents_velo_2022 WHERE dep IN %s"
            if gender_filter is not None:
                sql_count_query += "AND sexe = %s"

            cursor.execute(sql_count_query, (departments, gender_filter))
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'accidents': accidents_velo_2022,
        'last_page': f'/accidents_velo_2022?page={last_page}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',
        'next_page': f'/accidents_velo_2022?page={page+1}&page_size={page_size}&departments={",".join(map(str, departments))}&gender={gender}',  
    }

@app.route("/news_english")
@auth.required
def news_english():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM news_data_en_cleaned LIMIT %s OFFSET %s", (page_size, (page-1) * page_size))
            news_english = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM news_data_en_cleaned")
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'news_english': news_english,
        'last_page': f'/news_english?page={last_page}&page_size={page_size}',
        'next_page': f'/news_english?page={page+1}&page_size={page_size}',  
    }

@app.route("/news_french")
@auth.required
def news_french():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM news_data_fr_cleaned LIMIT %s OFFSET %s", (page_size, (page-1) * page_size))
            news_french = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM news_data_fr_cleaned")
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'news_french': news_french,
        'last_page': f'/news_french?page={last_page}&page_size={page_size}',
        'next_page': f'/news_french?page={page+1}&page_size={page_size}',  
    }

@app.route("/mens_bikes_prices")
@auth.required
def mens_bikes_prices():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM bike_info_men LIMIT %s OFFSET %s", (page_size, (page-1) * page_size))
            mens_bikes_prices = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM bike_info_men")
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'mens_bikes_prices': mens_bikes_prices,
        'last_page': f'/mens_bikes_prices?page={last_page}&page_size={page_size}',
        'next_page': f'/mens_bikes_prices?page={page+1}&page_size={page_size}',  
    }

@app.route("/womens_bikes_prices")
@auth.required
def womens_bikes_prices():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)

    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="final_project_ironhack",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM bike_info_women LIMIT %s OFFSET %s", (page_size, (page-1) * page_size))
            womens_bikes_prices = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM bike_info_women")
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'womens_bikes_prices': womens_bikes_prices,
        'last_page': f'/womens_bikes_prices?page={last_page}&page_size={page_size}',
        'next_page': f'/womens_bikes_prices?page={page+1}&page_size={page_size}',  
    }
