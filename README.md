# MovieFinder

MovieFinder is a simple web application built with **Flask** that allows users to search for movies using the **OMDb API** and manage a personal, in-memory watchlist.

-----

## Features

  * **Movie Search:** Search for movies by title using the OMDb API.
  * **Detailed Results:** Displays movie title, poster, IMDb rating, year, and a plot summary for each result.
  * **Watchlist Management:** Users can add movies from the search results to a temporary watchlist using an AJAX call.
  * **Front-end:** Uses **Bootstrap 5.3** for responsive styling and layout.

-----

## Requirements

To run this application, you need to have **Python 3** installed.

The required Python dependencies are listed in `requirements.txt`:

  * `Flask`
  * `requests`
  * `Jinja2`
  * `bootstrap-flask`

-----

## Setup and Installation

1.  **Clone the repository (or download the files):**

    ```bash
    git clone [repository-url]
    cd MovieFinder
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **API Key Configuration:**
    The application is configured to use the OMDb API with the key `'605797f8'`. While this key might work for testing, you may need to register for your own free OMDb API key and update the `OMDB_API_KEY` variable in `app.py` if the included key stops working or hits rate limits.

-----

## Running the Application

1.  **Ensure your virtual environment is active.**

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application is set to run in debug mode.

3.  **Access the application:**
    Open your web browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```
<img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/f649c24e-45c3-45d6-acee-98c6ce084e73" />
  Here We can Search For Movies Example Iam Searching Avengers It gave me Certain list of movies 
<img width="940" height="423" alt="image" src="https://github.com/user-attachments/assets/3b2d8549-2658-4d18-be23-3b6e0a917fde" />
After Seeing The Results We Can add the movies based on our choices We Can Add The movies to Watchlist 
<img width="940" height="415" alt="image" src="https://github.com/user-attachments/assets/44cbbb11-5b98-49b0-badd-d6211a3ea5f2" />
Now We Can check Our Watchlist
<img width="940" height="327" alt="image" src="https://github.com/user-attachments/assets/868f7765-cdb3-4501-b828-bbb7d754e3a5" />
We Can update our Watchlist with More Movies 
<img width="940" height="594" alt="image" src="https://github.com/user-attachments/assets/6b06b0bf-9c43-4c3a-ba74-8bf62b637a54" />

-----

## Important Notes

  * **Watchlist Storage:** The watchlist is stored in a simple, in-memory Python list (`watchlist = []`). **Any movies added to the watchlist will be lost** when the Flask server is stopped or restarted.
  * **Search Logic:** When a user searches for a movie, the `/search` route first calls the OMDb API to get a list of results, and then makes a **second, separate API call for each result** to fetch the detailed plot summary, rating, and year data.
  * **No Poster Handling:** If a movie result is missing a poster URL, the `results.html` and `watchlist.html` templates are set up to try and load a fallback image at `/static/no-poster.png` using the `onerror` attribute.
