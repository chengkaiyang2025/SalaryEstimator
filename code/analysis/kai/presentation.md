Hi everyone, today I’d like to introduce our project — a salary prediction tool for students.

Many UVic Computer Science students are looking for internships or their first job — especially international students.
But sometimes, they really don’t know what salary to expect.

They might have questions like:

- How much can I earn with my current skills?

- If I want to be a full-stack developer or data analyst, how does salary change in different cities or with different skills?

---
We developed an online webpage that allows users to predict their salary based on their personal information, 
such as education level, years of experience, and work location.

Now I’d like to show you our demo website.

This is an online salary prediction tool we built for students.

Let’s try an example.

Suppose I’m a student with a Bachelor’s degree, 1 year of experience, and I want to work in Vancouver as a full-stack developer.
I’ll also choose some common skills like Python and JavaScript.

Once I click "Submit", the model gives me a predicted salary based on real-world data 

about one hundred nine K one year

This helps international students get a better sense of what to expect in the job market,
and even simulate “what-if” scenarios — 

for example, as an internation student, if I go back to China , what salary I will get ? 

about one hundred and 21 K one year

Let me walk you through our project workflow.
We split it into three parts:

**First**, we started with only one dataset We did data cleaning and analysis in Google Colab
 just to understand what features might be useful, and also remove outliers or missing values.

**Second**, we selected key features like working experience, education level, and job location.
At the same time,we can start build the web application, those features will be user input.

**Third**, 
Then we trained different models — like decision tree or linear regression, and we choose one of our models,
and export it as  a `.pkl` file.

And we can use these pkl file to predict online.

This whole process is repeatable.
If we get more data or find better model settings, we always update the website with the new model step by step.

---

