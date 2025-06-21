from zoneinfo import ZoneInfo


# Limits settings
MAX_LINKS_LIMIT = 100
SEMAPHORE_LIMITS = 3


# Cron settings
CRON_SLEEPING_TIME = 60 * 60 * 1

SCRAPING_CRON_HOUR = 12
SCRAPING_CRON_MINUTE = 0
SCRAPING_CRON_TIMEZONE = "Europe/Kyiv"
SCRAPING_CRON_SCHEDULE = {
    "hour": SCRAPING_CRON_HOUR,
    "minute": SCRAPING_CRON_MINUTE,
    "timezone": ZoneInfo(SCRAPING_CRON_TIMEZONE)
}

DUMP_CRON_HOUR = 13
DUMP_CRON_MINUTE = 0
DUMP_CRON_TIMEZONE = "Europe/Kyiv"
DUMP_CRON_SCHEDULE = {
    "hour": DUMP_CRON_HOUR,
    "minute": DUMP_CRON_MINUTE,
    "timezone": ZoneInfo(DUMP_CRON_TIMEZONE)
}


# DB settings
# POSTGRES_HOST = "localhost"
POSTGRES_HOST = "cars_postgres"
POSTGRES_PORT = 5432
DUMP_NAME_TIMEZONE = "Europe/Kyiv"
DUMP_NAME_DATE_FORMAT = "%Y-%m-%d_%H-%M-%S"

# Magic numbers
THOUSAND = 1000
