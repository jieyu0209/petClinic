from flask import render_template, flash, redirect, url_for, session, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
#from blogapp import app, db
from pet import app
#from blogapp.forms import LoginForm, SignupForm, ProfileForm, PostForm
#from blogapp.models import User,Post, Profile
#from blogapp.config import Config
#import os, time
import time


@app.route('/home')
def home():
	return render_template('home_default.html')
	
@app.route('/login')
def login():
	return render_template('log_in.html')

