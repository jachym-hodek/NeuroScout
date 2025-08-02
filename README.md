    # NeuroScout

NeuroScout is an open-source web scraping and aggregation tool designed to help high school students discover neuroscience-related opportunities. These include lectures, competitions, internships, and more. The project gathers data from across the web, stores it in a database, and makes it accessible through a user-friendly website.

## Project Goals

- **Accessibility**: Make neuroscience opportunities more visible and accessible to high school students.
- **Automation**: Use automated web scraping and APIs to collect opportunities.
- **Centralization**: Store and display the collected opportunities in one easy-to-navigate platform.

---

## Features

- Scrapes data from structured and unstructured web sources
- Supports various types of opportunities (lectures, internships, competitions, etc.)
- Stores data in a searchable and filterable database
- Provides data for display on a frontend website (to be developed or integrated)

---

## Technology Stack

- **Python** for the scraping logic and data handling
- **BeautifulSoup**, **requests**, **Selenium** for web scraping
- **Google Custom Search API**, **PRAW**, or **snscrape** for structured site scanning and social media
- **SQLite / PostgreSQL** for data storage
- **Flask** or **FastAPI** for backend (optional for API interface)
- **HTML/CSS/JS** or a frontend framework (e.g., React) for the website interface (not yet implemented)

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/neuroscout.git
   cd neuroscout
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Run the scraper script:**

   ```bash
   python main.py
   ```

4. **(Optional) Start the backend server:**

   ```bash
   uvicorn app.main:app --reload
   ```

---

## Folder Structure

```
neuroscout/
├── main.py                # Main script for running the scraper
├── scrapers/              # Custom scrapers for individual sources
├── database/
│   └── models.py          # ORM/database schema
├── data/                  # Raw or processed data output
├── app/                   # Backend API (optional)
├── utils/                 # Utilities (e.g. date parsing, keyword matching)
├── templates/             # For future web frontend
└── README.md              # Project documentation
```

---

## Future Plans

- Add automated scheduling (e.g. with `cron` or `APScheduler`)
- Build a user-facing web interface
- Add notification features (e.g. email alerts for new opportunities)
- Expand the list of sources and keywords

---

## Contribution Guidelines

We welcome contributions! Please fork the repository and submit a pull request. Before contributing:

- Follow PEP8 style guidelines
- Write meaningful commit messages
- Document your code clearly

---

## License

This project is licensed under the MIT License.

---

## Contact

Maintained by Jáchym Hodek. For inquiries, open an issue or reach out at [hodekjachym00@gmail.com](mailto\:hodekjachym00@gmail.com).

