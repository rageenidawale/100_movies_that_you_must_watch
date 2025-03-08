# 🎬 100 movies that you must watch

## 📌 Overview  
This project **scrapes** a list of the **100 greatest movies** from a webpage using `BeautifulSoup` and saves them in a text file.  

## 🚀 Features  
- 🌐 **Web Scraping** - Extracts movie titles from a webpage.  
- 📜 **Data Storage** - Saves the movie list to a `movie_names.txt` file.  
- 🔄 **Reverses Order** - Arranges the movies in ranking order from 1 to 100.  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **BeautifulSoup** 🏗️ (for web scraping)  
- **Requests** 🌐 (to fetch the webpage)  

## 📸 Screenshot  
*(Example output stored in `movie_names.txt`)*  
```
1. The Godfather  
2. The Dark Knight  
3. Pulp Fiction  
...
100. Some Movie  
```

## 📂 File Structure  
```
/movie-scraper
│── movie_scraper.py
│── movie_names.txt
│── README.md
```

## 📜 How to Run  
1. Clone the repository:  
   ```
   git clone https://github.com/your-username/movie-scraper.git
   ```
2. Install dependencies:  
   ```
   pip install beautifulsoup4 requests
   ```
3. Run the script:  
   ```
   python movie_scraper.py
   ```
4. Check `movie_names.txt` for the list! 🎥  

## 🎯 Future Enhancements  
- 🏆 **Allow users to specify the number of movies to scrape.**  
- 🔎 **Scrape from multiple sources for a more diverse list.**  
- 📝 **Save in JSON or CSV format for better usability.**  
- 📊 **Create a GUI to display the movies interactively.**  


🎬 *Enjoy your ultimate movie list!* 🍿
