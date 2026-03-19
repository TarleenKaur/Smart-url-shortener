# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "URL Shortener is running!"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         long_url = request.form["long_url"]
#         return f"You entered: {long_url}"

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import random
# import string

# app = Flask(__name__)

# # temporary storage
# url_database = {}

# def generate_short_code(length=6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))

# @app.route("/", methods=["GET", "POST"])
# def home():
#     short_url = None

#     if request.method == "POST":
#         long_url = request.form["long_url"]

#         short_code = generate_short_code()
#         url_database[short_code] = long_url

#         short_url = f"http://127.0.0.1:5000/{short_code}"

#     return render_template("index.html", short_url=short_url)

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect
# # import random
# # import string
# from flask_sqlalchemy import SQLAlchemy
# import random
# import string

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# url_database = {}

# # class URL(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     original_url = db.Column(db.String(500), nullable=False)
# #     short_code = db.Column(db.String(10), unique=True, nullable=False)
# class URL(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     original_url = db.Column(db.String(500), nullable=False)
#     short_code = db.Column(db.String(10), unique=True, nullable=False)
#     clicks = db.Column(db.Integer, default=0)

# def generate_short_code(length=6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))

# @app.route("/", methods=["GET", "POST"])
# def home():
#     short_url = None

#     if request.method == "POST":
#         long_url = request.form["long_url"]

#         short_code = generate_short_code()
#         # url_database[short_code] = long_url
#         new_url = URL(original_url=long_url, short_code=short_code)
#         db.session.add(new_url)
#         db.session.commit()

#         short_url = f"http://127.0.0.1:5000/{short_code}"

#     return render_template("index.html", short_url=short_url)

# @app.route("/<short_code>")
# def redirect_to_url(short_code):
#     # long_url = url_database.get(short_code)
#     url = URL.query.filter_by(short_code=short_code).first()

#     # if long_url:
#         # return redirect(long_url)
#     # if url:
#     #     return redirect(url.original_url)
#     if url:
#         url.clicks += 1
#         db.session.commit()

#         return redirect(url.original_url)

#     return "URL not found"
    
#     # else:
#     # return "URL not found"

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# import random
# import string

# app = Flask(__name__)

# # Database configuration
# # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"

# import os

# database_url = os.environ.get("DATABASE_URL")

# if database_url and database_url.startswith("postgres://"):
#     database_url = database_url.replace("postgres://", "postgresql://", 1)

# if not database_url:
#     database_url = "sqlite:///urls.db"

# app.config["SQLALCHEMY_DATABASE_URI"] = database_url
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# with app.app_context():
#     # db.create_all()

# # import os

# # database_url = os.environ.get("DATABASE_URL")

# # # Fix Render PostgreSQL URL issue (VERY IMPORTANT)
# # if database_url and database_url.startswith("postgres://"):
# #     database_url = database_url.replace("postgres://", "postgresql://", 1)

# # app.config["SQLALCHEMY_DATABASE_URI"] = database_url
# # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# # db = SQLAlchemy(app)


# # Database Model
# class URL(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     original_url = db.Column(db.String(500), nullable=False)
#     short_code = db.Column(db.String(10), unique=True, nullable=False)
#     clicks = db.Column(db.Integer, default=0)

# with app.app_context():
#     db.create_all()


# # Function to generate short codes
# def generate_short_code(length=6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))


# # Home route
# # @app.route("/", methods=["GET", "POST"])
# # def home():

# #     if request.method == "POST":

# #         long_url = request.form["long_url"]

# #         short_code = generate_short_code()

# #         new_url = URL(
# #             original_url=long_url,
# #             short_code=short_code,
# #             clicks=0
# #         )

# #         db.session.add(new_url)
# #         db.session.commit()

# #         short_url = request.host_url + short_code

# #         return render_template(
# #             "index.html",
# #             short_url=short_url,
# #             clicks=0
# #         )

# #     return render_template("index.html")


# @app.route("/", methods=["GET", "POST"])
# def home():

#     if request.method == "POST":

#         long_url = request.form["long_url"]
#         if not long_url.startswith("http://") and not long_url.startswith("https://"):
#             long_url = "https://" + long_url
#         custom_code = request.form.get("custom_code")

#         # If user entered custom alias
#         if custom_code:

#             existing = URL.query.filter_by(short_code=custom_code).first()

#             if existing:
#                 return render_template(
#                     "index.html",
#                     error="Custom name already taken. Try another."
#                 )

#             short_code = custom_code

#         else:
#             short_code = generate_short_code()

#         new_url = URL(
#             original_url=long_url,
#             short_code=short_code,
#             clicks=0
#         )

#         db.session.add(new_url)
#         db.session.commit()

#         short_url = request.host_url + short_code

#         return render_template(
#             "index.html",
#             short_url=short_url,
#             clicks=0
#         )

#     return render_template("index.html")

# # Redirect route
# @app.route("/<short_code>")
# def redirect_to_url(short_code):

#     url = URL.query.filter_by(short_code=short_code).first()

#     if url:

#         url.clicks += 1
#         db.session.commit()

#         return redirect(url.original_url)

#     return "URL not found"


# # if __name__ == "__main__":
# #     app.run(debug=True)

# import os

# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(host="0.0.0.0", port=port)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)

# ✅ Database configuration
database_url = os.environ.get("DATABASE_URL")

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

if not database_url:
    database_url = "sqlite:///urls.db"

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ✅ Model (MUST come before create_all)
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)

# ✅ Create tables (TEMPORARY for first deploy)
with app.app_context():
    db.create_all()


# Function to generate short codes
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Home route
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        long_url = request.form["long_url"]

        if not long_url.startswith("http://") and not long_url.startswith("https://"):
            long_url = "https://" + long_url

        custom_code = request.form.get("custom_code")

        if custom_code:
            existing = URL.query.filter_by(short_code=custom_code).first()

            if existing:
                return render_template(
                    "index.html",
                    error="Custom name already taken. Try another."
                )

            short_code = custom_code
        else:
            short_code = generate_short_code()

        new_url = URL(
            original_url=long_url,
            short_code=short_code,
            clicks=0
        )

        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code

        return render_template(
            "index.html",
            short_url=short_url,
            clicks=new_url.clicks  # ✅ FIXED
        )

    return render_template("index.html")


# Redirect route
@app.route("/<short_code>")
def redirect_to_url(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.original_url)

    return "URL not found"


# Local run only
if __name__ == "__main__":
    app.run(debug=True)