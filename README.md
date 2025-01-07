# **Calmora - AI-Powered Mental Health Diagnosis System**

---

## **Tagline**  
*Empowering mental health through AI-driven insights and personalized care.*

---

## **Table of Contents**  
1. [Introduction](#introduction) 
2. [Figma Design](#figma-design)
3. [Features](#features)  
4. [Technologies Used](#technologies-used)  
5. [Dataset](#dataset)  
6. [System Architecture](#system-architecture)  
7. [Model Workflow](#model-workflow)  
8. [Implementation Details](#implementation-details)  
9. [Results](#results)  
10. [Installation](#installation)  
11. [Usage](#usage)  
12. [Future Enhancements](#future-enhancements)  
13. [Contributing](#contributing)  
14. [License](#license)  

---

## **Introduction**  
The **AI-Powered Mental Health Diagnosis System** is designed to bridge the gap in mental health services by offering an intelligent platform for mental health assessment, mood tracking, and personalized recommendations. This system leverages advanced Machine Learning and NLP to empower users in taking proactive steps toward better mental health.

![Introduction Diagram](./assets/introduction_diagram.png)

---
## **Objectives**
- Develop an AI-powered system for accurate and early mental health diagnosis.
- Integrate machine learning and NLP for real-time mood monitoring and sentiment analysis.
- Provide users with personalized recommendations and insights to improve mental health.
- Ensure compliance with global privacy regulations (GDPR, HIPAA).

---

## **Summary**
Mental health challenges require innovative solutions to complement traditional diagnosis methods. This project leverages:
- **Machine Learning Models** for sentiment and emotion detection.
- **Natural Language Processing** for linguistic analysis.
- **Real-Time Monitoring** through integration with wearable devices and external data sources.

The system’s features include an interactive chatbot, self-assessment tools, personalized mental health recommendations, and secure cloud storage for user data.

---

## **Figma Design**
The user interface of this project was designed using Figma. You can view the complete design by clicking the link below:

[View the complete Figma design here](https://www.figma.com/community/file/1451309568741892229/calmora-ai-powered-mental-health-diagnosis-system)

If you find the design helpful or inspiring, please **like** and **leave a comment** on the Figma page. This helps me know that my design is appreciated and motivates me to create more amazing projects!

---

## **Features**  

### **Before Login Features**  
1. **Landing Page**  
   - Interactive UI with a “Find Out More” button redirecting to the Services page.  
   - Demo Button opens the AI Chatbot for user interaction.  
   - Navigation bar functional across all pre-login pages.  

2. **AI Chatbot**  
   - Engages users by asking relevant questions and providing insights.  
   - Prompts users to sign up/login for personalized services.  

### **After Login Features**  
1. **Dashboard**  
   - Personalized mental health overview.  
   - Mood trends, stress analysis, and alerts.

2. **Mood Assessments**  
   - AI-based real-time mood tracking.  
   - Sentiment analysis for emotional insights.  

3. **Progress Reports**  
   - Tracks mental health trends and highlights AI predictions.  

4. **Recommendations**  
   - Personalized tips for stress relief, mindfulness, and better sleep.  

5. **Relaxation Tools**  
   - Music therapy and guided meditation sessions.  

6. **Mood Diary**  
   - Logs user inputs and generates mood-based recommendations.  

7. **Guided Workout Exercises**  
   - Tailored yoga and breathing exercises for stress relief.  

8. **Contact and Subscribe**  
   - Sends notifications and reminders for self-assessments.  

9. **Settings and Profile**  
   - Edit profile, manage subscriptions, and sync wearable data.  

---


## **Technologies Used**

### **Frontend**
- **Django Templates**: Used for dynamic HTML rendering.
- **Bootstrap**: For responsive UI design.

### **Backend**
- **Django**: Python-based backend framework.
- **Django REST Framework (DRF)**: For API development.
- **MySQL**: Primary database for production.
- **SQLite**: Used for local development.

### **Machine Learning**
- **TensorFlow/Keras**: For model training and deployment.
- **Hugging Face Transformers (BERT)**: For NLP-based sentiment analysis.
- **Scikit-learn**: For predictive modeling and evaluation.
- **Pandas/NumPy**: For data manipulation and analysis.

### **Cloud Deployment**
- **AWS EC2**: For hosting the application.
- **Heroku**: For staging and deployment.
- **Docker**: For containerizing the application.

### **Other Tools**
- **Gunicorn**: For managing the application server.
- **Whitenoise**: For static file management in Django.
- **Figma**: For UI/UX design and prototyping.

---

## **Dataset**  
- **Sources**: Publicly available mental health datasets and user-provided inputs.  
- **Features**:  
  - **Input**: Mood, stress levels, heart rate, sleep patterns.  
  - **Output**: AI-based recommendations and insights.  
- **Visualization**:  

![Dataset Diagram](./assets/dataset_structure.png)

---

## **System Architecture**  
![System Architecture](./assets/system_architecture.png)  
- **Components**:  
  - Frontend: django Template 
  - Backend: Django  
  - Database: SQLlite3
  - Deployment: Heroku / EC2 

---

## **Model Workflow**  
![Model Workflow](./assets/model_workflow.png)  
- **Steps**:  
  1. Data Preprocessing (missing values, normalization).  
  2. Sentiment Analysis (NLP-based models).  
  3. AI Recommendation Model.  
  4. Result Delivery and User Feedback.  

---

## **Implementation Details**  
- **Preprocessing**:  
  - Cleaning, normalizing, and handling user inputs.  
- **Model Training**:  
  - Sentiment Analysis using Naive Bayes and Hugging Face Transformers.  
  - Decision Trees for recommendation logic.  
- **Deployment**:  
  - Hosted on Heroku with backend APIs.  

---

## **Results**  
- **Metrics**:  
  - Accuracy: 92%  
  - Precision: 89%  
  - Recall: 90%  

![Results Graph](./assets/results_graph.png)

## **Screenshots**
### Home Page
*(Include screenshot here)*

### Self-Assessment Tool
*(Include screenshot here)*

### Chatbot Interaction
*(Include screenshot here)*

### Dashboard
*(Include screenshot here)*

---
## **Hosting Link**
*(Insert hosting link here)*
---

Here’s the updated **Installation** section for a Python Django project:

---

## **Installation**  

### Prerequisites  
1. **Python** (v3.8 or higher)  
2. **pip** (Python package manager)  
3. **Django** (v4.0 or higher)  
4. **Virtual Environment** (recommended)  
5. **Database**: MySQL or SQLite (pre-configured in the project)  

### Steps  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/username/calmora.git  
   cd calmora  
   ```

2. **Create and Activate a Virtual Environment**  
   - Create the virtual environment:  
     ```bash
     python -m venv venv
     ```  
   - Activate the virtual environment:  
     - On Windows:  
       ```bash
       venv\Scripts\activate
       ```  
     - On macOS/Linux:  
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**  
   - Open the `settings.py` file in the `calmora` directory and configure the database settings (e.g., MySQL credentials).  
   - If you’re using SQLite, it is already pre-configured.

5. **Apply Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser** (Admin Account)  
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**  
   - Open your browser and go to:  
     - Localhost: `http://127.0.0.1:8000`  

---

## **Usage**  
- **Steps**:  
  1. Open the application and sign up/login.  
  2. Navigate through the dashboard to access features.  
  3. Use the AI chatbot for recommendations.  
  4. Log moods in the Mood Diary for insights.  

![Usage UI](./assets/ui_wireframe.png)

---

## **Future Enhancements**  
- **Advanced Machine Learning Models** for mood predictions.  
- **Integration** with wearable devices for real-time data.  
- Enhanced UI/UX designs.  

---

## **Contributing**  
1. Fork this repository.  
2. Create a new branch for your feature/bug fix.  
3. Submit a pull request.  

---

## **License**  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

## **Contact**  
- **Sanala Bala Sree Varsha (Team Lead)**:  
- **Parasa Hari Sai (Team Member 1)**: [harisaiparasa@gmail.com]  
- **Sathiri Vyshnavi (Team Member 2)**:  
- **Karumuru Jahnavi (Team Member 3)**:  

--- 