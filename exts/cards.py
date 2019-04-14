from docutils import nodes
from docutils.parsers.rst import Directive, directives


class card(nodes.General, nodes.Element):
    pass


def visit_card_node(self, node):

    img_name = node["img_name"]
    name = node["name"]
    github = node["github"]
    aff_name = node["aff_name"]
    aff_link = node["aff_link"]
    date = node["date"]
    desc = node["desc"]

    if node["title"]:
        title = "<h4>{}</h4>".format(node["title"])
    else:
        title = ""

    col_extra_class = "column-half" if title else ""

    body = f"""<div class="column {col_extra_class}">
                {title}
                <div class="card">
                <img src="_static/img/{img_name}" alt="{name}">
                <p>{name}</p>
                <p><button class="button" data-toggle="modal" data-target="#{github}">More Info</button></p>
                <div class="modal fade" id="{github}" role="dialog" style="display: none;">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                                <h4 class="modal-title center">{name}</h4>
                            </div>
                            <div class="modal-body">
                                <p>{desc}</p>
                                <p>Affiliation: <a href="{aff_link}">{aff_name}</a></p>
                                <p>Github: <a href="https://github.com/{github}">@{github}</a></p>
                                <p>Start Date: {date}</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div></div>"""

    self.body.append(body)


def depart_card_node(self, node):
    pass


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

        if "img_name" in self.options:
            img_name = self.options.get("img_name")
        else:
            img_name = "sunpy_icon.svg"
        if "github" in self.options:
            github = self.options.get("github")
        else:
            github = "sunpy"
        if "aff_name" in self.options:
            aff_name = self.options.get("aff_name")
        else:
            aff_name = "sunpy"
        if "title" in self.options:
            title = self.options.get("title")
        else:
            title = ""
        if "aff_link" in self.options:
            aff_link = self.options.get("aff_link")
        else:
            aff_link = "sunpy.org"
        if "date" in self.options:
            date = self.options.get("date")
        else:
            date = "1066"
        if "desc" in self.options:
            desc = self.options.get("desc")
        else:
            desc = "N/A"

        if len(self.arguments) == 2:
            name = self.arguments[0] + " " + self.arguments[1]
        else:
            name = self.arguments[0]

        return [
            card(
                name=name,
                img_name=img_name,
                title=title,
                github=github,
                aff_name=aff_name,
                aff_link=aff_link,
                date=date,
                desc=desc,
            )
        ]


def setup(app):
    app.add_node(card, html=(visit_card_node, depart_card_node))
    app.add_directive("card", Card)
