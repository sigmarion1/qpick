# qpick.app

Your go-to website for making random choices easy and fun! Whether you're deciding between lunch options, picking a movie to watch, or selecting who's up next for a game, qpick.app simplifies the decision-making process.

## How to Use qpick.app

### Making a Random Choice

1. **Gather Your Options**: Start by deciding on the items among which you want to make a random choice. These can be anything: names, places, activities, etc.

2. **Format Your URL**: Enter your options into the Pick1.me URL by appending them to the site's base URL in a comma-separated list. For example: https://qpick.app/pizza,sushi,burger

3. **Get Your Random Pick**: Hit enter or navigate to the formatted URL in your web browser. Pick1.me will automatically select one of the options at random and display it on the screen.

### Fixing the Result with a Seed Value

1. **Choose a Seed**: Your seed can be any string, like a date (`2024-01-01`) or a word (`WhatDoWeHaveForDinner`). The same seed will always produce the same result from the same list of options.

2. **Format Your URL with a Seed**: Append the seed value to the end of the URL after a slash (/). For example: https://qpick.app/pizza,sushi,burger/2024-01-01 https://qpick.app/pizza,sushi,burger/WhatDoWeHaveForDinner

3. **Get Your Fixed Result**: Navigate to the URL with your seed value included. The website will display the choice determined by the seed value, providing a consistent result for the same input and seed.

### Tips for Using qpick.app

- Double-Check Your List: Ensure there are no unintentional spaces after commas in your list, as this might affect the random selection or seed result.

- Creative Seeding: Use memorable dates or words for seeds when you need consistent results across different sessions or for sharing with others.

- Share Your Picks: Easily share your choices with friends or colleagues by sending them the URL. They'll get the same random (or fixed) result as you did.

## Support

Have questions, feedback, or suggestions? We're always looking to improve your experience. Please note that qpick.app currently does not offer direct support channels, but we encourage users to explore the site and discover its simplicity and convenience for all your decision-making needs.

### Thank you for using qpick.app – the simplest way to make random choices online!

### run develop app

```
source venv/bin/activate
uvicorn main:app --reload
```
