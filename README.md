# Simple Flask Store App (TBD)

SimpleStore is a lightweight e-commerce platform built with Flask, designed as a portfolio piece that can be enhanced to become a full-fledged online store for individuals looking to sell various products such as books, clothes, jewelry, and more.

# Technologies used (TBD)

* Sass for styling
* Python as the backend language
* Flask as the backend web framework
* SQLite as the database (for local development)
* Jinja2 as a template engine for back-end UI rendering
* Vue + Javascript in a 'modular fashion' for generating dynamic content

# Features (WIP)

* Product Catalog: Display a catalog of products with details like name, description, price, and images.
* User Authentication: Secure user registration and authentication mechanisms to manage user accounts.
* Shopping Cart: Allow users to add products to their cart, manage quantities, and proceed to checkout.
* Checkout Process: Guide users through a seamless checkout process, collecting shipping information and payment details.
* Order Management: Create orders with unique IDs, track order status, and manage order history.
* Admin Dashboard: Admin panel to manage products, orders, customers, and inventory.
* Email Notifications: Send email notifications for order confirmation, status updates, and shipping tracking.

# Necessary background to work in this project (TBD)

* Basics of HTML, CSS, Javascript and Sass.
* Python basics: Variables, control structures, functions, lists, etc.
* OOP essential concepts: Objects, classes, inheritance, etc.
* Coding Style and Best Practices: Following Python coding conventions (PEP 8) and adopting best practices for writing clean, readable, and efficient Python code.
* Basics of relational databases (SQL, DDL, DML) and understanding how relationships function.
* Essential knowledge for API creation: Defining endpoints using RESTful principles and HTTP methods like GET (retrieve), POST (create), PUT (update), DELETE (remove), PATCH (partially update), and OPTIONS (get communication options). Additionally, you can think of error handling with status codes, rate limiting, versioning, caching, monitoring, and logging for robust and secure API functionality.
* Flask + SQLAlchemy: Essential knowledge for managing routing, templating, blueprints, assets configuration, database operations, etc.
* Essential web app security knowledge: Implementing parameterized queries to prevent SQL injection attacks, ensuring authentication and authorization using JWT, enabling HTTPS/SSL to encrypt data in transit, securely.managing secret keys for sensitive information, managing app and database sessions securely to prevent session hijacking, implementing data encryption for protecting sensitive data, etc.

# Running and coding in this project

* Have SQLite installed on your machine. You can check the official SQLite website and follow the installation instructions.
* Install Pipenv on your machine with `pip install pipenv`.
* Create a virtual environment with `pipenv --python 3`.
* Activate/reactivate a virtual environment associated to this project with `pipenv shell`.
* Confirm virtual environment creation path with `pipenv --venv`.
* Install project's dependencies using `pipenv install`.
* Run this project with `python app.py` to make sure the data base Path + URI are going to be resolved. After that, you can run this app with `flask run`.
* Open your browser and check the project running with `localhost:5000`.
* Make desired updates as you wish, this project is fully open source.

Once you have completed your coding session, you can stop the development server by pressing `CTRL + C` and exit the virtual environment by using the `exit` command.

# Recommended plugins installation

__Python (by Microsoft)__: Boost your Python development with Microsoft's VS Code extension. Access IntelliSense, linting, debugging, navigation, testing, Jupyter support, and code refactoring in a single, professional package. 

__autopep8 (by Microsoft)__: The Autopep8 VS Code plugin automatically formats Python code to adhere to the PEP 8 style guide within Visual Studio Code. It provides on-the-fly feedback, customizable formatting options, and seamless integration with VS Code, promoting consistent and standardized code formatting.

__Code Spell Checker(by Street Side Software)__:  This extension helps maintain clean and error-free code by highlighting spelling mistakes in comments and strings. It assists in avoiding typos and ensuring code professionalism.

__Jinja (by wholroyd)__: Install this plugin to add Jinja template language support

__General Configuration__: VS Code allow you to customize settings, keybindings, and themes according to your preferences. Explore the features provided by VS Code and its plugins to maximize productivity and efficiency in Python development.

NOTE: To enable automatic code formatting with __autopep8__ when saving Python files, create a folder named __.vscode__ in the root directory where your Python scripts are located. Inside this folder, include a file named __settings.json__ with the following configuration:

```json
{
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8",
    "editor.formatOnSave": true
  }
}
```

After configuring this, you'll notice that Python's coding style guidelines are automatically applied. This includes maintaining a two-line distance between function definitions, adding spaces around operators, and after commas in function arguments, etc. These automated adjustments can save us a lot of time by eliminating the need to manually adhere to PEP 8.

# Some important considerations for those planning to deploy and use this app seriously (And yes, I know, lots of work to do, but that's life)

