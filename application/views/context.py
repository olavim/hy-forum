from flask import request
from ..main import app
from ..forms.search import QuickSearchForm

@app.context_processor
def inject_search_form():
	search_form = QuickSearchForm(None)
	return dict(search_form=search_form)
