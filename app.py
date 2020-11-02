import query_on_whoosh
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

@app.route("/")
def handle_slash():
    user_name = request.args.get("name")
    return render_template("index.html", name=user_name)

@app.route("/query/")
def handle_query():
    search_term = request.args.get("q")
    page_num = int(request.args.get("p"))
    search_results, num_hits,num_pages=query_on_whoosh.query(search_term, search_page, 10)
    return jsonify({"query_term":search_term, "num_hits":num_hits, "num_pages": num_pages, "search_results":search_results})