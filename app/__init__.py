from flask import Flask
from app.routes.uf_route import uf_api
from flasgger import Swagger

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>UF API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f2f2f2;
        }

        h1 {
            font-size: 24px;
            color: #333;
            margin-bottom: 10px;
        }

        p {
            font-size: 16px;
            color: #666;
            margin-bottom: 5px;
        }

        ul {
            list-style-type: none;
            margin-left: 20px;
            padding-left: 0;
        }

        li {
            font-size: 14px;
            color: #333;
            margin-bottom: 5px;
        }

        a {
            text-decoration: none;
            color: #007bff;
        }

        a:hover {
            text-decoration: underline;
        }

        .example-container {
            background-color: #fff;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }

        .example-code {
            font-family: Consolas, monospace;
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>UF API</h1>
    <p>Available routes:</p>
    <ul>
        <li><a href="/api/v1/uf/30-05-2022">/api/v1/uf/&lt;date&gt;</a></li>
    </ul>
    <p>Available methods:</p>
    <ul>
        <li>GET</li>
    </ul>
    <p>Available date format:</p>
    <ul>
        <li>DD-MM-YYYY</li>
    </ul>
    
    <div class="example-container">
        <p>Example:</p>
        <ul>
            <li><a href="/api/v1/uf/30-05-2022">api/v1/uf/01-01-2020</a></li>
        </ul>
        <p>Response:</p>
        <div class="example-code">
            <pre>{
  "data": "32.664,89",
  "message": "UF value",
  "success": true
}</pre>
        </div>
    </div>
    
    <h2>Documentation and Source code</h2>
    <p>⭐ If you like it leave me a little star on my github please ⭐</p>
    <p><a href="https://github.com/MartinAAcebeyL/ApiUnidadFomento" target="_blank">Documentation/repository</a></p>
    <p>Author: Martín Acebey L.</p>
    <p><a href="https://www.linkedin.com/in/martin-acebey-l/" target="_blank">LinkedIn</a></p>
</body>
</html>
"""
def create_app(config):
    app = Flask(__name__)
    swagger = Swagger()
    app.register_blueprint(uf_api)
    app.config.from_object(config)
    app.app_context().push()
    swagger.init_app(app)
    app.route('/')(lambda: HTML)
    return app
