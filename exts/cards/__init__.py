import os
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.fileutil import copy_asset


class card(nodes.General, nodes.Element):
    pass


def visit_card_node(self, node):
    title = node.get("title", "")
    key = title or node["github"]
    key = key.lower().replace(" ", "-")
    title = f"<h4>{title}</h4>" if len(title) > 0 else ""

    col_extra_class = "column-half" if title else ""

    body = f"""<div class="column {col_extra_class}">
                {title}
                <div class="card">
                <img class="dark-light" src="/_static/img/{node['img_name']}" alt="{node['name']}">
                <p>{node['name']}</p>
                <p><button type="button" class="btn btn-sunpy btn-sunpy1" data-bs-toggle="modal" data-bs-target="#{key}">More Info</button></p>
                <div class="modal fade" id="{key}" tabindex=-1>
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h4 class="modal-title center">{node['name']}</h4>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
    """
    self.body.append(body)


def depart_card_node(self, node):
    body = f"""
                                <p>Affiliation: <a href="{node['aff_link']}">{node['aff_name']}</a></p>
                                <p>GitHub: <a href="https://github.com/{node['github']}">{node['github']}</a></p>
                                <p>Start Date: {node['date']}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div></div>"""

    self.body.append(body)


class Card(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 6
    option_spec = {
        "img_name": directives.unchanged,
        "title": directives.unchanged,
        "github": directives.unchanged,
        "aff_name": directives.unchanged,
        "aff_link": directives.unchanged,
        "date": directives.unchanged,
        "desc": directives.unchanged,
    }

    def run(self):
        if "title" in self.options:
            title = self.options.get("title")
        else:
            title = ""
        if "img_name" in self.options:
            img_name = self.options.get("img_name")
        else:
            img_name = "sunpy_icon.svg"
        if "github" in self.options:
            github = self.options.get("github")
        else:
            github = ""
        if "aff_name" in self.options:
            aff_name = self.options.get("aff_name")
        else:
            aff_name = ""
        if "aff_link" in self.options:
            aff_link = self.options.get("aff_link")
        else:
            aff_link = ""
        if "date" in self.options:
            date = self.options.get("date")
        else:
            date = ""
        if "desc" in self.options:
            desc = self.options.get("desc")
        else:
            desc = "N/A"

        name = " ".join(self.arguments)

        out = card(
            name=name,
            img_name=img_name,
            title=title,
            github=github,
            aff_name=aff_name,
            aff_link=aff_link,
            date=date,
            desc=desc,
        )

        self.state.nested_parse(self.content, 0, out)

        return [out]


def copy_asset_files(app, exc):
    if exc is None:  # build succeeded
        for path in (Path(__file__).parent / "static").glob("*"):
            copy_asset(str(path), os.path.join(app.outdir, "_static"))


def setup(app):
    app.add_node(card, html=(visit_card_node, depart_card_node))

    app.add_css_file("cards.css")
    app.add_directive("custom-card", Card)

    app.connect("build-finished", copy_asset_files)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
