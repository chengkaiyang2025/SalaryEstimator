# Problem description and motivation
## Background
Many UVic Computer Science students are seeking their first job or internship. 
However, many of them do not have a clear understanding of the salary they might expect given their current skill sets,or how their potential salary could grow over the next 3 to 5 years if they pursue roles such as data analyst or full-stack developer.
## motivation

Salary is often considered a sensitive topic. Without real industry experience, students may struggle to estimate their future salary range. 

Additionally, they may be unsure which skills or types of experience would lead to better pay in the job market.

We propose building a web application that helps students evaluate their potential salary based on their current skills, experience, job type, and location. This tool can guide students in planning their learning path more strategically to maximize their future income.

Suppose a student has some knowledge of Python, Go, Java, SQL, JavaScript, and machine learning. They are unsure which skills to learn next. Our website would allow them to:

* Enter their current skill set (e.g., Python, JS, SQL) and other information (e.g., years of experience, education level, location)
* Get an estimated salary for a junior full-stack engineer with those skills

They could also simulate “what-if” scenarios:

* What if they had 2 years of experience in TypeScript, 1 year in Kotlin, and 2 years in React? What would be their expected salary in Toronto?
* What if they had 1 year of PyTorch, 1 year of Spark, plus TensorFlow and Power BI experience? What could they earn in Vancouver?

### ML techniques in this problem

This is essentially a salary prediction problem, which requires modeling complex relationships between skill sets, experience, location, and salary. Machine learning, especially linear regression, can learn from existing datasets to make salary predictions.

Additionally, explainable AI techniques can help users understand why the model made a certain prediction, by showing similar data samples or feature contributions.

# Related work (150 word)
@Archana
# Problem Formulation (450 word)

### Objective Function:

We aim to predict a student's salary based on their skill set, experience, location, and job type using a linear regression model.
The objective is to minimize the loss function:

$$
\min_{w,b} \sum_{i=1}^n (y_i - (w^T x_i + b))^2
$$

where $y_i$ is the actual salary, $x_i$ is the feature vector (skills, experience, etc.), and $w$, $b$ are model parameters.

### Search Space:

Each student’s background (skills, years of experience, education level, city, etc.) is encoded as a feature vector of dimension $d$.
The model will learn $d+1$ parameters ($w$ and $b$). Therefore, the search space is $\mathbb{R}^{d+1}$.

### Output Space:

The output is a continuous value representing the predicted salary.

# Methodology and Evaluation (600 words)
## Well-defined approach to solve the problem 
@Chaoran @Archana
## Accurate and precise evaluation of your solution 
@Chaoran @Archana
## Sufficient experiments to validate your results
@Chaoran @Archana
# Results and discussion (750 words)
## Comparisons (op2mal solu2on, previous solu2ons, and/or your solu2on improvement)
[ @Chaoran @Archana Copy from @Charina's slide] and add more details   
## Use graphs, charts, and/or tables to effectively display results
[ @Chaoran @Archana Copy from @Charina's slide] and add more details     
## Justify the obtained results
[ @Chaoran @Archana Copy from @Charina's slide] and add more details     
## Challenges faced and how did you overcome them
@Charina


# Conclusion and future work (150)
@Kai
# Proper cita2ons in your report (150 words)
@Archana


# Code: (20%)
@Kai
- https://github.com/chengkaiyang2025/SalaryEstimator
• Source code quality [10%]
• Run and compile [10%]
