# Movie-Recommendation-System

## About

Welcome to the Movie Recommendation System project. This project is a simple user-based movie recommendation system developed using Python and pandas. The system calculates the maximum correlation of one user with the rest of the users in the dataset. Additionally, it compares the viewing history of two users to determine the correlation between them, which is used to suggest personalized movie recommendations to each user.

## Features

- Calculates user-user correlation to identify similar users.
- Provides personalized movie recommendations based on user viewing history.
- Utilizes Python and pandas for data processing and recommendation generation.

## Getting Started

### Prerequisites

Before you can run the Movie Recommendation System, ensure you have the following prerequisites installed:

- Python 3.x
- pandas library

### Installation

Follow these steps to set up and run the system:

1. Clone the repository: `git clone https://github.com/your-username/movie-recommendation.git`
2. Navigate to the project directory: `cd  Movie-Recommendation-System`

### Usage

To use the Movie Recommendation System, follow these steps:

1. Prepare your movie dataset and user viewing history.
   - For movie data, place your "movies_metadata.csv" file in the `data/` directory.
   - For user ratings, place your "ratings.csv" file in the `data/` directory.

2. To use the Movie Recommendation System, follow these steps:

   - Prepare your movie dataset and user viewing history.
   - Run the recommendation script to Recommendation system for choosing Movie: `python MovieRecommendation_Sys.py`.
   - Run the recommendation script to Recommendation System for choosing the movies that only applied for two UserId: `python Recommendation_system.py`
   - The system will generate personalized movie recommendations for each user.

## Contributing

We welcome contributions from the community. If you'd like to contribute to the Movie Recommendation System, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure the code passes all tests.
- Submit a pull request.
