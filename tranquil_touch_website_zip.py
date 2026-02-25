import os
from zipfile import ZipFile
from PIL import Image, ImageOps
import shutil

# --- Setup folders ---
folder_name = "Tranquil_Touch_Website"
public_folder = os.path.join(folder_name, "public")
os.makedirs(public_folder, exist_ok=True)

# --- Logo processing ---
# Open your original logo (hand + leaf) - make hand+leaf green (#A8BFA0), rest transparent
def process_logo(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        # Assuming hand+leaf are not white/transparent
        if item[3] != 0 and sum(item[:3]) < 700:  # simple threshold for non-background
            new_data.append((168, 191, 160, item[3]))  # green #A8BFA0
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(output_path, "PNG")

process_logo("your_logo.png", os.path.join(public_folder, "logo.png"))

# --- Copy PDF ---
shutil.copy("Tranquil_Touch_Luxury_Brochure.pdf", os.path.join(public_folder, "Tranquil_Touch_Luxury_Brochure.pdf"))

# --- Create index.html ---
index_html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Tranquil Touch Cleaning Co.</title>
  <link rel=\"stylesheet\" href=\"styles.css\">
</head>
<body>
  <header>
    <img src=\"public/logo.png\" alt=\"Tranquil Touch Logo\" class=\"logo\">
    <h1>Tranquil Touch Cleaning Co.</h1>
    <p class=\"tagline\">Soft • Intentional • Nature-Inspired Cleaning</p>
  </header>
  <section>
    <h2>Our Services</h2>
    <ul>
      <li>Standard Residential Cleaning – Starting at $160</li>
      <li>Deep Cleaning – Starting at $240</li>
      <li>Airbnb / Short-Term Rental Turnover – Custom Quote</li>
      <li>Commercial Cleaning – Custom Quote</li>
    </ul>
  </section>
  <section>
    <h2>Enhance Your Experience</h2>
    <ul>
      <li>Laundry Service</li>
      <li>Home Organization</li>
      <li>Interior Fridge Cleaning</li>
      <li>Interior Oven Cleaning</li>
      <li>Bed Linen Refresh</li>
    </ul>
  </section>
  <section>
    <h2>Contact</h2>
    <p>Phone: 509-558-1623</p>
    <p>Email: tranquil29touch@gmail.com</p>
    <p>Serving Spokane Valley & Surrounding Areas</p>
  </section>
  <section>
    <a href=\"public/Tranquil_Touch_Luxury_Brochure.pdf\" download class=\"download-button\">
      Download Our Luxury Brochure
    </a>
  </section>
</body>
</html>
"""
with open(os.path.join(folder_name, "index.html"), "w") as f:
    f.write(index_html)

# --- Create styles.css ---
styles_css = """body { font-family: sans-serif; margin: 0; padding: 0; line-height: 1.6; color: #333; }
header { text-align: center; padding: 2rem 1rem; }
header .logo { width: 150px; margin-bottom: 1rem; }
h1 { color: #A8BFA0; margin-bottom: 0.5rem; }
.tagline { color: grey; font-size: 1.1rem; margin-bottom: 1.5rem; }
section { max-width: 700px; margin: 2rem auto; padding: 0 1rem; }
h2 { color: #C6A75E; margin-bottom: 1rem; }
ul { list-style-type: disc; padding-left: 1.5rem; }
.download-button { display: inline-block; background-color: #A8BFA0; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 1rem; }"""
with open(os.path.join(folder_name, "styles.css"), "w") as f:
    f.write(styles_css)

# --- Create ZIP ---
zip_filename = "Tranquil_Touch_Website.zip"
with ZipFile(zip_filename, "w") as zipf:
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_name))

print(f"{zip_filename} created successfully! ✅")