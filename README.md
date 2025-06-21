# General information
This project showcases Serhii Korobov's Python backend skills.
It is a scraper for a random car sales website (you can configure website starting page in .env file and if it
fits the HTML structure, everything will work).
Built with Python, PostgreSQL, Playwright, BeautifulSoup and Docker.

# Project structure
```
project/
├── app/
│   ├── application/
│   │   ├── parsers.py
│   │   └── use_cases.py
│   ├── domain/
│   │   └── models.py
│   ├── infrastructure/
│   │   ├── db/
│   │   │   ├── models.py
│   │   │   ├── repositories.py
│   │   │   ├── setup.py
│   │   │   └── utils.py
│   │   ├── crawlers.py
│   │   └── scrapers.py
│   ├── bootstrap.py
│   ├── config.py
│   └── utils.py
├── docker/
│   └── Dockerfile.scraper
├── dumps/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

# Project installation
1. Clone the repository to your local machine or server:
   `git clone https://github.com/Peppendom/Scraper_v1`
2. Start your Docker application.
3. Configure settings in `/app/config.py` if needed.
4. Create a `.env` file in the root folder by renaming `.env.example`.
5. Add the base site URL you want to scrape to the `.env` file under `BASE_SCRAPING_URL`.
6. Run `docker-compose up` in your terminal.

# Project settings
You can configure.
1. Scraping settings:
- Maximum number of links scraper will process. Set to 'None' to scrape all pages.
- Number of concurrent browser windows used for scraping.

2. Cron settings:
- Schedule (time and timezone) for scraping and database dump jobs.

3. Database settings.
- Toggle `POSTGRES_HOST` to switch between local testing to production
- Set timezone and datetime format for database dumps names.