from flask import render_template, url_for, flash, request, Blueprint
import pandas as pd
from datetime import datetime
from PyAny_MainApp.covid19_dailyreports.forms import HealthChecklistForm

covid19_dailyreports = Blueprint('covid19_dailyreports',__name__)

# Submit online daily monitoring form
@covid19_dailyreports.route('/covid19_healthchecklistform',methods=['GET','POST'])
def covid19_healthchecklistform():
  #form = HealthChecklistForm()
  #if form.validate_on_submit:
  #  pass
  return render_template('covid19_healthchecklistform.html')