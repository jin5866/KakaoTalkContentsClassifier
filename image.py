import os

if __name__ == "__main__":
    root_dir = "./contents/"
    for (root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                file_path = os.path.join(root,file_name)
