#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with the Open Graph standard size
width = 1200
height = 630
bg_color = '#667eea'  # Matching the gradient from the site

# Create gradient background
img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

# Create gradient from purple to darker purple
for y in range(height):
    # Gradient from #667eea to #764ba2
    r = int(102 + (118 - 102) * y / height)
    g = int(126 + (75 - 126) * y / height)
    b = int(234 + (162 - 234) * y / height)
    draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

# Load and resize profile image
profile = Image.open('emckenna-profile.png')
profile = profile.convert('RGBA')

# Create circular mask
profile_size = 300
profile = profile.resize((profile_size, profile_size), Image.LANCZOS)

# Create circular mask
mask = Image.new('L', (profile_size, profile_size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, profile_size, profile_size), fill=255)

# Create a white circle background
circle_bg = Image.new('RGBA', (profile_size + 10, profile_size + 10), (255, 255, 255, 255))
circle_mask = Image.new('L', (profile_size + 10, profile_size + 10), 0)
circle_draw = ImageDraw.Draw(circle_mask)
circle_draw.ellipse((0, 0, profile_size + 10, profile_size + 10), fill=255)

# Position for profile picture (left side)
profile_x = 100
profile_y = (height - profile_size) // 2

# Paste white circle first
img.paste(circle_bg, (profile_x - 5, profile_y - 5), circle_mask)

# Create output with alpha
output = Image.new('RGBA', (profile_size, profile_size), (0, 0, 0, 0))
output.paste(profile, (0, 0))
output.putalpha(mask)

# Paste the circular profile
img.paste(output, (profile_x, profile_y), output)

# Add text
draw = ImageDraw.Draw(img)

# Try to use a nice font, fallback to default
try:
    title_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 72)
    subtitle_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 42)
    body_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Text position (right side)
text_x = profile_x + profile_size + 80
text_y_start = 150

# Name
name_text = "Eric McKenna"
draw.text((text_x, text_y_start), name_text, font=title_font, fill='white')

# Title
title_text = "Senior Software Engineer"
draw.text((text_x, text_y_start + 90), title_text, font=subtitle_font, fill='white')

# Expertise
expertise_text = "Ruby on Rails • Full Stack • Team Lead"
draw.text((text_x, text_y_start + 160), expertise_text, font=body_font, fill=(255, 255, 255, 230))

# Years of experience
years_text = "25+ Years Experience"
draw.text((text_x, text_y_start + 220), years_text, font=body_font, fill=(255, 255, 255, 230))

# Save the image
img.save('og-image.png', 'PNG', quality=95)
print("✓ Created og-image.png (1200x630)")
