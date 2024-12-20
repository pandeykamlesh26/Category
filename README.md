# Category

Category is a Django app to facilitate web-based category management.

Quick start
-----------

1. Add "Category" to your INSTALLED_APPS setting like this::

    ``INSTALLED_APPS = [
        ...,
        "category",
    ]``

2. Include the Category URLconf in your project urls.py like this::

    ``path("category/", include("category.urls")),``

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a category.

5. Visit the ``/category/`` URL to participate in the category.