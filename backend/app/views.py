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

@main.route('/api/seed')
def seed():
    from app.models import Profile, Skill, Education, Experience, Project
    
    if Profile.query.first():
        return jsonify({'message': 'Already seeded'})
    
    p = Profile(
        name="Romaine Dixon",
        title="Software Engineer & Electronics Engineer",
        tagline="Building clean, scalable web applications",
        bio="Software Engineer and Electronics Engineer with 5+ years of hands-on experience spanning full-stack development, IT infrastructure, and embedded systems. Currently working as a Helpdesk Officer at NERHA while pursuing my BSc in Software Engineering at UWI.",
        avatar_url="https://res.cloudinary.com/dydzpx6mb/image/upload/f_auto,q_auto/A1D81E03-60D5-4C8F-9AC6-6034B1C78237_u7bch9",
        resume_url="https://drive.google.com/file/d/1dOSL7iOeIYEQsD-vGMy_cCzccgVLg1Dj/preview",
        github_url="https://github.com/YoriichiTsugiikuni",
        linkedin_url="https://www.linkedin.com/in/romaine-dixon-333754219/"
    )
    db.session.add(p)

    skills = [
        Skill(name="Python", category="language", proficiency=85),
        Skill(name="JavaScript", category="language", proficiency=80),
        Skill(name="Java", category="language", proficiency=75),
        Skill(name="SQL", category="language", proficiency=80),
        Skill(name="Flask", category="framework", proficiency=85),
        Skill(name="Vue 3", category="framework", proficiency=80),
        Skill(name="SQLAlchemy", category="framework", proficiency=80),
        Skill(name="Bootstrap", category="framework", proficiency=80),
        Skill(name="PostgreSQL", category="database", proficiency=80),
        Skill(name="MySQL", category="database", proficiency=75),
        Skill(name="REST API Design", category="tool", proficiency=85),
        Skill(name="OOP & Software Design Patterns", category="tool", proficiency=85),
        Skill(name="MVC Architecture", category="tool", proficiency=82),
        Skill(name="JWT Authentication", category="tool", proficiency=80),
        Skill(name="Data Structures & Algorithms", category="tool", proficiency=78),
        Skill(name="Git & Version Control", category="tool", proficiency=85),
    ]
    db.session.add_all(skills)

    experience = [
        Experience(
            company="St. Ann's Bay Regional Hospital, NERHA",
            role="Helpdesk Officer",
            start_date="Sep 2024",
            end_date="Present",
            description="Administer and maintain hospital EHR systems ensuring reliability and compliance with clinical workflows. Deliver frontline technical support to healthcare professionals, resolving software, hardware, and network issues. Deploy and maintain desktop computers and peripheral devices across all hospital departments. Design and facilitate user training sessions for clinical and administrative staff, driving system adoption and reducing recurring errors. Enforce data security protocols and manage helpdesk documentation.",
            current=True
        ),
        Experience(
            company="Salus Technology Services",
            role="Systems Specialist",
            start_date="Jan 2024",
            end_date="Aug 2024",
            description="Configured, maintained, and optimised servers, operating systems, and enterprise applications to ensure maximum reliability and performance. Administered user accounts, permissions, and security policies. Performed system monitoring, patching, and preventive maintenance, reducing downtime and improving overall system availability.",
            current=False
        ),
        Experience(
            company="Jamaica Public Service (JPS)",
            role="Project Analyst",
            start_date="Sep 2023",
            end_date="Jan 2024",
            description="Worked in the GIS Department to update and enhance geographic information systems island-wide, supporting accurate asset mapping, improved system planning, and operational efficiency.",
            current=False
        ),
        Experience(
            company="Jamaica Public Service (JPS)",
            role="Intern",
            start_date="Sep 2022",
            end_date="Aug 2023",
            description="Completed an internship at JPS gaining hands-on experience in systems and operations within a large utility organisation.",
            current=False
        ),
    ]
    db.session.add_all(experience)

    education = [
        Education(
            institution="University of the West Indies, Mona",
            degree="Bachelor of Science",
            field="Software Engineering (Major) & Economics (Minor)",
            start_year=2024,
            end_year=2027
        ),
        Education(
            institution="University of the West Indies, Mona",
            degree="Bachelor of Science (Hons)",
            field="Electronics Engineering",
            start_year=2019,
            end_year=2022
        ),
        Education(
            institution="Glenmuir High School",
            degree="Associate Degree & High School Diploma",
            field="General Studies",
            start_year=2012,
            end_year=2019
        ),
    ]
    db.session.add_all(education)

    projects = [
        Project(
            title="Real-Time Vehicle Tracking System",
            description="A real-time vehicle tracking system integrating GPS and GSM hardware modules with the Google Maps API. Tracks live vehicle location, displays movement on an interactive map, and transmits data via GSM. Demonstrates IoT, hardware-software integration, and real-time data handling.",
            tech_stack="Python, Google Maps API, GPS Module, GSM Module, JavaScript",
            featured=True,
            order_index=1
        ),
        Project(
            title="Legal Case Management System",
            description="A desktop application designed for lawyers to manage and organise their cases efficiently. Features case creation, client tracking, document management, and status updates through an intuitive GUI built with Java Swing.",
            tech_stack="Java, Java Swing, SQLite",
            featured=True,
            order_index=2
        ),
        Project(
            title="Automated Attendance Tracking System",
            description="An automated attendance system using QR code scanning via device camera. Users scan their unique QR code to log attendance in real time, eliminating manual registers and reducing errors.",
            tech_stack="JavaScript, HTML5, CSS3, HTML5 Camera API, jsQR, LocalStorage",
            featured=True,
            order_index=3
        ),
    ]
    db.session.add_all(projects)

    db.session.commit()
    return jsonify({'message': 'Database seeded successfully'})