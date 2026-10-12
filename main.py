from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import mysql.connector
from mysql.connector import Error

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chenna123",
            database="electronic_db",
            port=3306
        )
        return connection

    except Error as e:
        print("MySQL connection error:", e)
        return None

def get_products():
    connection = get_db_connection()
    if connection is None:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT product_no, product_name, price FROM Electronic_products"
        )
        product_list = cursor.fetchall()
        cursor.close()
        return product_list
    except Error as e:
        print("Query error:", e)
        return None
    finally:
        connection.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"message": "Welcome to Electronic Essentials"}
    )

@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    product_list = get_products()
    if product_list is None:
        return HTMLResponse(
            content="Unable to connect to the database or fetch products"
        )
    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": product_list}
    )

@app.post("/login", response_class=HTMLResponse)
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    print(username, password)
    product_list = get_products()
    if product_list is None:
        return HTMLResponse(
            content="Unable to connect to the database or fetch products"
        )

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": product_list}
    )