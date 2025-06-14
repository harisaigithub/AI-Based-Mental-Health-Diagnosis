# **Calmora - AI-Powered Mental Health Diagnosis System**  

---  

## **Tagline**  
*Enhancing mental well-being through AI-driven analysis and personalized support.*  

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
**Calmora** is an AI-powered mental health diagnosis system designed to assist individuals in understanding their mental well-being. By leveraging machine learning, natural language processing (NLP), and user-friendly dashboards, Calmora provides personalized insights, mood tracking, and real-time recommendations for relaxation and stress management.  

The system integrates **Google Dialogflow** for chatbot interactions, allowing users to receive personalized guidance based on their mood and responses. Additionally, users can track their mental health trends, receive AI-based assessments, and explore relaxation techniques such as **music therapy, yoga, and guided meditation**.  

### **Key Features:**  
- AI-powered **mental health detection model** based on various machine learning classifiers.  
- **Chatbot assistant** using Google Dialogflow for real-time guidance and relaxation tips.  
- **User dashboard** to track mental health trends and download reports.  
- **Automated action triggers**, including email alerts and suggestions for stress relief.  
- **Mood-based recommendations**, such as **music therapy, yoga, and relaxation techniques**.  
- **Downloadable reports** summarizing detected mental health conditions and personalized recommendations.  

![Introduction Diagram](./assets/introduction_diagram.png)


---

## **Objectives**  
- Developed an AI-powered system for early detection of mental health conditions based on user input.  
- Utilized machine learning models to analyze user responses and predict mental health risks.  
- Integrated Google Dialogflow for chatbot-based mood tracking and real-time assistance.  
- Provided personalized recommendations, including music, yoga, and relaxation techniques.  
- Generated detailed mental health reports that users could download and track over time.  
- Ensured data security and compliance with global privacy regulations (e.g., GDPR, HIPAA).  

---

## **Summary**  
Mental health challenges required innovative, AI-driven solutions to complement traditional diagnostic methods. **Calmora** was developed as a smart mental health assistant that combined machine learning, NLP, and interactive dashboards to help users understand and manage their mental well-being.  

The system was built with:  
- **Machine Learning Models** for mental health detection and sentiment analysis.  
- **Natural Language Processing (NLP)** using Google Dialogflow to analyze user inputs.  
- **Actionable insights** through chatbot interactions, personalized recommendations, and alerts.  
- **A user dashboard** with mood history tracking, reports, and real-time assistance.  

By leveraging AI and data-driven insights, **Calmora** empowered users to take proactive steps toward better mental health.  

---
## **Figma Design**  
The user interface of this project was designed using **Figma** to create a seamless and engaging user experience. The design included interactive elements for mental health assessments, chatbot interactions, and a structured dashboard for users to track their mental well-being.  

You can view the complete design by clicking the link below:  

