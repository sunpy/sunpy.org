from docutils import nodes
from docutils.parsers.rst import Directive, directives


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
                <img src="/_static/img/{node['img_name']}" alt="{node['name']}">
                <p>{node['name']}</p>
                <p><button class="button" data-toggle="modal" data-target="#{key}">More Info</button></p>
                <div class="modal fade" id="{key}" role="dialog" style="display: none;">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                                <h4 class="modal-title center">{node['name']}</h4>
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
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
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


def setup(app):
    app.add_node(card, html=(visit_card_node, depart_card_node))
    app.add_directive("card", Card)
