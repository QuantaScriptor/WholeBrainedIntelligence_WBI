python
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate

# Load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Prepare dataset for Surprise library
def prepare_dataset(data, user_col, item_col, rating_col):
    reader = Reader(rating_scale=(data[rating_col].min(), data[rating_col].max()))
    return Dataset.load_from_df(data[[user_col, item_col, rating_col]], reader)

# Train recommendation model
def train_model(data):
    trainset, testset = train_test_split(data, test_size=0.2)
    algo = SVD()
    algo.fit(trainset)
    return algo, testset

# Evaluate model
def evaluate_model(algo, testset):
    cross_validate(algo, testset, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Generate recommendations
def generate_recommendations(algo, user_id, item_ids, num_recommendations=5):
    predictions = [(item_id, algo.predict(user_id, item_id).est) for item_id in item_ids]
    recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)[:num_recommendations]
    return recommendations

if __name__ == "__main__":
    data = load_data('path_to_your_data.csv')
    dataset = prepare_dataset(data, 'user_id', 'item_id', 'rating')
    algo, testset = train_model(dataset)
    evaluate_model(algo, testset)

    user_id = 1  # Example user ID
    item_ids = [i for i in range(100)]  # Example item IDs
    recommendations = generate_recommendations(algo, user_id, item_ids)
    print(f"Top recommendations for user {user_id}: {recommendations}")
