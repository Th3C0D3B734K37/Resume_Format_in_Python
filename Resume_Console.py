# Note: The resume information provided in the code is fictional and for demonstration purposes only. 
# Replace the details with your own information for an accurate representation of your resume.

def display_resume():
    # Greeting in Sanskrit
    greeting = """
\033[91mसर्वेभ्यः सुखिनः सन्तु।\033[0m
    
Translation:
May all beings be happy.
"""

    # Personal Information
    name = "John Doe"
    address = "123 Main Street, Anytown, USA"
    email = "johndoe@example.com"
    phone_number = "+1-555-1234"
    github_link = "https://github.com/johndoe"
    linkedin_link = "https://www.linkedin.com/in/johndoe/"

    # Objective
    objective = """
\033[91mObjective:\033[0m
    
A driven and dedicated B.Tech student in Computer Science and Engineering, 
seeking to leverage technical expertise and a deep passion for innovation to contribute to cutting-edge projects. 
With a strong belief in the transformative power of technology,I aspire to secure and shape the digital landscape 
while upholding strong ethical values.Through continuous learning and collaboration, I aim to make a positive impact, 
propelling the boundaries of cybersecurity to safeguard organizations and individuals in our ever-evolving digital era.
"""

    # Education
    education = [
        {
            "degree": "B.Tech in Computer Science and Engineering ",
            "institution": "ABC University",
            "batch": "2098 - 3002"
        },
        {
            "degree": "Higher Secondary Education",
            "institution": "XYZ School",
            "year_of_completion": "2098"
        },
        {
            "degree": "High School Education",
            "institution": "PQR School",
            "year_of_completion": "2096"
        }
    ]

    # Skills
    skills = [
        "Cybersecurity",
        "Programming (Python, C)",
        "Graphical Designing (Canva)",
        "Public Speaking",
        "Event Management and Fest Organization",
        "Team Leadership",
        "Quick Learner and Adaptable",
        "Hardworking and Disciplined",
        "Friendly and Quick to Adapt to Situations",
        "Time Management",
        "Problem Solving",
        "Data Analysis",
        "Communication Skills",
        "Critical Thinking",
        "Project Management"
    ]

    # Projects
    projects = [
        {
            "name": "Robo Car",
            "description": "Led a team in building a self-driving robotic car, showcasing technical skills in robotics, programming, and automation. Developed algorithms for object detection and motion planning, resulting in a fully functional autonomous vehicle."
        },
        {
            "name": "Circuit Breaker",
            "description": "Designed and prototyped a smart circuit breaker with advanced safety features using microcontrollers and IoT technology. Collaborated with a multidisciplinary team to ensure efficient power management and real-time monitoring capabilities."
        }
    ]

    # Contributions
    contributions = """
\033[91mContributions:\033[0m
    
Mentoring and Upskilling
Actively contributed to the learning and growth of fellow students by sharing knowledge, assisting with assignments, and conducting workshops. 
Demonstrated strong leadership and communication skills in guiding and motivating peers to achieve academic and personal success.

Continuous Learning Initiatives
Regularly attended industry conferences, webinars, and workshops to stay updated with the latest advancements in the field. 
Engaged with online learning platforms, technical blogs, and podcasts to expand knowledge and explore emerging technologies.
"""

    # Achievements
    achievements = """
\033[91mAchievements:\033[0m
    
Received accolades for outstanding public speaking skills through numerous stage performances.
Recognized for contributions to co-curricular activities, including [specific achievements or awards].
"""

    # How I Can Perform Better
    perform_better = """
\033[91mHow I Can Perform Better:\033[0m
    
Continuously upgrading skills through online courses and staying up-to-date with the latest industry trends and technologies.

Actively seeking opportunities to apply theoretical knowledge to practical projects to enhance problem-solving abilities.

Embracing challenges and learning from failures to foster personal and professional growth.

Seeking feedback and actively implementing suggestions for improvement.

Engaging in collaborative environments to enhance teamwork and communication skills.
"""

    # Display Resume
    print("========== Resume ==========")
    print(greeting)
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Email: {email}")
    print(f"Phone: {phone_number}")
    print(f"GitHub: {github_link}")
    print(f"LinkedIn: {linkedin_link}\n")
    print(objective + "\n")
    print("Education:")
    for edu in education:
        print(f"\n- {edu['degree']}")
        print(f"  {edu['institution']}")
        print(f"  Batch/Year of Completion: {edu.get('batch', edu.get('year_of_completion', 'N/A'))}")
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")
    print("\nProjects:")
    for project in projects:
        print(f"\n- {project['name']}")
        print(f"  {project['description']}")
    print("\n" + contributions)
    print("\n" + achievements)
    print("\n" + perform_better)

    # Ending Quote in Sanskrit
    print("========== Quote ==========")
    print("\033[91mतमसो मा ज्योतिर्गमय।\033[0m")
    print("Translation: Lead me from darkness to light.\n")

# Call the function to display the resume
display_resume()
