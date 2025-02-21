from flask import Flask, render_template, request, jsonify
from hybrid_recommender import hybrid_recommendations, popularity_recommendations
app = Flask(__name__)

@app.route('/')
def index():
    top10 = popularity_recommendations()
    return render_template('index.html', top10=top10)

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend', methods=['POST', 'GET'])
def getdata():
    if request.method == 'POST':
        title = request.form['title']
        return hybrid_recommendations(title)
    else:
        return 'This endpoint only accepts POST requests'



if __name__ == '__main__':
    app.run(debug=True)