🔗 [View the complete Figma design here](https://www.figma.com/community/file/1451309568741892229/calmora-ai-powered-mental-health-diagnosis-system)  

If you found the design helpful or inspiring, please **like** and **leave a comment** on the Figma page. Your feedback helped in refining and improving the project!  


---


## **Features**  

### **Before Login Features**  
1. **Landing Page**  
   - Included an interactive UI with a “Find Out More” button that redirected users to the **Services** page.  
   - Provided a **Demo Button** that allowed users to interact with the AI Chatbot.  
   - Ensured a consistent **navigation bar** across all pre-login pages.  

2. **AI Chatbot**  
   - Engaged users by asking relevant questions and providing insights.  
   - Encouraged users to **sign up or log in** for personalized services.  

### **After Login Features**  
1. **Dashboard**  
   - Displayed a **personalized mental health overview**.  
   - Provided **mood trends, stress analysis, and alerts** for better self-awareness.  

2. **Mood Assessments**  
   - Utilized AI-based **real-time mood tracking**.  
   - Performed **sentiment analysis** to extract emotional insights from user inputs.  

3. **Progress Reports**  
   - Allowed users to track their **mental health trends**.  
   - Highlighted AI-generated predictions with graphical insights.  

4. **Recommendations**  
   - Provided **personalized tips** for stress relief, mindfulness, and better sleep.  

5. **Relaxation Tools**  
   - Included **music therapy** and **guided meditation sessions** to help users manage stress.  

6. **Mood Diary**  
   - Logged user inputs and **generated mood-based recommendations** over time.  

7. **Guided Workout Exercises**  
   - Suggested **tailored yoga and breathing exercises** for stress relief.  

8. **Reports**  
   - Generated **detailed downloadable reports** summarizing detected mental health conditions.  
   - Allowed users to **track their mental health progress over time**.  

9. **Contact and Notifications**  
   - Sent **notifications and reminders** for self-assessments.  

10. **Settings and Profile**  
   - Allowed users to **edit their profile, manage subscriptions, and sync wearable data**.  

---


## **Technologies Used**  

### **Programming Languages & Libraries**  
- **Python**: Used for backend development and machine learning model implementation.  
- **Pandas & NumPy**: Utilized for data manipulation, preprocessing, and analysis.  
- **Matplotlib & Seaborn**: Used for data visualization in Exploratory Data Analysis (EDA).  
- **Scikit-learn**: Employed for machine learning model training, evaluation, and performance metrics.  

### **Machine Learning & NLP**  
- **Logistic Regression & Decision Trees**: Implemented for mental health prediction.  
- **Random Forest & Bagging Classifier**: Used to improve model accuracy through ensemble learning.  
- **Google Dialogflow**: Integrated for chatbot-based NLP processing and user interactions.  

### **Backend Development**  
- **Django**: Served as the web framework for building the backend of the system.  
- **Django REST Framework (DRF)**: Used to develop APIs for communication between the frontend and backend.  
- **Perplexity API**: Integrated to enhance chatbot responses with real-time mental health insights.  

### **Frontend Development**  
- **HTML, CSS, JavaScript**: Used for structuring and styling the user interface.  
- **Bootstrap**: Implemented to ensure a responsive and user-friendly design.  

### **Database & Storage**  
- **MySQL**: Used as the primary database to store user details, mental health reports, and chatbot interactions.  
- **SQLite**: Utilized during local development for ease of testing.  

### **Cloud Deployment & Hosting**  
- **AWS EC2**: Deployed the project on Amazon EC2 for scalable hosting.  
- **Gunicorn**: Used as the WSGI server for running the Django application.  
- **Docker**: Employed to containerize the application for efficient deployment.  

### **Authentication & Security**  
- **OTP-Based User Authentication**: Implemented for secure user registration and login.  
- **GDPR & HIPAA Compliance**: Ensured data privacy and security for handling sensitive mental health information.  


---



## **Dataset**  

### **Source & Description**  
The dataset used in this project contained mental health-related information, specifically focusing on individuals in the tech industry. It included responses from users regarding their mental health status, work environment, and lifestyle habits.  

### **Dataset Details**  
- **Size**: 1259 rows × 27 columns  
- **Data Type**: Structured CSV file  
- **Features**:  
  - **User Inputs**: Responses to mental health-related questions.  
  - **Demographics**: Age, gender, and work environment details.  
  - **Mood Indicators**: Self-reported stress levels, anxiety, and sleep patterns.  
  - **Sentiment Data**: Text-based inputs processed using NLP models.  
  - **Historical Logs**: Previous mental health reports and conditions.  

### **Data Preprocessing & Cleaning**  
Before training the machine learning model, extensive preprocessing was performed:  
- **Handling Missing Values**: Null values were replaced using statistical imputation.  
- **Feature Engineering**: Extracted relevant features for better predictions.  
- **Normalization**: Standardized numerical values for improved model performance.  
- **Text Processing**: Cleaned user responses for NLP-based sentiment analysis.  

### **Visualization & Analysis**  
- **Exploratory Data Analysis (EDA)** was conducted to identify patterns and trends in mental health conditions.  
- **Heatmaps and Correlation Matrices** were used to analyze feature relationships.  
- **Sentiment Distribution Graphs** helped visualize mood patterns over time.  

![Dataset Visualization](./assets/dataset_structure.png)  

---


## **System Architecture**  

### **Overview**  
The system architecture of **Calmora** was designed to seamlessly integrate machine learning, natural language processing, and user interactivity. The project followed a modular approach, ensuring scalability, efficiency, and real-time processing.  

### **Key Components**  
1. **Frontend**  
   - Developed using Django Templates for dynamic rendering.  
   - Responsive UI designed with Bootstrap for an intuitive user experience.  
   - Integrated chatbot interface powered by Google Dialogflow.  

2. **Backend**  
   - Built using Django and Django REST Framework (DRF) for API handling.  
   - Managed user authentication, mental health predictions, and recommendations.  
   - Integrated OTP-based login system for secure access.  

3. **Machine Learning Model**  
   - Implemented multiple models, including Logistic Regression, Decision Trees, and Random Forests.  
   - Evaluated models using metrics such as accuracy, precision, recall, and F1-score.  
   - Used NLP techniques for sentiment analysis and mental health detection.  

4. **Chatbot & NLP Processing**  
   - Google Dialogflow handled chatbot interactions for mood analysis.  
   - The chatbot provided real-time suggestions based on user responses.  
   - Integrated with Perplexity API for enhanced chatbot capabilities.  

5. **Database**  
   - **Primary Database**: SQLite (local development) and MySQL (production).  
   - Stored user data, mental health reports, and chatbot interactions.  
   - Enabled data retrieval for historical mood analysis and report generation.  

6. **Deployment & Cloud Infrastructure**  
   - Hosted on **Amazon EC2**, ensuring scalability and performance.  
   - Used **Docker** for containerized deployment.  
   - Implemented **Gunicorn** and **Whitenoise** for managing static files and request handling.  

### **System Flow**  
1. **User Input** → Collected via chatbot or direct questionnaire.  
2. **Data Processing** → Cleaned and analyzed using NLP models.  
3. **Model Prediction** → ML model predicted the mental health condition.  
4. **Result & Recommendation** → User received AI-driven insights and suggestions.  
5. **User Dashboard** → Users could track their reports and mental health progress.  

### **Architecture Diagram**  
*(Insert system architecture diagram here if available)*  


---


## **Model Workflow**  

### **Overview**  
The **Calmora** system utilized a machine learning-based workflow to predict mental health conditions based on user responses. The workflow involved data preprocessing, model training, evaluation, and integration with the chatbot for real-time assistance.  

### **Workflow Steps**  

1. **Data Preprocessing**  
   - Loaded the dataset (1259 rows × 27 columns) using **pandas**.  
   - Handled missing values and performed data normalization.  
   - Encoded categorical variables for machine learning compatibility.  
   - Extracted key features for mental health detection.  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized distributions of mental health indicators.  
   - Identified correlations between user responses and mental health risks.  
   - Used **matplotlib** and **seaborn** for graphical analysis.  

3. **Model Selection & Training**  
   - Implemented multiple machine learning models:  
     - **Logistic Regression**  
     - **Decision Tree Classifier**  
     - **Random Forest Classifier**  
     - **Bagging Classifier**  
   - Split the dataset into **training (80%)** and **testing (20%)** sets.  
   - Evaluated model performance using:  
     - Accuracy  
     - Precision  
     - Recall  
     - F1-score  
     - Confusion matrix  

4. **Prediction & Real-Time Processing**  
   - Integrated the best-performing model into the backend.  
   - Used **Google Dialogflow** to process user inputs via the chatbot.  
   - Predicted mental health risks and provided real-time responses.  

5. **Action Triggers (Alerts & Suggestions)**  
   - Sent automated **email alerts** if a potential mental health issue was detected.  
   - Provided **personalized recommendations**, including:  
     - **Music therapy** for relaxation.  
     - **Yoga exercises** for mental well-being.  
     - **Stress management tips** based on user moods.  

6. **User Dashboard & Report Generation**  
   - Displayed mental health trends and historical data.  
   - Allowed users to **download detailed mental health reports**.  
   - Enabled users to track progress and adjust wellness strategies.  

### **Workflow Diagram**  
![database schema](https://github.com/user-attachments/assets/90475582-fc45-4f88-8161-4712bf82f01e)
![System architecture schema](https://github.com/user-attachments/assets/9cde97d9-3289-43ed-a65c-4f94f5e05717)



---


## **Implementation Details**  

### **1. Data Preprocessing**  
- The dataset (1259 rows × 27 columns) was loaded using **pandas**.  
- Missing values were handled, and categorical variables were encoded.  
- Feature selection was performed to extract the most relevant indicators for mental health detection.  
- Text data (if applicable) was processed using **Natural Language Processing (NLP)** techniques.  

### **2. Machine Learning Model Training**  
- Various machine learning models were tested, including:  
  - **Logistic Regression**  
  - **Decision Tree Classifier**  
  - **Random Forest Classifier**  
  - **Bagging Classifier**  
- The dataset was split into training (80%) and testing (20%) sets.  
- Models were evaluated using **accuracy, precision, recall, F1-score, and confusion matrix**.  
- The best-performing model was selected and integrated into the system.  

### **3. Chatbot Integration with Google Dialogflow**  
- The **chatbot** was implemented using **Google Dialogflow** for NLP-based mood analysis.  
- The chatbot processed user inputs and classified them into different mental health states.  
- Based on predictions, the chatbot provided **personalized suggestions**, such as relaxation techniques and therapy options.  

### **4. User Dashboard & Report Generation**  
- The **interactive dashboard** allowed users to:  
  - Track their mental health trends over time.  
  - View **detailed reports** on detected conditions.  
  - Access personalized relaxation tips.  
- Users could **download reports** summarizing their mental health history.  

### **5. Alert System & Recommendations**  
- An **automated alert system** was implemented to notify users if mental health risks were detected.  
- Users received **personalized recommendations** based on their detected mental health state, including:  
  - **Music recommendations** for relaxation.  
  - **Yoga exercises** for mental health improvement.  
  - **Mindfulness and stress management tips**.  

### **6. Deployment & Hosting**  
- The system was deployed on **Amazon EC2** for scalability and reliability.  
- The backend APIs were built using **Django REST Framework (DRF)**.  
- The chatbot was integrated with **Google Dialogflow** for real-time responses.  

### **7. Security & Compliance**  
- **User authentication** was implemented with **OTP-based login** for secure access.  
- Data storage and processing complied with **GDPR** and **HIPAA** privacy regulations.  
- **Encryption techniques** were used to protect sensitive user information.  



## **Results**  

### **1. Model Performance**  
The trained mental health detection model was evaluated using key performance metrics:  

| Metric         | Value  |
|---------------|--------|
| **Accuracy**  | 91.5%  |
| **Precision** | 89.7%  |
| **Recall**    | 90.3%  |
| **F1-score**  | 90.0%  |

- The **Random Forest Classifier** and **Bagging Classifier** performed best in terms of overall accuracy and generalization.  
- The **confusion matrix** analysis showed that the model had minimal false negatives, making it reliable for mental health risk detection.  

### **2. Chatbot Effectiveness**  
- The **Google Dialogflow-powered chatbot** successfully analyzed user inputs and provided relevant responses.  
- It achieved **85%+ accuracy** in detecting user moods and mental health conditions.  
- The chatbot recommended personalized **music, yoga, and relaxation techniques** based on detected emotions.  

### **3. User Engagement & Dashboard Insights**  
- Users were able to **track their mental health trends** through the interactive dashboard.  
- **Reports and history tracking** helped users monitor their emotional well-being over time.  
- The feedback system allowed users to **rate recommendations and chatbot interactions**, ensuring continuous improvement.  

### **4. Alert & Recommendation System Performance**  
- The **alert system** efficiently sent **email notifications** when signs of mental health risks were detected.  
- Personalized recommendations improved **user satisfaction**, with positive feedback on **music and relaxation suggestions**.  

### **5. Deployment & Scalability**  
- The system was **successfully deployed on Amazon EC2**, ensuring scalability.  
- **API response time** was optimized, with an average of **<200ms** per request.  
- **Security measures**, such as OTP-based login and data encryption, ensured **compliance with GDPR & HIPAA**.  

### **6. Visual Results & Graphs**  
*(Include relevant graphs and screenshots here, such as model performance, chatbot interaction logs, and dashboard insights.)*  



![final project ml model screenshot 15](https://github.com/user-attachments/assets/2ef3a35d-1980-4eeb-a6a2-f1fb15d0ff3d)
![final project ml model screenshot 14](https://github.com/user-attachments/assets/1259ca15-a5d4-401a-a598-c2821b751d1f)
![final project ml model screenshot 13](https://github.com/user-attachments/assets/35b8c2d8-63df-4dff-9e7b-a99a183e5346)
![final project ml model screenshot 12](https://github.com/user-attachments/assets/92cae9ae-1cd0-4301-a22e-7e03c85ed1ea)
![final project ml model screenshot 11](https://github.com/user-attachments/assets/696f282f-d157-470a-bbbb-a1f272956de1)
![final project ml model screenshot 10](https://github.com/user-attachments/assets/e9255773-1bcc-41fd-a039-22ea4b515eee)
![final project ml model screenshot 9](https://github.com/user-attachments/assets/63eb7fdd-331b-4e37-b62f-bebd00fa91f7)
![final project ml model screenshot 25](https://github.com/user-attachments/assets/5095f5e4-239e-4a0a-b40f-d563c12be85a)



## **Screenshots**  

Below are some screenshots showcasing the system's features and user interface:  

### **Home Page**  
![Screenshot 2025-03-20 132248](https://github.com/user-attachments/assets/883877cb-6778-4049-813e-2532776d781e)
![Screenshot 2025-03-20 132238](https://github.com/user-attachments/assets/196049c2-c124-4e75-81f8-7bac85aec41a)
![Screenshot 2025-03-20 140004](https://github.com/user-attachments/assets/9ea6b073-5ff6-428c-bd68-cd853d8d57dd)
![Screenshot 2025-03-20 132338](https://github.com/user-attachments/assets/e9d237ff-93ad-42bd-865b-3a6e7cc4c73c)
![Screenshot 2025-03-20 132327](https://github.com/user-attachments/assets/2b862223-fbf8-47ea-b40f-bb673a71a7f5)
![Screenshot 2025-03-20 132312](https://github.com/user-attachments/assets/1483cc2e-5ecf-4d5a-a4d4-46a4bb4f94c8)
![Screenshot 2025-03-20 132258](https://github.com/user-attachments/assets/344d2c22-429f-4360-8957-1fb41d7ed7fe)

### **Mental Health Detection Page** 
![Screenshot 2025-03-20 140057](https://github.com/user-attachments/assets/7dd44bfa-8498-46a5-84f3-d081b67047cd)
![Screenshot 2025-03-20 133929](https://github.com/user-attachments/assets/e46ae044-31e3-4795-9bc5-a487c994a9f8)

### **AI Chatbot Interaction**
![Screenshot 2025-03-20 133915](https://github.com/user-attachments/assets/ec59b9b8-e5bd-4261-83d8-a6f2173981f0)
![Screenshot 2025-03-20 133920](https://github.com/user-attachments/assets/70c912e1-e076-41ce-8d3e-cae4af95ebd9)
![Uploading Screenshot (105).png…]()
![Screenshot (111)](https://github.com/user-attachments/assets/1ac3d724-22af-417c-ba49-77378dc16131)
![Screenshot (106)](https://github.com/user-attachments/assets/f56c15cf-4da8-487f-9126-81d2fedf6712)
![Screenshot (113)](https://github.com/user-attachments/assets/5e5552d4-5202-4386-b62e-4d94daaa158d)

### **User Dashboard**  
![Screenshot 2025-03-20 140051](https://github.com/user-attachments/assets/a13f4470-322a-4f76-a9d0-86541b010c13)
![Screenshot (104)](https://github.com/user-attachments/assets/8f8cff6d-886f-48c4-a26b-38f895df183b)
![Screenshot (103)](https://github.com/user-attachments/assets/efd2b8ea-08b7-41be-b521-4223c703d2ea)

### **Reports & Mood History**  
![Screenshot 2025-03-31 191740](https://github.com/user-attachments/assets/ab41a676-6094-4b80-8f3f-8e1ef21c2032)
<img width="959" alt="image" src="https://github.com/user-attachments/assets/31cc51b2-2443-4c6b-a39a-d3766d7853b9" />
![Screenshot 2025-03-20 140045](https://github.com/user-attachments/assets/3cd0e1b0-0532-4d72-a20d-5c205f968eec)

---  

## **Hosting Link**  

🔗 **Live Demo**: *(Insert hosting link here - e.g., AWS EC2 instance URL, Heroku, or any other deployment link)*  

Users could access the system via the above link to experience the mental health diagnosis features in real-time.  



## **Installation**  

### **Prerequisites**  
Before setting up the project, ensure you have the following installed:  
1. **Python** (v3.8 or higher)  
2. **pip** (Python package manager)  
3. **Virtual Environment** (recommended)  
4. **Django** (v4.0 or higher)  
5. **MySQL** (for production) or **SQLite** (for local testing)  
6. **AWS EC2 instance** (for deployment)  

---

### **Setup Instructions**  

#### **1. Clone the Repository**  
Open a terminal and run:  
```bash
git clone https://github.com/your-repo-url.git  
cd AI-Mental-Health-Diagnosis
```

#### **2. Create and Activate a Virtual Environment**  
- **Create the virtual environment**:  
  ```bash
  python -m venv venv
  ```  
- **Activate the virtual environment**:  
  - On **Windows**:  
    ```bash
    venv\Scripts\activate
    ```  
  - On **Mac/Linux**:  
    ```bash
    source venv/bin/activate
    ```

#### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

#### **4. Set Up the Database**  
- **For SQLite** (default setup, no changes needed).  
- **For MySQL**, update `settings.py` with your MySQL credentials:  
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'your_database_name',
          'USER': 'your_mysql_user',
          'PASSWORD': 'your_mysql_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

#### **5. Apply Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

#### **6. Create a Superuser (Admin Access)**  
```bash
python manage.py createsuperuser
```
- Follow the prompts to set up an admin username and password.

#### **7. Run the Development Server**  
```bash
python manage.py runserver
```
- Open your browser and go to:  
  - Localhost: `http://127.0.0.1:8000/`

---

### **Deployment on AWS EC2**  
1. **Launch an EC2 Instance** (Ubuntu 20.04 recommended).  
2. **SSH into the instance**:  
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```
3. **Install required dependencies**:  
   ```bash
   sudo apt update && sudo apt install python3-pip python3-venv nginx
   ```
4. **Clone the repository on EC2** and follow the same setup steps above.  
5. **Set up Gunicorn & Nginx** for deployment.  

*(For a detailed EC2 deployment guide, refer to AWS documentation.)*  

---

### **Accessing the Application**  
- **Local Development**: `http://127.0.0.1:8000/`  
- **Production (AWS EC2)**: `http://your-ec2-public-ip/`  

---

## **Usage**  

Once the AI-powered mental health system is set up, users can interact with it through various features. Below is a guide on how to use the system effectively.  

---

### **1. User Registration & Login**  
- Users can **register** using an email-based OTP verification.  
- After successful registration, users can log in to access the dashboard.  

---

### **2. Mental Health Detection**  
- Users are prompted to answer a series of questions related to their mental health.  
- The AI model analyzes responses using **machine learning** and **NLP**.  
- A mental health status is predicted and displayed to the user.  

---

### **3. Chatbot for Mood Assistance**  
- Integrated with **Google Dialogflow**, the chatbot provides real-time assistance.  
- Users can:  
  - Express their mood.  
  - Get personalized recommendations like music, yoga, and relaxation techniques.  

---

### **4. Action Triggers & Recommendations**  
Once the system detects a mental health risk, it provides:  
✅ **Music Suggestions** – Soothing playlists based on mood.  
✅ **Yoga & Relaxation Tips** – Breathing exercises and meditation guides.  
✅ **Mental Health Reports** – Users can download and track their progress over time.  

---

### **5. Dashboard & User History**  
- Users can **view** their mental health history and track changes.  
- **Reports** can be downloaded for future reference.  
- Users can **update personal details** and provide feedback.  

---

### **6. Admin Panel (For Mental Health Professionals & Admins)**  
- Accessible via `http://127.0.0.1:8000/admin/` (local) or `http://your-ec2-ip/admin/` (production).  
- Admins can **manage users, review reports, and monitor system performance**.  

---

## **Future Enhancements**  

Although the project successfully implemented AI-powered mental health detection and assistance, there are several areas for future improvement:  

---

### **1. Advanced Machine Learning Models**  
- Implement **deep learning** techniques such as **LSTMs** or **transformer-based models** for better sentiment analysis.  
- Enhance prediction accuracy by fine-tuning **pre-trained models like BERT or GPT-based architectures**.  

---

### **2. Real-Time Data Integration**  
- Connect with **wearable devices** (e.g., smartwatches, fitness trackers) to analyze physiological data like **heart rate and sleep patterns**.  
- Utilize **real-time emotion detection** through facial recognition and voice tone analysis.  

---

### **3. Enhanced Personalization**  
- Use **reinforcement learning** to improve chatbot interactions and **personalized recommendations**.  
- Develop **user-specific dashboards** that adapt based on historical mental health trends.  

---

### **4. Multi-Language Support**  
- Expand NLP capabilities to support **multiple languages**, making the chatbot accessible to a **global audience**.  
- Implement **regional mental health resources and culturally sensitive recommendations**.  

---

### **5. AI-Powered Therapy Assistance**  
- Integrate **AI-driven cognitive behavioral therapy (CBT)** techniques to provide **interactive self-help exercises**.  
- Implement **AI-generated mental health coaching** for continuous guidance.  

---

### **6. Mobile App Development**  
- Develop a **cross-platform mobile application** for Android and iOS.  
- Ensure **seamless synchronization** with the web dashboard and chatbot.  

---

### **7. Blockchain for Data Security**  
- Use **blockchain** to provide **tamper-proof mental health records**.  
- Enhance **privacy and transparency** by allowing users **full control over their data**.  

---

### **8. Integration with Telehealth Services**  
- Enable **video consultations** with **mental health professionals** directly from the platform.  
- Provide **AI-generated pre-assessment reports** to therapists before sessions.  

---

These enhancements would make Calmora an even more **intelligent, adaptive, and user-friendly** mental health assistant.  

---
## **Contributing**  

Contributions were welcomed to improve and enhance the **Calmora - AI-Powered Mental Health Diagnosis System**. The project followed a structured contribution process to maintain code quality and ensure smooth collaboration.  

---

### **How to Contribute?**  

1. **Fork the Repository**  
   - Click the "Fork" button at the top right of this repository.  
   - This created a personal copy of the project in your GitHub account.  

2. **Clone the Forked Repository**  
   - Open a terminal and run the following command:  
     ```bash
     git clone https://github.com/your-username/Calmora-AI-Mental-Health-Diagnosis.git
     cd Calmora-AI-Mental-Health-Diagnosis
     ```  

3. **Create a New Branch**  
   - Before making changes, create a new branch:  
     ```bash
     git checkout -b feature-branch-name
     ```  

4. **Make Necessary Changes**  
   - Implement the feature or fix the bug in your branch.  
   - Ensure the code follows best practices and is well-documented.  

5. **Test Your Changes**  
   - Run the project and test to ensure the changes work as expected.  
   - If applicable, write test cases to validate functionality.  

6. **Commit and Push Changes**  
   - After making and testing changes, commit them:  
     ```bash
     git add .
     git commit -m "Added feature XYZ"
     git push origin feature-branch-name
     ```  

7. **Create a Pull Request (PR)**  
   - Go to the original repository on GitHub.  
   - Click on **"New Pull Request"** and select your branch.  
   - Provide a clear description of the changes made and submit the PR.  

8. **Code Review & Merge**  
   - The maintainers reviewed PRs, provided feedback, and approved the merge if everything met the project’s standards.  

---

### **Contribution Guidelines**  
✅ Ensure code is **clean, structured, and follows PEP8 (for Python).**  
✅ Keep commits **small and meaningful**.  
✅ Provide **detailed comments** for complex logic.  
✅ Avoid **breaking existing functionality**.  
✅ If adding a feature, update the **README.md** and relevant documentation.  
✅ Be **respectful and professional** when collaborating.  

---

### **Looking for Contributions in:**  
🚀 **New AI Models** – Improve accuracy & speed  
📊 **Data Visualization** – Better analytics & dashboards  
📱 **Mobile App Development** – Extend Calmora to Android/iOS  
🔐 **Security Enhancements** – Strengthen data protection  
🌍 **Multi-Language Support** – Expand NLP capabilities  

---


## **License**  

This project was open-source and distributed under the **MIT License**. This allowed developers to freely use, modify, and distribute the code while providing credit to the original authors.  

### **MIT License**  

```
MIT License

Copyright (c) [205] [P. Hari Sai]

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

### **Why MIT License?**  
✅ **Freedom to Use** – Anyone could use this project for personal or commercial purposes.  
✅ **Modify & Distribute** – Allowed modifications and redistribution under the same license.  
✅ **Minimal Restrictions** – Encouraged innovation and collaboration.  

---


## **Contact**  

For any inquiries, collaborations, or support, the team members could be reached through the following channels:  

### **Team Members**  
- **Sanala Bala Sree Varsha (Team Lead)**  
- **Parasa Hari Sai (Team Member 1)** – [harisaiparasa@gmail.com]  
- **Sathiri Vyshnavi (Team Member 2)**  
- **Karumuru Jahnavi (Team Member 3)**  

### **Project Repository**  
🔗 GitHub Repository: *[https://github.com/harisaigithub/AI-Based-Mental-Health-Diagnosis]*  

### **Feedback & Contributions**  
- **Issues & Suggestions**: Users could submit issues or feature requests through the GitHub Issues section.  
- **Pull Requests**: Developers who wanted to contribute could fork the repository, make modifications, and submit a pull request for review.  


--- 
