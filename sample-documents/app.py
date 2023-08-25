import os
import rook
from flask import Flask
from flask import render_template, request
from currency_converter import CurrencyConverter
# rook.start() # Rookout token is stored in Secret Manager and is loaded into an Environment Variable (ROOKOUT_TOKEN) during deployment.

app = Flask(__name__)
# region = os.environ.get("region")
region = "eu" # This is used to showcase Rookout


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def my_form_post():
    c = CurrencyConverter()

    euros = request.form["euros"]
    usd = round(c.convert(euros, "EUR", "USD"), 2)
    print("Tailing...Some+++More---1") # Using the distroless Dockerfile will not print this to console
    print("USD value is: ", str(usd))
    print("Region is: ", region)
    # region = os.environ.get("region")
    return render_template("form.html", euros=euros, usd=usd)


if __name__ == "__main__":
    # Run in development server
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    rook.start() # Rookout token is stored in Secret Manager and is loaded into an Environment Variable (ROOKOUT_TOKEN) during deployment.
    
    # Run in production
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))