import argparse
import os


def main():
    """
    Use:  python .\scripts\setup_problem.py --name three_sum --topic Array
    The topic should be within choices set
    """
    parser = argparse.ArgumentParser()
    topic_choices = ["Array"]

    parser.add_argument("--name", type=str, help="Name of the problem separated by underscore.")
    parser.add_argument("--topic", type=str, choices=topic_choices, help="Topic name to create file and dir in")

    args = parser.parse_args()

    name = args.name
    topic = args.topic

    # Create problem file
    py_file_name = f"C:\\Users\\User\\Documents\\Interview Prep\\practice\\src\\{topic}\\{name}.py"
    open(py_file_name, 'w').close()

    # Create directory for ip & op
    dir_path = f"C:\\Users\\User\\Documents\\Interview Prep\\practice\src\\res\\{topic}\\{name}\\"
    os.makedirs(os.path.dirname(dir_path), exist_ok=True)

    # Create input and output files
    open(f"{dir_path}\input.py", 'a').close()
    open(f"{dir_path}\output.py", 'a').close()

if __name__ == "__main__":
    main()
