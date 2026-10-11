from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pymysql

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Chenna123",
        database="electronic_db",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"message": "Welcome to Electronic Essentials "}
    )

@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT product_no, product_name, price FROM Electronic_products"
            )
            product_list = cursor.fetchall()
    finally:
        connection.close()

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": product_list}
    )
@app.post("/login", response_class=HTMLResponse)
def login(
    req: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    print(username, password)

    product_list = [
        {"product_no": 1, "product_name": "Realme Buds", "price": 1899 },
        {"product_no": 2, "product_name": "Smart Speaker", "price": 4990}
    ]

    return templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products": product_list}
    )