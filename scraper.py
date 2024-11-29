from telethon.sync import TelegramClient
import csv

# Telegram API credentials
API_ID = "24825344"
API_HASH = "a953af5f7e280426c059fb3192893403"
CHANNEL_USERNAME = "mohancareers"  # Replace with the Telegram channel/group username

async def scrape_messages():
    async with TelegramClient('session', API_ID, API_HASH) as client:
        # Get the channel entity
        channel = await client.get_entity(CHANNEL_USERNAME)

        # Fetch messages
        messages = await client.get_messages(channel, limit=200)  # Adjust limit as needed
        print(f"Scraped {len(messages)} messages.")

        # Save messages to a CSV file
        with open('data/raw_data.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'sender_id', 'message'])  # Header row
            for message in messages:
                writer.writerow([message.date, message.sender_id, message.text])

if __name__ == "__main__":
    import asyncio
    asyncio.run(scrape_messages())
    print("Messages scraped and saved to data/raw_data.csv.")
