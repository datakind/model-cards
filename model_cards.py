# Databricks notebook source
# Model overview 
# Dynamic/Replicable Table Creation
class TableRenderer:
    def __init__(self):
        self._table_data = {}

    @property
    def table_data(self):
        return self._table_data

    @table_data.setter
    def table_data(self, value):
        if isinstance(value, dict) and all(isinstance(v, list) for v in value.values()):
            self._table_data = value
        else:
            raise ValueError("table_data must be a dictionary with lists as values")

class ImageWithDescription:
    def __init__(self):
        self._img_src = ""
        self._description = ""

    @property
    def img_src(self):
        return self._img_src

    @img_src.setter
    def img_src(self, value):
        self._img_src = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
        
class ModelOverview:
    def __init__(self):
        self._description = ""
        self._version = []
        self._owners = []
        self._references = []

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if isinstance(value, list) and all(isinstance(v, dict) and 'name' in v and 'date' in v for v in value):
            self._version = value
        else:
            raise ValueError("Version must be a list of dictionaries with 'name' and 'date' keys")

    @property
    def owners(self):
        return self._owners

    @owners.setter
    def owners(self, value):
        if isinstance(value, list) and all(isinstance(o, dict) and 'name' in o and 'contact' in o for o in value):
            self._owners = value
        else:
            raise ValueError("Owners must be a list of dictionaries with 'name' and 'contact' keys")

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, value):
        if isinstance(value, list) and all(isinstance(r, dict) and 'description' in r and 'url' in r for r in value):
            self._references = value
        else:
            raise ValueError("References must be a list of dictionaries with 'description' and 'url' keys")

# Model Considerations Section
class ModelConsiderations:
    def __init__(self):
        self._intended_users = []
        self._use_cases = []
        self._limitations = []

    @property
    def intended_users(self):
        return self._intended_users

    @intended_users.setter
    def intended_users(self, value):
        if isinstance(value, list):
            self._intended_users = value
        else:
            raise ValueError("Intended users must be a list.")

    @property
    def use_cases(self):
        return self._use_cases

    @use_cases.setter
    def use_cases(self, value):
        if isinstance(value, list):
            self._use_cases = value
        else:
            raise ValueError("Use cases must be a list.")

    @property
    def limitations(self):
        return self._limitations

    @limitations.setter
    def limitations(self, value):
        if isinstance(value, list):
            self._limitations = value
        else:
            raise ValueError("Limitations must be a list.")

# Model Parameters Section
class ModelParameters:
    def __init__(self):
        self._outcome_definition = ""
        self._model_optimization_metric = []
        self.table_renderer = TableRenderer()

    @property
    def outcome_definition(self):
        return self._outcome_definition

    @outcome_definition.setter
    def outcome_definition(self, value):
        self._outcome_definition = value

    @property
    def model_optimization_metric(self):
        return self._model_optimization_metric

    @model_optimization_metric.setter
    def model_optimization_metric(self, value):
        if isinstance(value, list):
            self._model_optimization_metric = value
        else:
            raise ValueError("Model optimization metric must be a list.")
    
    def feature_selection(self, table_data):
        """
        Accepts a dictionary where keys are column headers and values are lists of column data.
        This method sets the table data for the TableRenderer.
        """
        self.table_renderer.table_data = table_data

    def get_table_data(self):
        """
        Returns the current table data for rendering in the template.
        """
        return self.table_renderer.table_data
    
# Model Results Section
class ModelResults:
    def __init__(self):
        self._img_src = ""
        self._description = ""
        self._performance_metrics = []  # This will store a list
        self._plot_images = []

    @property
    def img_src(self):
        return self._img_src

    @img_src.setter
    def img_src(self, value):
        self._img_src = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def performance_metrics(self):
        return self._performance_metrics

    @performance_metrics.setter
    def performance_metrics(self, value):
        if isinstance(value, list):
            self._performance_metrics = value
        else:
            raise ValueError("Performance metrics must be a list.")
    
    @property
    def plot_images(self):
        return self._plot_images

    @plot_images.setter
    def plot_images(self, value):
        if isinstance(value, list) and all(isinstance(r, dict) and 'description' in r and 'img_base64' in r for r in value):
            self._plot_images = value
        else:
            raise ValueError("References must be a list of dictionaries with 'description' and 'img_base64' keys")



# COMMAND ----------

from jinja2 import Environment, FileSystemLoader
import os

class ModelCard:
    def __init__(self):
        self.overview = ModelOverview()
        self.considerations = ModelConsiderations()
        self.parameters = ModelParameters()
        self.results = ModelResults()
        self.table_renderer = TableRenderer()
        self.image_with_description = ImageWithDescription()     # Initialize other sections similarly

        # Initialize other sections as before

    def render_html(self):
        # Load the Jinja2 template environment
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('model_cards.html')
        return template.render(overview=self.overview, considerations=self.considerations, parameters=self.parameters)


# COMMAND ----------

model_card = ModelCard()

# Setting Overview
model_card.overview.description = "This model predicts whether a transaction is fraudulent."
model_card.overview.version = [{"name": "1.0", "date": "2021-05-20"}]
model_card.overview.owners = [{"name": "John Doe", "contact": "john.doe@example.com"}]
model_card.overview.references = [
    {"description": "Project Repository", "url": "https://github.com/example/project"}
]

# Setting Considerations
model_card.considerations.intended_users = ["Data Scientists", "Financial Analysts"]
model_card.considerations.use_cases = ["Fraud detection", "Risk assessment"]
model_card.considerations.limitations = ["Requires large datasets", "Not suitable for real-time predictions"]

# Setting Parameters
model_card.parameters.outcome_definition = "Whether a transaction is fraudulent based on historical data."
model_card.parameters.model_optimization_metrics = [
    {"metric": "Accuracy", "value": "95%"},
    {"metric": "Precision", "value": "93%"}
]
model_card.parameters.feature_selection({
    'Metric': ['Accuracy', 'Precision', 'Recall'],
    'Test Value': ['95%', '93%', '92%'],
    'Validation Value': ['94%', '92%', '90%']
})

# Setting Results
model_card.results.feature_importance_image = "path/to/image.jpg"
model_card.results.description = "Feature importance in fraud detection model."
model_card.results.performance_metrics = [
    {"metric": "ROC AUC", "value": "0.97"},
    {"metric": "F1 Score", "value": "0.94"}
]

# Render HTML
html_content = model_card.render_html()

# Write HTML Output to a File
output_file_path = 'output_model_card.html'
with open(output_file_path, 'w') as file:
    file.write(html_content)

print(f"HTML output has been written to {output_file_path}")


# COMMAND ----------


