from flask import Blueprint, jsonify, request
from app.models import Manga, db
from flask_login import current_user, login_required
from datetime import datetime
