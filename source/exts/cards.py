from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

class card(nodes.General, nodes.Element): pass

def visit_card_node(self, node):

    img_name = node['img_name']
    name = node['name']
    github = node['github']
    aff_name = node['aff_name']
    aff_link = node['aff_link']
    date = node['date']

    body="""<div class="card">
                <img src="_static/img/{}" alt="{}"></img>
                <p>{}</p>
                <p><button class="button" data-toggle="modal" data-target="#{}">More Info</button></p>
                <div class="modal fade" id="{}" role="dialog">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                                <h4 class="modal-title center">{}</h4>
                            </div>
                            <div class="modal-body">
                                <p>Affiliation : <a href="{}">{}</a></p>
                                <p>Github: <a href="https://github.com/{}">@{}</a></p>
                                <p>Start Date: {}</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>""".format(img_name, name, name, img_name, img_name, name, aff_link, aff_name, github, github, date)

    self.body.append(body)

def depart_card_node(self, node):
    pass

class Card(Directive):
    has_content = True
    required_arguments = 1
    option_spec = {
        "img_name": directives.unchanged,
        "github": directives.unchanged,
        "aff_name": directives.unchanged,
        "aff_link": directives.unchanged,
        "date": directives.unchanged,
                  }

    def run(self):

        if "img_name" in self.options:
            img_name = self.options.get("img_name")
        else:
            img_name = 'sunpy.svg'
        if "github" in self.options:
            github = self.options.get("github")
        else:
            github = 'sunpy'
        if "aff_name" in self.options:
            aff_name = self.options.get("aff_name")
        else:
            aff_name = 'sunpy'
        if "aff_link" in self.options:
            aff_link = self.options.get("aff_link")
        else:
            aff_link = 'sunpy.org'
        if "date" in self.options:
            date = self.options.get("date")
        else:
            date = '1066'

        return [card(name=self.arguments[0], img_name=img_name, github=github, aff_name=aff_name, aff_link=aff_link, date=date)]

def setup(app):
    app.add_node(card,html=(visit_card_node, depart_card_node))
    app.add_directive('card', Card)
