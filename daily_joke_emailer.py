import waveassist
waveassist.init()

joke = waveassist.fetch_data("joke")

waveassist.send_email(
    subject="Your Daily Dad Joke",
    html_content=f"<p>{joke}</p>"
)

waveassist.store_data("email_sent", True)