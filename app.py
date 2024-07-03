from flask import Flask, request, jsonify, render_template
from scraper.group_claims import group_claims_by_lda
from scraper.extract import get_claims_from_urls

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/group", methods=["GET"])
def group():
    num_topics = int(request.args.get("groups", 3))
    urls = [
        "https://patents.google.com/patent/GB2478972A/en?q=(phone)&oq=phone",
        "https://patents.google.com/patent/US9634864B2/en?oq=US9634864B2",
        "https://patents.google.com/patent/US9980046B2/en?oq=US9980046B2",
    ]
    claims = get_claims_from_urls(urls)

    grouped_claims, topic_words = group_claims_by_lda(claims, num_topics=num_topics)

    response = {"groups": []}
    for i, (group, topic) in enumerate(zip(grouped_claims, topic_words)):
        response["groups"].append({"title": topic, "number_of_claims": len(group)})

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
