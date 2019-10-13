from flask import request
import config
from ..main import app
from ..forms.search import QuickSearchForm

# Inject some common variables to all templates

@app.context_processor
def inject_search_form():
	search_form = QuickSearchForm(None)
	return dict(search_form=search_form)

@app.context_processor
def inject_page_size():
	return dict(page_size=config.page_size)
