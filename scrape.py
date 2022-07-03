from scrapeutils import Scraper
from rich.console import Console
from rich.progress import Progress

console = Console()
console.print("Starting scraper", style="bold yellow")

with Progress() as progress:
    scrapeTask = progress.add_task("[yellow]Scraping...", total=5)
    f = open("tweets.txt", "a")
    TweetScraper = Scraper()
    TweetScraper.openTwitterProfile("kfc")
    TweetScraper.getTweets(f, progress, scrapeTask)
    TweetScraper.report()

console.print("Success", style="bold green") 
f.close()