# Grouping Patent Texts for Mobile Communication Analysis

This project aims to group patent claims into topics using various models. It facilitates an interactive tool that allows users to select the number of groups and see the names and number of claims in each group.

## Installation & Running the Project
1. Setup: Ensure you have the required libraries installed. You can install the dependencies using:
`pip install -r requirements.txt`

2. Run the Application: Execute the main application script to start the web interface:
`python app.py`

3. Access the Interface: Open a web browser and navigate to http://localhost:5000 to interact with the tool.

## Project Structure
project/

├── scraper/<br />
│ ├── **init**.py<br />
│ ├── extract.py<br />
│ ├── parser.py<br />
│ ├── group_claims.py<br />
├── templates/<br />
│ └── index.html<br />
└── app.py<br />
└── analysis_notebook.ipynb<br />
└── requirements.txt<br />

## Directory and File Descriptions
scraper/: Contains scripts for extracting and parsing patent claims data.<br />
**init**.py: Initializes the scraper module.<br />
extract.py: Contains functions to scrape patent pages and extract claims.<br />
parser.py: Parses the HTML content to extract the relevant claims sections.<br />
group_claims.py: Implements the functions for grouping claims using LDA (Latent Dirichlet Allocation).<br />
templates/: Contains HTML templates for the web interface.<br />
index.html: The main HTML template for displaying the grouped claims.<br />
app.py: The main application script that runs the web interface and handles user interactions.<br />
analysis_notebook.ipynb: Jupyter Notebook containing the analysis and comparison of different 3 clustering models.<br />

## Task 1: Extracting text from patents
Using BeautifulSoup, I automated the process of extracting claims text from three specified patent URLs. The solution involves fetching the HTML content of each patent page, parsing it to locate the claims section, and then extracting the text of each claim. This method ensures efficient and accurate retrieval of the required claims data.

## Task 2: Grouping claims by topic

The analysis notebook explores three different clustering models for grouping patent claims:

1. K-Means Clustering: A centroid-based algorithm that partitions the data into a predefined number of clusters. It assigns each claim to the cluster with the nearest mean value. This method is straightforward and effective for large datasets but doesn't consider the context of the claims.

2. LDA (Latent Dirichlet Allocation): A probabilistic model that assigns claims to topics based on the words they contain. It considers the context of the claims, making it suitable for identifying meaningful and coherent topics. This method was ultimately chosen for the project due to its ability to provide contextually relevant titles for each group.

3. Hierarchical Clustering: An agglomerative clustering method that builds a hierarchy of clusters. It starts with each claim as its own cluster and merges them based on their similarity. While this method can capture nested groupings, it can be computationally intensive for large datasets.

## Final Model Choice
After comparing the models, For this assignment, Latent Dirichlet Allocation (LDA) is the most suitable model due to its probabilistic approach, which offers nuanced groupings and richer insights into the themes underlying the claims. LDA’s topic modeling provides interpretable topics based on word distributions, making it meaningful for users to understand the themes. Despite requiring the number of topics to be specified, LDA’s ability to reveal thematic structures makes it valuable for an interactive application where users can explore different groupings. Overall, LDA balances interpretability and depth, making it an excellent choice for building an interactive and insightful web application for grouping patent claims.
K-Means selects headers for each group by identifying the term with the highest average TF-IDF score among the claims in that cluster, reflecting the most prominent term within the grouped claims. In contrast, LDA selects headers based on the highest probability words within each topic, as determined by the probabilistic distribution of words across the entire dataset. This means K-Means headers are straightforward and directly represent dominant terms, while LDA headers provide a thematic representation that offers deeper insights but can be more complex to interpret. For an interactive application, LDA’s nuanced thematic grouping might offer richer user experiences, despite being more computationally intensive than K-Means.

## Task 3: Creating an interactive application
To build an interactive web application, I used Flask to create a basic app that incorporates the paragraph grouping method. The application allows users to specify the number of groups they want, processes the claims from specified patent URLs using LDA, and returns a JSON response with the group titles and the number of claims in each group. Users can interact with the app through an endpoint, providing a dynamic way to analyze and visualize the grouped patent claims.


