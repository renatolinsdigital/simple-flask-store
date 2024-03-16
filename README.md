# Simple Flask Store App

SimpleStore is a lightweight e-commerce platform built with Flask, designed as a portfolio piece that can be enhanced to become a full-fledged online store for individuals looking to sell various products such as books, clothes, jewelry, and more.

# Features

* Product Catalog: Display a catalog of products with details like name, description, price, and images.

* User Authentication: Secure user registration and authentication mechanisms to manage user accounts.

* Shopping Cart: Allow users to add products to their cart, manage quantities, and proceed to checkout.

* Checkout Process: Guide users through a seamless checkout process, collecting shipping information and payment details.

* Order Management: Create orders with unique IDs, track order status, and manage order history.

* Admin Dashboard: Admin panel to manage products, orders, customers, and inventory.

* Email Notifications: Send email notifications for order confirmation, status updates, and shipping tracking.

* Payment Integration: Integrate payment gateways for secure online transactions.

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

# Considerations for those planning to deploy this app:

If you intend to deploy this application, ensure that you never share the __.env__ file, as it may contain sensitive information such as environment variables or Flask secret keys (used for session management). In this example, I am providing a __.env__ file solely for demonstration purposes in my portfolio, but in a real-world scenario, you should keep such files private and never expose them publicly. You can, however, include the __.env.example__ file in your repository as a template for configuring environment-specific variables in various deployment environments.
