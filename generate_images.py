from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import csv
import os

def create_image(number, english_text, russian_text):
    output_image = f"Images/{number}.png"
    page_width, page_height = 1920, 1080
    margin = 30

    with Image(width=page_width, height=page_height, background=Color("white")) as img:
        with Drawing() as draw:
            draw.font = "Arial"
            draw.fill_color = Color("black")

            # Adjust font size for number
            number_font_size = 100
            draw.font_size = number_font_size
            number_metrics = draw.get_font_metrics(img, str(number))
            while number_metrics.text_width + margin > page_width:
                number_font_size -= 10
                draw.font_size = number_font_size
                number_metrics = draw.get_font_metrics(img, str(number))
            draw.text(margin, page_height - margin, str(number))

            # Adjust font size for English text
            english_font_size = 100
            draw.font_size = english_font_size
            english_metrics = draw.get_font_metrics(img, english_text)
            while english_metrics.text_width + margin > page_width:
                english_font_size -= 10
                draw.font_size = english_font_size
                english_metrics = draw.get_font_metrics(img, english_text)
            draw.text(margin, int((page_height - english_metrics.text_height) / 2), english_text)

            # Adjust font size for Russian text
            russian_font_size = 50
            draw.font_size = russian_font_size
            russian_metrics = draw.get_font_metrics(img, russian_text)
            while russian_metrics.text_width + margin > page_width:
                russian_font_size -= 5
                draw.font_size = russian_font_size
                russian_metrics = draw.get_font_metrics(img, russian_text)
            draw.text(margin, int((page_height - english_metrics.text_height) / 2) + int(russian_metrics.text_height) + 20, russian_text)

            # Add "ILYAAA.COM" / URL with adjusted coordinates
            draw.text(page_width - 400, page_height - 60, "ILYAAA.COM")
            draw(img)

        img.save(filename=output_image)

def main():
    if not os.path.exists("Images"):
        os.makedirs("Images")

    with open("phrases.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            number, english_phrase, russian_phrase = row
            create_image(number, english_phrase, russian_phrase)

if __name__ == "__main__":
    main()