* Choose a reliable hosting provider to securely host your Flask application. Avoid sharing sensitive information like environment variables or secret keys in the .env file. Instead, use .env.example as a template for configuring your deployment environments.
* Integrate real payment gateways for secure online transactions without storing sensitive financial information such as credit card details on your systems. Leveraging reputable payment gateways like Stripe or PayPal offloads the responsibility of handling payment data to trusted third-party services. This reduces the risk of data breaches and compliance issues while enhancing customer confidence in transaction security. Payment gateways also offer advanced fraud detection, encryption, and PCI DSS compliance measures, improving overall payment processing security.
* Consider improving your Flask API functionality by applying endpoint best practices as the project grows or needs nested endpoints. Implement better error handling with appropriate status codes, incorporate rate limiting, versioning, caching, and set up monitoring and logging for robust and secure API functionality.
* SQLite is ideal for small-scale applications due to its simplicity, but for larger projects with high concurrency, consider using a robust DBMSs like PostgreSQL for better performance and scalability. Also, consider hosting your database on cloud platforms that offer scalable and secure solutions.
* Obtain an SSL/TLS certificate to enable HTTPS and safeguard sensitive information from unauthorized access. Utilize encryption techniques like AES (Advanced Encryption Standard) to encrypt sensitive data both at rest and in transit. Apply encryption protocols to protect data stored in databases, file systems, and communication channels, thereby mitigating the risk of data breaches.
* Implement robust error handling mechanisms that improve logging for better insight and enhance user experience. Differentiate between errors and warnings by logging them accordingly and providing associated visual feedback for users, such as using yellow for warnings and red for errors.
* Set up monitoring tools and logging mechanisms to track system performance, detect anomalies, and monitor for potential security incidents. Use monitoring dashboards and alerts to promptly respond to issues and ensure system reliability.
* Improved app access control: Implement strong access control measures by using role-based access controls (RBAC), multi-factor authentication (MFA), and privilege principles. Limit access to sensitive data and system functionalities based on user roles and responsibilities.
* Regularly update and patch your hosted systems and dependencies to address security vulnerabilities and improve system stability. Follow a structured and scheduled patch management process to minimize risks of having the application down for too long.
* Set up a support form that includes order IDs, allowing you to receive emails and track user issues/tickets related to specific transactions.
* Consider 'dockerizing' your back-end for improved scalability, easier deployment, and streamlined resource management. Dockerization offers benefits such as portability, simplified configuration, enhanced security, and seamless integration with container orchestration tools like Kubernetes.
* Improve data management: Implement data privacy and compliance regulations (e.g., GDPR, HIPAA) as well as database management principles such as access control, data encryption, audit logging, and data masking to ensure data security and regulatory compliance. Additionally, employ backup and recovery strategies, database monitoring and performance tuning, disaster recovery planning, and database optimization techniques for efficient and reliable database management.
* Implement continuous integration and continuous deployment (CI/CD) pipelines for automated testing, building, and deploying backend applications and APIs.
* Create a full-fledged front-end app using popular frameworks: Consider leveraging frameworks such as Angular, React, or Vue as a standalone application to enhance both user experience and development efficiency, particularly as the application scales. By opting for these frameworks, you can benefit from features such as component-based architecture for modular and reusable code, robust state management for maintaining application state, efficient virtual DOM rendering for improved performance, and extensive libraries and ecosystem support for rapid development and integration of complex functionalities. These frameworks also offer advanced tools and debugging capabilities, enabling seamless collaboration among developers and facilitating the implementation of modern UI/UX designs and interactive features.
* Consider adding analytics: If you're treating this website as a serious business, analytics can significantly boost your earnings potential. E-commerce analytics involves tracking user behavior, conversion rates, and marketing effectiveness by monitoring metrics like cart additions, purchases, direct link visits, and referred link visits with user IDs. These insights help businesses understand user interactions, popular products, traffic sources, and marketing ROI, enabling informed decisions to enhance the website, improve user experience, target marketing efforts, and boost sales. 
* Reevaluate your app architecture with a focus on enhancing availability, scalability, performance, and optimizing server resource utilization. Create visual diagrams illustrating your application's functionality and gather feedback to achieve the most effective architecture possible, taking into account the scale of your business and associated costs.
* Think and rethink SEO strategies such as optimizing keywords, improving site speed, enhancing user experience, and creating high-quality content, so your website can be better ranked by search engines.
* Enhance the functionality of the coupon system and explore creative ways to manage it, such as engaging users through marketing campaigns. For instance, users can earn a discount coupon by watching a video, making a purchase of another product, or receiving periodic coupons via marketing-related emails.
* Implement chatbots to not only provide automated support but also to guide users in finding what they are looking for.

The list continues to grow, especially for those looking to establish a thriving e-commerce business. It's crucial to recognize that integrating advanced features into your application may necessitate professional guidance, and the methods of implementation can evolve significantly over time.
