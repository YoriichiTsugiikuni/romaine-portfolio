from flask import Blueprint, jsonify, request
from app import db
from app.models import Profile, Project, Skill, Experience, Education, Message

main = Blueprint('main', __name__)

@main.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Portfolio API running'})

# --- PROFILE ---
@main.route('/api/profile')
def get_profile():
    profile = Profile.query.first()
    if not profile:
        return jsonify({'error': 'No profile found'}), 404
    return jsonify({
        'id': profile.id,
        'name': profile.name,
        'title': profile.title,
        'tagline': profile.tagline,
        'bio': profile.bio,
        'avatar_url': profile.avatar_url,
        'resume_url': profile.resume_url,
        'github_url': profile.github_url,
        'linkedin_url': profile.linkedin_url
    })

# --- PROJECTS ---
@main.route('/api/projects')
def get_projects():
    projects = Project.query.order_by(Project.order_index).all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'tech_stack': p.tech_stack,
        'github_url': p.github_url,
        'live_url': p.live_url,
        'image_url': p.image_url,
        'featured': p.featured
    } for p in projects])

# --- SKILLS ---
@main.route('/api/skills')
def get_skills():
    skills = Skill.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'category': s.category,
        'proficiency': s.proficiency,
        'icon': s.icon
    } for s in skills])

# --- EXPERIENCE ---
@main.route('/api/experience')
def get_experience():
    experience = Experience.query.all()
    return jsonify([{
        'id': e.id,
        'company': e.company,
        'role': e.role,
        'start_date': e.start_date,
        'end_date': e.end_date,
        'description': e.description,
        'current': e.current
    } for e in experience])

# --- EDUCATION ---
@main.route('/api/education')
def get_education():
    education = Education.query.all()
    return jsonify([{
        'id': e.id,
        'institution': e.institution,
        'degree': e.degree,
        'field': e.field,
        'start_year': e.start_year,
        'end_year': e.end_year
    } for e in education])

# --- CONTACT ---
@main.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    


    message = Message(
        name=data.get('name'),
        email=data.get('email'),
        subject=data.get('subject'),
        body=data.get('body')
    )
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201

