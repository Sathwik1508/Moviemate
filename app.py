from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your TMDB API key or use static data for demo

# OMDb API setup
OMDB_API_KEY = '605797f8'
OMDB_SEARCH_URL = 'http://www.omdbapi.com/'

# Temporary watchlist storage (in-memory)
watchlist = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    title = request.form.get('title')
    if not title:
        return render_template('index.html', error='Please enter a movie title.')
    # Call OMDb API
    params = {
        'apikey': OMDB_API_KEY,
        's': title
    }
    response = requests.get(OMDB_SEARCH_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get('Search', [])
        # For each result, fetch full details for poster, rating, year, summary
        movies = []
        for item in results:
            imdb_id = item.get('imdbID')
            detail_params = {'apikey': OMDB_API_KEY, 'i': imdb_id}
            detail_resp = requests.get(OMDB_SEARCH_URL, params=detail_params)
            if detail_resp.status_code == 200:
                detail = detail_resp.json()
                movies.append({
                    'title': detail.get('Title'),
                    'poster': detail.get('Poster'),
                    'rating': detail.get('imdbRating'),
                    'year': detail.get('Year'),
                    'summary': detail.get('Plot'),
                    'id': imdb_id
                })
        return render_template('results.html', movies=movies)
    else:
        return render_template('index.html', error='Error fetching data from OMDb.')


@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    movie = request.get_json()
    if movie:
        watchlist.append(movie)
        return jsonify({'success': True, 'message': 'Added to watchlist!'})
    return jsonify({'success': False, 'message': 'Failed to add.'})


@app.route('/watchlist')
def show_watchlist():
    return render_template('watchlist.html', watchlist=watchlist)

if __name__ == '__main__':
    app.run(debug=True)
