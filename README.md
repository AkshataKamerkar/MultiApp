
# Multi-App


The Multi-App Django Application is a versatile project that integrates three distinct applications into a single Django framework. This repository showcases a Chatbot, a Weather App, and a To-Do List App, providing users with a diverse set of functionalities within a unified platform.
## Description


The project allows users to engage in dynamic conversations with a customizable Chatbot, retrieve real-time weather information using web scraping in the Weather App, and efficiently manage tasks with various features in the To-Do List App. 
## Key Features 


**ChatBot** 
    
- Customize the Chatbot's responses and behavior.
- Engage in dynamic conversations with a responsive and adaptable Chatbot.
- Utilize ChatterBot for a more interactive experience.

**Weather App**

- Retrieve accurate weather information through web scraping.
- Customize the Weather App to provide location-specific weather updates.
- Access real-time data including temperature, humidity, and weather conditions.

**To-Do List**

- Add tasks to your to-do list.
- Update task details.
- Mark tasks as complete to track your progress.
- Delete tasks you no longer need.


## Technologies Used 

* **Python :** Core programming language for backend development.
* **Django :** Web framework for rapid development and clean design.
* **Beautiful Soup :** Web scraping for real-time weather information.
* **ChatterBot :** Powers dynamic and customizable chat interactions.
* **Requests :** Simplifies communication with external APIs for weather data.







## Requirements 

To run this project locally, ensure you have Python installed along with the necessary libraries mentioned in the requirements.txt file. You can install these dependencies using :

``` pip install -r requirements.txt ```

## Deployment

Accessing the project involves a few steps:

**Step 1 :** Clone the repository
```
    git clone https://github.com/AkshataKamerkar/MultiApp

```

**Step 2 :** Set Up Environment and Dependencies

* Install Python : Ensure Python (preferably Python 3.x) is installed on your system.

* Install Required Libraries : Navigate to the project directory and install the necessary Python libraries by running -

```
      pip install -r requirements.txt
```

If there's a requirements.txt file in the project, this command installs all the dependencies needed for the project to run.

**Step 3 :** Upgrade the Chatbot's Database 

* Go to the /bot/ directory.

* Open the training_data.txt file.

* Add your custom data in the given format.

* Save the changes to the training_data.txt file.

* Run the following commands in your terminal :

```
    python manage.py makemigrations
    python manage.py migrate

```

**Step 4 :** Configure and Run the Project

* Dataset Setup : Ensure the datasets are placed in the appropriate directory (Datasets/) within the project structure as required by the code.

* Adjust Configuration (if required) : Modify any configuration parameters in the code if needed, such as file paths.

* Run the Application : Launch the Django application that powers the disease prediction and chatbot features -

```
    python manage.py runserver
```

* **Accessing the Application :** Once the Django application is running, access it through your web browser using the provided address (usually http://127.0.0.1:5000/ or http://localhost:5000/). 

## Video


https://github.com/AkshataKamerkar/MultiApp/assets/98729105/fbe4388e-462a-474a-9b4f-72d1efd4339a





## Conclusion

The Multi-App Django Application provides a comprehensive solution for users seeking a seamless integration of a Chatbot, Weather App, and To-Do List App. With customization options and the use of web scraping technologies, this project offers a rich and interactive user experience. Explore the various features and functionalities to enhance your conversational, weather, and task management needs.
