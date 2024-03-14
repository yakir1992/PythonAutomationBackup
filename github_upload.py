import os
from datetime import datetime
from github import Github

# GitHub credentials
USERNAME = "your_username"
PASSWORD = "your_password_or_personal_access_token"
REPO_NAME = "your_repository_name"
FOLDER_PATH = "/path/to/your/folder"

def upload_to_github():
    # Authenticate to GitHub
    g = Github(USERNAME, PASSWORD)

    # Get the repository
    repo = g.get_user().get_repo(REPO_NAME)

    # Create a new commit with the contents of the folder
    commit_message = f"Upload at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    try:
        for filename in os.listdir(FOLDER_PATH):
            with open(os.path.join(FOLDER_PATH, filename), 'rb') as file:
                content = file.read()
                repo.create_file(filename, commit_message, content)
        print("Upload successful.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    upload_to_github()

