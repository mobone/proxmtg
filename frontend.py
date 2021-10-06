from flask import Blueprint, render_template, flash, redirect, url_for, send_from_directory
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
from forms import SignupForm
from nav import nav
import wtf
from flask import request
from find_cards import get_images
from flask import session


frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('ProxyMTG', '.index'),
    View('Home', '.index'),
))
'''
Moonblade Shinobi
Ninja of the Deep Hours
'''
# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/', methods=['GET','POST'])
def index():
    form = SignupForm()
    
    if request.method == 'POST':
        flash('We have found the following card images', 'info')
        deck_name = str(form.deck_name.data).replace(' ','_')
        card_list = str(form.card_input.data.replace('\r','').split('\n'))
        print(card_list)
        result = get_images(deck_name, card_list)
        print(result)
        print("setting deck name", deck_name)
        

        return render_template('result.html', result=result.split('\n'),deck_name=deck_name)
        
    return render_template('index.html', form=form)


@frontend.route('/download/<deck_name>', methods=['GET','POST'])
def download_zip(deck_name):
    
    return send_from_directory('.\decks\\',filename=deck_name+'.zip', as_attachment=True)
    
@frontend.route('/delete/<deck_name>', methods=['GET','POST'])
def delete_zip(deck_name):

    import os

    
    os.remove('./decks//'+deck_name+'.zip')
    
    flash('Zip file has been removed from the server. Thanks!', 'info')

    return redirect('/')