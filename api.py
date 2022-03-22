import db_com

from flask import Flask, request, jsonify

api_server = Flask(__name__)
api_server.secret_key = "super_secret_key"


@api_server.route("/add_product", methods=["POST"])
def add_product():
    if request.method == "POST":
        if "ean" not in request.json:
            resp = jsonify({"message": "bad_request"})
            resp.status_code = 200
            return resp
        if "name" not in request.json:
            resp = jsonify({"message": "bad_request"})
            resp.status_code = 200
            return resp
        if "bin" not in request.json:
            resp = jsonify({"message": "bad_request"})
            resp.status_code = 200
            return resp
        db_com.insert_product(request.json["ean"], request.json["name"], request.json["bin"])
        resp = jsonify({"message": "added"})
        resp.status_code = 200
        return resp


@api_server.route("/")
def test():
    return "działa"


@api_server.route("/check_product", methods=["POST"])
def check_product():
    if request.method == "POST":
        if "ean" not in request.json:
            resp = jsonify({"message": "bad_request"})
            resp.status_code = 200
            return resp
        result = db_com.get_product(request.json["ean"])
        if len(result) == 0:
            resp = jsonify({"message": "no_product"})
            resp.status_code = 200
            return resp
        result = f"[('{result[0][0]}', '{result[0][1]}', '{result[0][2]}')]"
        resp = jsonify({"message": "all_ok", "values": result})
        resp.status_code = 200
        return resp


def run_server():
    # zmieniac ip na adres kompa
    api_server.run(debug=True, host="192.168.0.7", use_reloader=False)
