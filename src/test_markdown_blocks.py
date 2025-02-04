import unittest

from htmlnode import HTMLNode

from markdown_blocks import*

class TestSplitDelimiter(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        block_out = markdown_to_blocks(text)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],block_out
        ) 
    
    
    def test_markdown_to_block_epic(self):
        markdown = "# Heading\n\nParagraph\n\n* List item"
        block_out = markdown_to_blocks(markdown)
        self.assertListEqual(
            ["# Heading", "Paragraph", "* List item"],block_out
        )  

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks_hard_way(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks_hard_way(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_heading_valid(self):
        text = "# Heading"
        res = block_to_block_type(text)
        self.assertEqual(
            "heading",
            res
        )
        text = "###### Heading"
        res = block_to_block_type(text)
        self.assertEqual(
            "heading",
            res
        )
    
    def test_heading_invalid(self):
        text = "#Heading"
        res = block_to_block_type(text)
        self.assertEqual(
            "paragraph",
            res
        )
        text = "####### Heading"
        res = block_to_block_type(text)
        self.assertEqual(
            "paragraph",
            res
        )

    def test_block_to_block_type_valid(self):
        text = """> Quote
> Quote2"""
        res = block_to_block_type(text)
        self.assertEqual(
            "quote",
            res
        )
        text = """- item
- item2
- item3"""
        res = block_to_block_type(text)
        self.assertEqual(
            "unordered_list",
            res
        )
        text = """* item
* item2
* item3"""
        res = block_to_block_type(text)
        self.assertEqual(
            "unordered_list",
            res
        )
        text = """1. item
2. item2
3. item3"""
        res = block_to_block_type(text)
        self.assertEqual(
            "ordered_list",
            res
        )
    ##aca 
    ##aca
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_extract_title(self):
        text = """## Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

# My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```"""
        title = extract_title(text)
        self.assertEqual(title,"My favorite characters (in order)")

if __name__ == "__main__":
    unittest.main()