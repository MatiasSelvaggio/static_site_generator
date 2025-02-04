from textnode import TextNode, TextType
from static_website import *


def main():
    copy_all("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")



if __name__ == "__main__":
    main()