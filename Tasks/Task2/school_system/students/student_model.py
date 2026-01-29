class Student:
    def __init__(self, id, name, courses=None):
        self.id = id
        self.name = name
        self.courses = courses if courses else []  

    def enroll(self, course):
        self.courses.append(course.title)

    def list_courses(self):
        return [course.title for course in self.courses]
    
    def __str__(self):
        course_titles = ', '.join(self.list_courses()) if self.courses else "No courses"
        return f"Student(ID: {self.id}, Name: {self.name}, Courses: {course_titles})"

