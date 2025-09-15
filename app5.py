course = "Python Programming"
course_strip_example = "    Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
# strip() removes both leading and trailing whitespace, not just trailing.
print(course_strip_example.strip())
# .find("pro") searches for the substring "pro" inside "Python Programming".
print(course.find("pro"))
# .find("Pro") will recognize "Python Programming"
print(course.find("Pro"))
print(course.replace("P", "x"))
# The "in" operator checks if the substring "Pro" exists in the string.
# Returns True if found, False if not.
print("Pro" in course)
print(course_strip_example.rstrip())
print(course_strip_example.strip())
