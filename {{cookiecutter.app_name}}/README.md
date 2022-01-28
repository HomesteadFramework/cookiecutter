# Project Created with Homestead

Homestead is a fast, simple and easy to use cli for creating fast and scalable web applications with FASTAPI.

A project scaffold with Homestead is opinionated and includes the following packages/features:
* [FastAPI](https://fastapi.tiangolo.com/) 
* [SQLModel](https://sqlmodel.tiangolo.com/)
* [TailwindCSS](https://tailwindcss.com/)
* [Laravel Mix](https://laravel-mix.com/)
* [FastAPI-Jinja](https://github.com/AGeekInside/fastapi-jinja)

# Architecture

As well as being opinionated, Homestead is also designed around the idea that each feature should be self-contained and
have an easy to use api.

The following folder structure is used and is the recommended structure for Homestead projects. This is the
structure that cli commands will be expecting the files to be in. 

**Modules**

Modules the self-contained "packages" that contain your code and business logic. 

**Middleware** 

Any middleware that you want to use in your project. 

**Providers**

Providers setup as a dependency for your project. These are things such as database connections, logging, etc. 

**Services**

Any global services that you want to use in your project. Your business logic should live here.

**assets**

Directory for your css and js files. 

**templates**

Jinja2 templates for your project. 

**config.py**

Config settings used throughout the app. These use BaseSettings from Pydantic.

**cors.py**

Register your cors settings here.

**main.py**

Entrypoint for your project.

**tailwind.config.js**

Config file for TailwindCSS.

**tsconfig.json**

Typescript config file

**webpack.mix.js**

Config file for Laravel Mix.

**.env.example**

**requirements.txt**

Python requirements file

**package.json**

NPM package file

An example of your .env file. This will contain all the default values for your .env file.



```
.
|-- app
|    | -- middleware
|    | -- modules
|    |    | -- example
|    |    |   | -- controller.py
|    |    |   | -- models.py
|    |    |   | -- schemas.py
|    |    |   | -- services
|    |    |   |   | -- example_service.py
|    | -- providers
|    |    | -- example_provider.py
|    | -- services
|    | -- assets
|    |    | -- css
|    |    | -- js
|    | -- templates
| -- config.py
| -- cors.py
| -- main.py
| -- tailwind.config.js
| -- tsconfig.json 
| -- webpack.mix.js 
```