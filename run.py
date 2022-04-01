from card_page.card_page import Card_Page

with Card_Page() as bot:
    bot.land_first_page()
    bot.find_all_card_urls()