from flask import render_template, Blueprint
from PyAny_MainApp.flames_app.forms import FlamesForm
from PyAny_MainApp.flames_app.flames_match import match_results

flames_app = Blueprint('flames_app',__name__)

# Submit online daily monitoring form
@flames_app.route('/flames_app', methods=['GET','POST'])
def flames():
  form = FlamesForm()
  results_header = "Results"
  results = "(Results display here)"
  if form.validate_on_submit:
    your_name = form.your_name.data
    crush_name = form.crush_name.data
    try:
      results_header = f"Results for {your_name.title()} and {crush_name.title()}"
      results = match_results(yourName=your_name,crushName=crush_name)
    except:
      results_header = "Results"
      results = "(Results display here)"
      return render_template('flames_app.html',form=form,results=results,results_header=results_header)
    return render_template('flames_app.html',form=form,results=results,results_header=results_header)
  
  return render_template('flames_app.html',form=form,results=results)