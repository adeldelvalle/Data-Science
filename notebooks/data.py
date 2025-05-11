gics_sectors = [
    "Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples",
    "Health Care", "Financials", "Information Technology", "Communication Services",
    "Utilities", "Real Estate"
]

# Example sentence templates
templates = [
    "The {} sector outperformed the market this quarter.",
    "{} stocks have shown strong resilience in recent months.",
    "Investors are rotating into the {} sector.",
    "{} companies saw a decline due to economic pressures.",
    "Analysts are bullish on {} given recent earnings.",
    "The index is heavily weighted towards {}.",
    "{} has been a top performer in the S&P 500.",
    "Market volatility has had little impact on {}.",
    "There is increasing regulatory pressure on {}.",
    "{} remains undervalued according to most analysts.",
    "ETFs tracking {} are gaining popularity.",
    "New policy changes could impact the {} industry.",
    "{} continues to attract institutional investors.",
    "{} will likely benefit from rising interest rates.",
    "Global trends are favoring growth in {}.",
    "{} stocks have seen the largest inflows this week.",
    "Mergers and acquisitions are reshaping the {} space.",
    "{} plays a vital role in the national economy.",
    "{} faces challenges from new market entrants.",
    "The performance of {} is closely tied to commodity prices."
]

# Generate 200 examples
TRAIN_DATA = []
for _ in range(200):
    sector = random.choice(gics_sectors)
    template = random.choice(templates)
    sentence = template.format(sector)
    start = sentence.index(sector)
    end = start + len(sector)
    TRAIN_DATA.append((sentence, {"entities": [(start, end, "SECTOR")]}))
