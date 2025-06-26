import waveassist
waveassist.init()

joke = waveassist.fetch_data("joke") or "No joke today, but here's a smile anyway 🙂"

html = f"""
<div style="font-family: Arial, sans-serif; padding: 12px;">
  <h2 style="font-size: 20px; font-weight: normal;">😂 {joke}</h2>
</div>
"""

waveassist.send_email(
    subject="Your Daily Dad Joke",
    html_content=html.strip()
)

waveassist.store_data("email_sent", True)
