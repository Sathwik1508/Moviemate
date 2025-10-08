# Movie_application
MovieFinder
MovieFinder is a simple web application built with Flask that allows users to search for movies using the OMDb API and manage a personal, in-memory watchlist.

Features
Movie Search: Search for movies by title using the OMDb API.
Detailed Results: Displays movie title, poster, IMDb rating, year, and a plot summary for each result.
Watchlist Management: Users can add movies from the search results to a temporary watchlist using an AJAX call.
Front-end: Uses Bootstrap 5.3 for responsive styling and layout.
Requirements
To run this application, you need to have Python 3 installed.

The required Python dependencies are listed in requirements.txt:

Flask
requests
Jinja2
bootstrap-flask
Setup and Installation
Clone the repository (or download the files):

git clone [repository-url]
cd MovieFinder
Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

pip install -r requirements.txt
API Key Configuration: The application is configured to use the OMDb API with the key '605797f8'. While this key might work for testing, you may need to register for your own free OMDb API key and update the OMDB_API_KEY variable in app.py if the included key stops working or hits rate limits.

Running the Application
Ensure your virtual environment is active.

Run the Flask application:

python app.py
The application is set to run in debug mode.

Access the application: Open your web browser and navigate to:

http://127.0.0.1:5000/
<img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/b19814a4-b4c3-4e48-8208-d4a1319e536d" />
image Here We can Search For Movies Example Iam Searching Avengers It gave me Certain list of movies image
<img width="940" height="423" alt="image" src="https://github.com/user-attachments/assets/51416f6f-b03c-49bc-bde2-df411a06128c" />
After Seeing The Results We Can add the movies based on our choices We Can Add The movies to Watchlist image
<img width="940" height="415" alt="image" src="https://github.com/user-attachments/assets/7259f2b9-8060-47db-9e48-3aadb79513f8" />
Now We Can check Our Watchlist
<img width="940" height="327" alt="image" src="https://github.com/user-attachments/assets/bce3f21d-38c8-4e46-8fbe-8ff6bf187a40" />
image We Can update our Watchlist with More Movies
<img width="940" height="594" alt="image" src="https://github.com/user-attachments/assets/b5655a25-a932-4725-8aa2-220c8f897b7c" />


Important Notes
Watchlist Storage: The watchlist is stored in a simple, in-memory Python list (watchlist = []). Any movies added to the watchlist will be lost when the Flask server is stopped or restarted.
Search Logic: When a user searches for a movie, the /search route first calls the OMDb API to get a list of results, and then makes a second, separate API call for each result to fetch the detailed plot summary, rating, and year data.
No Poster Handling: If a movie result is missing a poster URL, the results.html and watchlist.html templates are set up to try and load a fallback image at /static/no-poster.png using the onerror attribute.
