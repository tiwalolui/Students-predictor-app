<<<<<<< HEAD
🎓 Student Performance Prediction (Machine Learning Project)

Project Overview

This project explores how different factors affect student academic performance using machine learning.

The goal is to:

- Analyze student data
- Build predictive models
- Understand which features truly influence performance

---

Dataset

The dataset includes features such as:

- Study time
- Number of past failures
- Absences
- Parental education level
- Free time
- Previous exam scores (G1, G2)

---

Models Built

1. Linear Regression (Study Time Only)

- Result: Very poor performance (negative R²)
- Insight: Study time alone is not enough to predict performance

---

2. Linear Regression (Real-world Features Only)

Features used:

- Study time

- Failures

- Absences

- Parental education

- Result:
  
  - R² ≈ 0.05
  - High error

- Insight:
  These features have weak correlation with final score and provide low predictive power.

---

3. Linear Regression (Including G1 & G2)

Features used:

- Study time

- G1 (first exam score)

- G2 (second exam score)

- Result:
  
  - R² ≈ 0.80
  - Much lower error

- Insight:
  Past academic performance is a strong predictor of final performance.

---

Key Learnings

- Feature selection is critical in machine learning
- Weak features lead to poor model performance
- Strong features (like past scores) significantly improve predictions
- Adding more features does not always improve performance
- Data leakage can occur when using features that may not be available in real-world scenarios



Conclusion

Model performance depends heavily on the quality and relevance of input features.

While lifestyle and environmental factors have some influence, they are weak predictors compared to direct academic indicators like previous test scores.



Future Improvements

- Build classification model (pass/fail prediction)
- Deploy model as a web app
- Perform feature scaling and advanced feature engineering
=======
# Students-predictor-app
>>>>>>> b02f01b6fcff5af293bcbc9696dc9d8ad6b44002
