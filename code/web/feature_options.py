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
        'I don\'t know',
        'Just me - I am a freelancer, sole proprietor, etc.'
    ],
    'ExperienceLevel': [
        'Beginner',
        'Expert',
        'Intermediate'
    ],
    'Country': [
        'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
        'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia, Plurinational State of',
        'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Cabo Verde', 'Cambodia',
        'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'Congo', 'Congo, The Democratic Republic of the',
        'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', "Côte d'Ivoire", 'Denmark', 'Dominican Republic',
        'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia', 'Germany',
        'Ghana', 'Greece', 'Guatemala', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India',
        'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy',
        'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', "Korea, Democratic People's Republic of",
        'Korea, Republic of', 'Kosovo', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic",
        'Latvia', 'Lebanon', 'Lesotho', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi',
        'Malaysia', 'Maldives', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia',
        'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand',
        'Nicaragua', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestine, State of',
        'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
        'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia',
        'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland',
        'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Trinidad and Tobago',
        'Tunisia', 'Turkmenistan', 'Türkiye', 'Uganda', 'Ukraine', 'United Arab Emirates',
        'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela, Bolivarian Republic of',
        'Viet Nam', 'Yemen', 'Zambia', 'Zimbabwe'
    ],
    'DevType': [
        'Academic researcher', 'Blockchain', 'Cloud infrastructure engineer', 'Data engineer',
        'Data or business analyst', 'Data scientist or machine learning specialist', 'Database administrator',
        'Designer', 'DevOps specialist', 'Developer Advocate', 'Developer Experience', 'Developer, AI',
        'Developer, QA or test', 'Developer, back-end', 'Developer, desktop or enterprise applications',
        'Developer, embedded applications or devices', 'Developer, front-end', 'Developer, full-stack',
        'Developer, game or graphics', 'Developer, mobile', 'Educator', 'Engineer, site reliability',
        'Engineering manager', 'Hardware Engineer', 'Marketing or sales professional',
        'Other (please specify):', 'Product manager', 'Project manager', 'Research & Development role',
        'Scientist', 'Security professional', 'Senior Executive (C-Suite, VP, etc.)', 'Student',
        'System administrator'
    ],
    'Employment': [
        'Employed, full-time', 'Employed, part-time', 'Independent contractor, freelancer, or self-employed',
        'Not employed, and not looking for work', 'Not employed, but looking for work', 'Retired',
        'Student, full-time', 'Student, part-time'
    ],
    'Languages': [
        'Apex', 'Assembly', 'Bash/Shell (all shells)', 'C', 'C#', 'C++', 'Clojure', 'Dart', 'Delphi',
        'Elixir', 'Erlang', 'F#', 'Fortran', 'GDScript', 'Go', 'Groovy', 'HTML/CSS', 'Haskell', 'Java',
        'JavaScript', 'Julia', 'Kotlin', 'Lisp', 'Lua', 'MATLAB', 'MicroPython', 'Objective-C', 'PHP',
        'Perl', 'PowerShell', 'Python', 'R', 'Ruby', 'Rust', 'SQL', 'Scala', 'Solidity', 'Swift',
        'TypeScript', 'VBA', 'Visual Basic (.Net)', 'Zig'
    ]
} 