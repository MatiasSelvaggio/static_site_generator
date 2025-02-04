from textnode import TextNode, TextType
from static_website import *


def main():
    copy_all("static", "public")
    generate_pages_recursive("content/", "template.html", "public/")



if __name__ == "__main__":
    main()