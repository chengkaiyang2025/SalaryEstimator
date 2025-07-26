# All possible options for one-hot encoded features
all_options = {
    'EdLevel': [
        'Bachelor\'s degree (B.A., B.S., B.Eng., etc.)',
        'Master\'s degree (M.A., M.S., M.Eng., MBA, etc.)',
        'Primary/elementary school',
        'Professional degree (JD, MD, Ph.D, Ed.D, etc.)',
        'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
        'Some college/university study without earning a degree',
        'Something else'
    ],
    'RemoteWork': [
        'In-person',
        'Remote'
    ],
    'OrgSize': [
        '10 to 19 employees',
        '10,000 or more employees',
        '100 to 499 employees',
        '2 to 9 employees',
        '20 to 99 employees',
        '5,000 to 9,999 employees',
        '500 to 999 employees',
        # 'I don\'t know',
        'Just me - I am a freelancer, sole proprietor, etc.'
    ],
    'ExperienceLevel': [
        'Beginner',
        'Expert',
        'Intermediate'
    ],
    'Country': [
        # Top 20 countries by GDP, ensuring at least 1 from each continent
        'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'Japan', 'Korea, Republic of', 'Netherlands', 'Philippines', 'Singapore', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States'

    ],
    'DevType': [
        'Academic researcher', 
        'Blockchain', 
        'Cloud infrastructure engineer', 
        'Data engineer',
        'Data or business analyst', 
        'Data scientist or machine learning specialist', 
        'Database administrator',
        'Designer', 
        'DevOps specialist', 
        'Developer Advocate', 
        'Developer Experience', 
        'Developer, AI',
        'Developer, QA or test', 
        'Developer, back-end', 
        'Developer, desktop or enterprise applications',
        'Developer, embedded applications or devices',
         'Developer, front-end', 
         'Developer, full-stack',
        'Developer, game or graphics',
         'Developer, mobile', 
        # 'Educator', 
         'Engineer, site reliability',
        'Engineering manager', 
        'Hardware Engineer', 
        # 'Marketing or sales professional',
        #'Other (please specify):', 
        # 'Product manager', 
        #'Project manager', 
        'Research & Development role',
        
        'Scientist', 
        'Security professional', 
        'Senior Executive (C-Suite, VP, etc.)', 
        # 'Student',
        'System administrator'
    ],
    'Employment': [
        'Employed, full-time', 
        'Employed, part-time', 
        'Independent contractor, freelancer, or self-employed',
        # 'Not employed, and not looking for work', 
        #'Not employed, but looking for work', 
        # 'Retired',
        'Student, full-time', 
        'Student, part-time'
    ],
    'Languages': [
        'Apex', 'Assembly', 'Bash/Shell (all shells)', 'C', 'C#', 'C++', 'Clojure', 'Dart', 'Delphi',
        'Elixir', 'Erlang', 'F#', 'Fortran', 'GDScript', 'Go', 'Groovy', 'HTML/CSS', 'Haskell', 'Java',
        'JavaScript', 'Julia', 'Kotlin', 'Lisp', 'Lua', 'MATLAB', 'MicroPython', 'Objective-C', 'PHP',
        'Perl', 'PowerShell', 'Python', 'R', 'Ruby', 'Rust', 'SQL', 'Scala', 'Solidity', 'Swift',
        'TypeScript', 'VBA', 'Visual Basic (.Net)', 'Zig'
    ]
} 